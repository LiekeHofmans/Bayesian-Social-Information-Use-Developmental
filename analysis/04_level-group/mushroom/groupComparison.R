
# Clear working directory
rm(list = ls())

library("tidyverse")
library("dplyr")
library("lmerTest")
library("viridis")
library("emmeans")
library("performance")
library("ggeffects")
library("car")


# Set directories
DIR_root_adolescents <- "P:/fMRI Projects/fMRI Project Mushroom Highschool"
DIR_analysis_main <- file.path(DIR_root_adolescents, "analysis")
DIR_this_analysis <- file.path(DIR_analysis_main, "04_level-group/mushroom")
DIR_data <- file.path(DIR_root_adolescents, "bids/derivatives/beh/mushroom")
participants_to_exclude_adolescents <- read.csv(file.path(DIR_analysis_main, "participants_to_exclude.csv"))

DIR_root_adults <- "P:/fMRI Projects/fMRI Project Mushroom"                      
DIR_adult_analysis_main <- file.path(DIR_root_adults, "analysis")
DIR_adult_analysis <- file.path(DIR_adult_analysis_main, "04_level-group/mushroom")
DIR_adult_data <- file.path(DIR_root_adults, "bids/derivatives/beh/mushroom")
participants_to_exclude_adults <- read.csv(file.path(DIR_adult_analysis_main, "participants_to_exclude.csv"))

fit.folder <- 'results_fit_sample'

source(file.path(DIR_analysis_main, "summary_function.R"))
source(file.path(DIR_analysis_main, "raincloud_plots.R"))

# Load behavioral data: task
df_mushroom_adolescents <- read.csv(file.path(DIR_data, "group_task-mushroom_preproc-trialwise.csv"))
df_mushroom_adults <- read.csv(file.path(DIR_adult_data, "group_task-mushroom_preproc-trialwise.csv"))
df_all <- rbind(df_mushroom_adolescents, df_mushroom_adults)
df_all$group <- ifelse(df_all$sID < 200, "adults", "adolescents")

# Load behavioral data: practice
df_practice_adolescents <- read.csv(file.path(DIR_data, "group_task-mushroom_preproc-practice_trialwise.csv"))
df_practice_adults <- read.csv(file.path(DIR_adult_data, "group_task-mushroom_preproc-practice_trialwise.csv"))
df_practice <- rbind(df_practice_adolescents, df_practice_adults)
df_practice$group <- ifelse(df_practice$sID < 200, "adults", "adolescents")

# Load demographics
df_age_adolescents <- read.csv(file.path(DIR_root_adolescents, "bids/derivatives/qnr/demographics/group_demographics.csv"))
df_age_adults <- read.csv(file.path(DIR_root_adults, "bids/derivatives/qnr/demographics/group_demographics.csv"))
df_age <- rbind(df_age_adolescents, df_age_adults)

# Combine behavioral and demographic data
df_all <- left_join(df_all, df_age, by = "sID")


## =============================================================================
## Descriptives
## =============================================================================

# Histogram of age
df_unique <- df_all %>% distinct(sID, .keep_all = TRUE)
ggplot(data = df_unique, aes(x = age)) +
  geom_histogram(binwidth = 1, color = "black", fill = "grey") + 
  theme_classic(base_size = 16) 

# Histogram of estimates at E1
# ------------------------------------------------------------------------------
ggplot(data = df_all, aes(x = estimate1)) +
  geom_histogram(binwidth = 3, color = "black", fill = "grey") + 
  scale_x_continuous(breaks = c(0,12.5,25,37.5,50,62.5,75,87.5,100), limits = c(0,100)) +
  theme_classic(base_size = 16) +
  ggtitle("Estimate 1")


# Do participants' estimates at E1 align with the true ratio? Yes
# ------------------------------------------------------------------------------
summ_ind <- summarySE(df_all, measurevar="estimate1", groupvars=c("true_ratio", "nTotal", "sID")) 
summ_group <- summarySE(summ_ind, measurevar="estimate1", groupvars=c("true_ratio", "nTotal"))

ggplot(data = summ_group, aes(x = true_ratio*100, y = estimate1, color = as.factor(nTotal))) +
  geom_abline(intercept = 0, slope = 1) +
  geom_jitter(data = summ_ind, size=2, alpha=0.2, width = 1, height = 1) +
  geom_smooth(method = "lm", se=F) +
  geom_point(size=3) +
  geom_errorbar(aes(ymin=estimate1-se, ymax=estimate1+se), width=.05, size=1) + 
  scale_color_viridis(discrete=TRUE) +
  theme_classic(base_size = 30) +
  xlab("true percentage") + 
  ylab("estimate 1") + 
  scale_color_manual(labels=c("uncertain", "certain"),name="",values = c('#453781FF',"#95D840FF" )) +
  theme(legend.position = c(0.8, 0.25)) + 
  coord_cartesian(xlim=c(0,100), ylim=c(0,100))

# Are participants more accurate relative to the true ratio at high own certainty?
# ------------------------------------------------------------------------------

df_all$deviance1_true <- abs(df_all$estimate1 - df_all$true_ratio*100)

# Difference between certain and uncertain condition
summ_ind <- summarySE(df_all, measurevar="deviance1_true", groupvars=c("nTotal", "sID"))
summ_group <- summarySE(summ_ind, measurevar="deviance1_true", groupvars=c("nTotal")) 
ggplot(data = summ_group, aes(x = as.factor(nTotal), y = deviance1_true)) +
  geom_line(data = summ_ind, aes(group = sID), alpha = 0.2) +
  geom_point(size=2, color = "#7B168C") +
  geom_errorbar(aes(ymin=deviance1_true-se, ymax=deviance1_true+se), width=0.2, size = 2, color = "#7B168C") +
  theme_classic(base_size = 30) +
  scale_x_discrete(name = "condition", labels = c("5"="uncertain", "45"="certain")) +
  ylab("deviance from true ratio")

summ_ind <- summ_ind[order(summ_ind$nTotal, summ_ind$sID), ]
t.test(deviance1_true ~ nTotal, summ_ind, paired=TRUE) # t(131) = 0.40, p = 0.689
mean(summ_ind$deviance1_true[summ_ind$nTotal==5]); mean(summ_ind$deviance1_true[summ_ind$nTotal==45])

# Difference in condition difference between adolescents and adults
summ_ind <- summarySE(df_all, measurevar="deviance1_true", groupvars=c("nTotal", "sID", "group")) 
summ_group <- summarySE(summ_ind, measurevar="deviance1_true", groupvars=c("nTotal", "group"))
summ_group$nTotal <- ifelse(summ_group$nTotal==5, 1, 2)
ggplot(data = summ_ind, aes(x = as.factor(nTotal), y = deviance1_true, color = as.factor(group))) +
  geom_flat_violin(aes(fill = as.factor(group)), alpha = 0.4, position = position_nudge(x = 0.1))+
  geom_point(position = position_jitter(width = .05, height = 0), size = 2.5, shape = 20, alpha=0.2)+
  geom_line(data = summ_group, aes(x = nTotal, y = deviance1_true, color = as.factor(group)), size = 1.2, position = position_nudge(x = 0.1)) +
  geom_errorbar(data = summ_group, aes(x = nTotal, ymin=deviance1_true-se, ymax=deviance1_true+se, color = as.factor(group)), width=0.2, size = 1.5, position = position_nudge(x = 0.1)) +
  geom_point(data = summ_group, aes(x = nTotal, y = deviance1_true, color = as.factor(group)), size=2.5, position = position_nudge(x = 0.1)) +
  theme_classic(base_size = 30) +
  ylab("deviance from true ratio") +
  scale_x_discrete(name = "condition", labels = c("5"="uncertain", "45"="certain")) +
  theme(legend.position = c(0.8, 0.25), legend.title = element_blank()) 

summ_adolescents_5 <- summarySE(df_all[df_all$group=="adolescents" & df_all$nTotal==5,], measurevar="deviance1_true", groupvars=c("sID"))
summ_adolescents_45 <- summarySE(df_all[df_all$group=="adolescents" & df_all$nTotal==45,], measurevar="deviance1_true", groupvars=c("sID"))
summ_adolescents <- summ_adolescents_5
summ_adolescents$condition_difference <- summ_adolescents_45$deviance1_true - summ_adolescents_5$deviance1_true

summ_adults_5 <- summarySE(df_all[df_all$group=="adults" & df_all$nTotal==5,], measurevar="deviance1_true", groupvars=c("sID"))
summ_adults_45 <- summarySE(df_all[df_all$group=="adults" & df_all$nTotal==45,], measurevar="deviance1_true", groupvars=c("sID"))
summ_adults <- summ_adults_5
summ_adults$condition_difference <- summ_adults_45$deviance1_true - summ_adults_5$deviance1_true

t.test(summ_adolescents$condition_difference, summ_adults$condition_difference, paired=FALSE) # t(126.46) = -0.05, p = 0.962

# Overall social information use
# ------------------------------------------------------------------------------
summ_all <- summarySE(df_all, measurevar="s", groupvars=c("sID")); mean(summ_all$s) # mean s = 0.37
t.test(summ_all$s, mu = 0.5) # egocentric discounting: t(131) = -11.524, p < 0.001

summ_adult <- summarySE(df_mushroom_adults, measurevar="s", groupvars=c("sID")) 
summ_adolescent <- summarySE(df_mushroom_adolescents, measurevar="s", groupvars=c("sID")) 
t.test( summ_adolescent$s, summ_adult$s) # adolescents: 0.36, adults: 0.39, t(129.1)=-1.37, p = 0.172


# histogram of s (trialwise)
ggplot(data = df_all, aes(x=s)) +
  geom_histogram(fill="grey", color = "black", bins = 20) +
  theme_classic(base_size = 30) +
  geom_vline(aes(xintercept = mean(s)), size = 1, color = "red") +
  xlab("social information use (s)")

# histogram of mean S per participant
summ_ind <- summarySE(df_all, measurevar="s", groupvars=c("sID"))
ggplot(data = summ_ind, aes(x=s)) +
  geom_histogram(fill="grey", color = "black") +
  theme_classic(base_size = 30) +
  #geom_vline(aes(xintercept = mean(s)), size = 1, color = "red") +
  xlab("mean social information use (S)")


# overall percentage of stay trials
# ------------------------------------------------------------------------------
percentage_zero_adolescents <- df_mushroom_adolescents %>%
  dplyr::group_by(sID) %>%
  dplyr::summarise(percentage_zero = mean(s == 0))
percentage_zero_adults <- df_mushroom_adults %>%
  dplyr::group_by(sID) %>%
  dplyr::summarise(percentage_zero = mean(s == 0))
t.test( percentage_zero_adolescents$percentage_zero, percentage_zero_adults$percentage_zero) # adults: 0.16, adolescents: 0.19, t(129.02)=0.86, p = 0.392


# Certainty level and self-reported confidence
# ------------------------------------------------------------------------------

# plot
summ_ind <- summarySE(df_all, measurevar="confidence_rating", groupvars=c("nTotal", "sID", "group")) 
summ_group <- summarySE(summ_ind, measurevar="confidence_rating", groupvars=c("nTotal", "group"))
summ_group$nTotal <- ifelse(summ_group$nTotal==5, 1, 2)
ggplot(data = summ_ind, aes(x = as.factor(nTotal), y = confidence_rating, color = as.factor(group))) +
  geom_flat_violin(aes(fill = as.factor(group)), alpha = 0.4, position = position_nudge(x = 0.1))+
  geom_point(position = position_jitter(width = .05, height = 0), size = 2.5, shape = 20, alpha=0.2)+
  geom_line(data = summ_group, aes(x = nTotal, y = confidence_rating, color = as.factor(group)), size = 1.2, position = position_nudge(x = 0.1)) +
  geom_errorbar(data = summ_group, aes(x = nTotal, ymin=confidence_rating-se, ymax=confidence_rating+se, color = as.factor(group)), width=0.2, size = 1.5, position = position_nudge(x = 0.1)) +
  geom_point(data = summ_group, aes(x = nTotal, y = confidence_rating, color = as.factor(group)), size=2.5, position = position_nudge(x = 0.1)) +
  theme_classic(base_size = 30) +
  ylab("mean confidence rating") +
  scale_x_discrete(name = "condition", labels = c("5"="uncertain", "45"="certain")) +
  theme(legend.position = c(0.8, 0.25), legend.title = element_blank()) 

# interaction age * certainty?
summ_ind$group <- factor(summ_ind$group, levels = c("adults", "adolescents"))
fit_confidenceRating <- lmerTest::lmer(confidence_rating ~ as.factor(nTotal)*group + 
                                      (1 | sID),
                                    data=summ_ind, 
                                    control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_confidenceRating)
emm_confidenceRating <- emmeans(fit_confidenceRating, ~ as.factor(group) | as.factor(nTotal))
summary(emm_confidenceRating)
pairs(emm_confidenceRating)


## =============================================================================
## Compare model free behavior adolescents with adults
## =============================================================================

df_all$confidence_peer_c <- df_all$confidence_peer-2 # set medium confidence to 0
df_all$nTotal_ind <- as.numeric(ifelse(df_all$nTotal==5, -0.5, 0.5)) # change to: uncertain = -0.5; certain = 0.5
df_all$group_ind <- as.numeric(ifelse(df_all$group=="adults", -0.5, 0.5)) # change to: adults = -0.5; adolescents = 0.5
df_all$deviance <- abs(df_all$true_ratio*100 - df_all$estimate1)

# Deviance
# =================================================
fit <- lmer(deviance ~ nTotal_ind*group_ind + (1 + nTotal_ind | sID), data = df_all)
summary(fit)

summ_ind <- summarySE(df_all, measurevar="deviance", groupvars=c("nTotal", "sID", "group")) 
summ_group <- summarySE(summ_ind, measurevar="deviance", groupvars=c("nTotal", "group"))
summ_group$nTotal <- ifelse(summ_group$nTotal==5, 1, 2)
ggplot(data = summ_ind, aes(x = as.factor(nTotal), y = deviance, color = as.factor(group))) +
  geom_flat_violin(aes(fill = as.factor(group)), alpha = 0.4, position = position_nudge(x = 0.1))+
  geom_point(position = position_jitter(width = .05, height = 0), size = 2.5, shape = 20, alpha=0.2)+
  geom_line(data = summ_group, aes(x = nTotal, y = deviance, color = as.factor(group)), size = 1.2, position = position_nudge(x = 0.1)) +
  geom_errorbar(data = summ_group, aes(x = nTotal, ymin=deviance-se, ymax=deviance+se, color = as.factor(group)), width=0.2, size = 1.5, position = position_nudge(x = 0.1)) +
  geom_point(data = summ_group, aes(x = nTotal, y = deviance, color = as.factor(group)), size=2.5, position = position_nudge(x = 0.1)) +
  theme_classic(base_size = 30) +
  ylab("deviance") +
  scale_x_discrete(name = "condition", labels = c("5"="uncertain", "45"="certain")) +
  theme(legend.position = "none")


# Confidence ratings and deviance (practice trials)
# =================================================
df_practice$deviance <- abs(df_practice$true_ratio*100 - df_practice$estimate1)

# stats: calculate correlation per subject, then check if correlation is different across groups
subject_r2 <- df_practice %>%
  dplyr::group_by(sID, group) %>%
  dplyr::summarise(
    r = cor(confidence_rating, deviance, method = "pearson", use = "complete.obs"),
    r2 = r^2
  )
t.test(r2 ~ group, data = subject_r2)


# plot
model_adolescents <- lmer(deviance ~ scale(confidence_rating, scale=F) + (1 + scale(confidence_rating, scale=F) | sID), data = df_practice[df_practice$group=="adolescents",])
group_pred_adolescents <- ggpredict(model_adolescents, terms = "confidence_rating")
model_adults <- lmer(deviance ~ scale(confidence_rating, scale=F) + (1 + scale(confidence_rating, scale=F) | sID), data = df_practice[df_practice$group=="adults",])
group_pred_adults <- ggpredict(model_adults, terms = "confidence_rating")

ggplot(df_practice, aes(x = confidence_rating, y = deviance)) +
  geom_line(aes(group = sID, color = group), stat="smooth", method = "lm", size = 0.1, se = FALSE, alpha = 0.2) +
  geom_line(data = group_pred_adolescents, aes(x = x, y = predicted), color = "#F8766D", size = 1.2) +
  geom_line(data = group_pred_adults, aes(x = x, y = predicted), color = "#00BFC4", size = 1.2) +
  labs(x = "confidence rating", y = "deviance practice trials") +
  theme_classic(base_size = 30) +
  coord_cartesian(xlim=c(1,3), ylim=c(0,60)) +
  scale_x_continuous(breaks = c(1, 2, 3)) +
  theme(legend.position = "none")

# Effects on social information use
# =================================

# LMER across groups
fit_all <- lmerTest::lmer(s ~ nTotal_ind*confidence_peer_c + 
                        (1 + nTotal_ind*confidence_peer_c| sID),
                      data=df_all, 
                      control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_all) 
standardize_parameters(fit_all) # standardized betas
performance::icc(fit_all, tolerance = 1e-9) # ICC = 0.505
performance::r2(fit_all, tolerance = 1e-9)

# LMER group comparison
fit_age <- lmerTest::lmer(s ~ nTotal_ind*confidence_peer_c*group_ind + 
                                    (1 + nTotal_ind*confidence_peer_c| sID),
                                  data=df_all, 
                                  control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_age) 
standardize_parameters(fit_age) # standardized betas
performance::icc(fit_age, tolerance = 1e-9) # ICC = 0.499 (variance due to between-subject differences)
performance::r2(fit_age, tolerance = 1e-9) # R2 (explained variance)



# Test age effect per certainty condition
# Rerun lmer with factors, as emmeans requires it (equivalent results as above)
fit_age_emmeans <- lmerTest::lmer(s ~ as.factor(nTotal_ind)*confidence_peer_c*as.factor(group_ind) + 
                                   (1 + as.factor(nTotal_ind)*confidence_peer_c| sID),
                                 data=df_all, 
                                 control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
emm_age_by_certainty <- emmeans(fit_age_emmeans, ~ as.factor(group_ind) | as.factor(nTotal_ind))
summary(emm_age_by_certainty)
pairs(emm_age_by_certainty)

# Test certainty effect per age group
emm_certainty_by_age <- emmeans(fit_age_emmeans, ~ as.factor(nTotal_ind) | as.factor(group_ind))
summary(emm_certainty_by_age)
pairs(emm_certainty_by_age)

# Plot Adolescents
summ_ind <- summarySE(df_all[df_all$group=="adolescents",], measurevar="s", groupvars=c("nTotal", "confidence_peer", "sID")) 
summ_group <- summarySE(summ_ind, measurevar="s", groupvars=c("nTotal", "confidence_peer"))

ggplot(data = summ_group, aes(x = as.factor(confidence_peer), y = s, color = as.factor(nTotal))) +
  geom_line(data = summ_ind, aes(group = interaction(as.factor(nTotal),sID)), alpha = 0.2) +
  geom_line(aes(x = confidence_peer), size = 1.2) +
  geom_point(size = 2) + 
  geom_errorbar(aes(ymin=s-se, ymax=s+se), size=2, width = 0.2) +
  theme_classic(base_size = 30) +
  scale_color_manual(labels=c("low", "high"),name="own certainty",values = c('#453781FF',"#95D840FF" )) + 
  scale_x_discrete(name = "peer confidence", labels = c("1"="low", "2"="medium", "3"="high")) +
  coord_cartesian(ylim = c(0,1)) +
  ylab("social information use") + 
  ggtitle("Adolescents") +
  theme(legend.position = 'none')

# Plot Adults
summ_ind <- summarySE(df_all[df_all$group=="adults",], measurevar="s", groupvars=c("nTotal", "confidence_peer", "sID")) 
summ_group <- summarySE(summ_ind, measurevar="s", groupvars=c("nTotal", "confidence_peer"))

ggplot(data = summ_group, aes(x = as.factor(confidence_peer), y = s, color = as.factor(nTotal))) +
  geom_line(data = summ_ind, aes(group = interaction(as.factor(nTotal),sID)), alpha = 0.2) +
  geom_line(aes(x = confidence_peer), size = 1.2) +
  geom_point(size = 2) + 
  geom_errorbar(aes(ymin=s-se, ymax=s+se), size=2, width = 0.2) +
  theme_classic(base_size = 30) +
  scale_color_manual(labels=c("low", "high"),name="own certainty",values = c('#453781FF',"#95D840FF" )) + 
  scale_x_discrete(name = "peer confidence", labels = c("1"="low", "2"="medium", "3"="high")) +
  coord_cartesian(ylim = c(0,1)) +
  ylab("social information use") + 
  ggtitle("Adults") +
  theme(legend.position = 'none')


# Plot both
summ_ind <- summarySE(df_all, measurevar="s", groupvars=c("nTotal", "confidence_peer", "sID", "group")) 
summ_group <- summarySE(summ_ind, measurevar="s", groupvars=c("nTotal", "confidence_peer", "group"))

ggplot(data = summ_group, aes(
           x = as.factor(confidence_peer), 
           y = s, 
           color = as.factor(nTotal), 
           linetype = as.factor(group), 
           group = interaction(group, nTotal))) +
  geom_line(aes(x = confidence_peer), size = 1.2) +
  geom_point(size = 2) + 
  geom_errorbar(aes(ymin=s-se, ymax=s+se), size=2, width = 0.2) +
  theme_classic(base_size = 30) +
  scale_color_manual(labels=c("uncertain", "certain"),name="",values = c('#453781FF',"#95D840FF" )) +
  scale_linetype_manual(labels = c("adolescents", "adults"), name = "", values = c("adolescents" = "longdash", "adults" = "solid")) +
  scale_x_discrete(name = "peer confidence", labels = c("1"="low", "2"="medium", "3"="high")) +
  coord_cartesian(ylim = c(0,1)) +
  ylab("social information use") + 
  theme(legend.position = 'none')



# sensitivity analysis to test age as a continuous factor
# =======================================================

fit_age_c <- lmerTest::lmer(s ~ nTotal_ind*confidence_peer_c*scale(age, scale=F) + 
                            (1 + nTotal_ind*confidence_peer_c| sID),
                          data=df_all, 
                          control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_age_c) 



# Difference in variance in social information use
# =======================================================
subject_variances <- df_all %>%
  dplyr::group_by(sID, group_ind, nTotal_ind, confidence_peer_c) %>%
  dplyr::summarise(var_si = var(s, na.rm = TRUE), .groups = "drop")

summary(lm(log(var_si + 0.0000001) ~ group_ind*nTotal_ind*confidence_peer_c, data = subject_variances)) # add small error to s to avoid log(0)


# Account for difference in variance between age groups

# First check if modeling unequal variances improves model fit
model_equal_var <- lme(
  s ~ nTotal_ind * confidence_peer_c * group_ind,
  random = ~ nTotal_ind*confidence_peer_c | sID,
  data = df_mushroom, 
  method = "REML"
)

model_unequal_var <- lme(
  s ~ nTotal_ind * confidence_peer_c * group_ind,
  random = ~ nTotal_ind*confidence_peer_c | sID,
  weights = varIdent(form = ~ 1 | group_ind),  # <-- different residual variance per age group
  data = df_mushroom, 
  method = "REML"
)
anova(model_equal_var, model_unequal_var)

# Interpret model while including unequal variances
summary(model_unequal_var)


## =============================================================================
## Compare model free behavior adolescents with adults, only for adolescents included in fMRI analysis
## =============================================================================

df_mushroom_adolescents_subset <- df_mushroom_adolescents[!df_mushroom_adolescents$sID %in% participants_to_exclude_adolescents$exclude_fmri,]
df_mushroom_adults_subset <- df_mushroom_adults[!df_mushroom_adults$sID %in% participants_to_exclude_adults$exclude_fmri,]
df_combined <- rbind(df_mushroom_adults_subset, df_mushroom_adolescents_subset)
df_combined$group <- ifelse(df_combined$sID < 200, "adults", "adolescents")
df_combined <- left_join(df_combined, df_age, by = "sID")

# overall social information use
summ_adult <- summarySE(df_mushroom_adults_subset, measurevar="s", groupvars=c("sID")) 
summ_adolescent <- summarySE(df_mushroom_adolescents_subset, measurevar="s", groupvars=c("sID")) 
t.test( summ_adolescent$s, summ_adult$s) 

# overall percentage of stay trials
percentage_zero_adolescents <- df_mushroom_adolescents_subset %>%
  dplyr::group_by(sID) %>%
  dplyr::summarise(percentage_zero = mean(s == 0))
percentage_zero_adults <- df_mushroom_adults_subset %>%
  dplyr::group_by(sID) %>%
  dplyr::summarise(percentage_zero = mean(s == 0))
t.test( percentage_zero_adolescents$percentage_zero, percentage_zero_adults$percentage_zero) 

# LMER

df_combined$confidence_peer_c <- df_combined$confidence_peer-2 # set medium confidence to 0
df_combined$nTotal_ind <- as.numeric(ifelse(df_combined$nTotal==5, 0.5, -0.5)) # change to indicator variable


fit <- lmerTest::lmer(s ~ nTotal_ind*confidence_peer_c*group + 
                        (1 + nTotal_ind*confidence_peer_c| sID),
                      data=df_combined, 
                      control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit) 




## =============================================================================
## Compare parameters adolescents with adults 
## =============================================================================

# Load data
adolescent_params <- as.data.frame(read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_M3d_fitE2.txt')), sep = " ", header=T))
adult_params <- as.data.frame(read.table(file.path(DIR_adult_analysis, fit.folder, paste0('subject_M3d_fitE2.txt')), sep = " ", header=T))

# Combine datasets and add model based certainty variables
adolescent_params$V8 <- "adolescents"
adult_params$V8 <- "adults"
all_params <- rbind(adolescent_params, adult_params)
all_params$subj_5 <- all_params$V2 * 5 # model based certainty: alpha * number of actual mushrooms
all_params$subj_45 <- all_params$V3 * 45
all_params$subj_diff <- all_params$subj_45 - all_params$subj_5

# First: descriptives across groups
apply(all_params[, c(2:6)], 2, median, na.rm = TRUE) # median parameter values
apply(all_params[, c(9, 10)], 2, median, na.rm = TRUE) # median model based certainty per condition
wilcox.test((all_params[,9]), (all_params[,10]), paired = TRUE) # difference in model based certainty between uncertain and certain condition

# Then: descriptives per group
apply(all_params[all_params$V8 == "adolescents", c(2:6)], 2, median, na.rm = TRUE)
apply(all_params[all_params$V8 == "adults", c(2:6)], 2, median, na.rm = TRUE)
apply(all_params[all_params$V8 == "adolescents", c(9,10)], 2, median, na.rm = TRUE)
apply(all_params[all_params$V8 == "adults", c(9,10)], 2, median, na.rm = TRUE)
wilcox.test(all_params$V2 ~ all_params$V8) # w = 2095, p = 0.714
wilcox.test(all_params$V3 ~ all_params$V8) # w = 1629, p = 0.013
wilcox.test(all_params$V4 ~ all_params$V8) # w = 2111, p = 0.769
wilcox.test(all_params$V5 ~ all_params$V8) # w = 1604.5, p = 0.009
wilcox.test(all_params$V6 ~ all_params$V8) # w = 2527.5, p = 0.103
wilcox.test(all_params$subj_diff ~ all_params$V8) # W = 1482, p = 0.002

# FDR correction
p_values <- c(wilcox.test(all_params$V2 ~ all_params$V8)$p.value,
              wilcox.test(all_params$V3 ~ all_params$V8)$p.value,
              wilcox.test(all_params$V4 ~ all_params$V8)$p.value,
              wilcox.test(all_params$V5 ~ all_params$V8)$p.value,
              wilcox.test(all_params$V6 ~ all_params$V8)$p.value)
p.adjust(p_values, method = "BH") # 0.769 0.032 0.769 0.032 0.172

# PLOTS
# ============

# alpha 5
summ <- summarySE(all_params, measurevar="V2", groupvars=c("V8")) 
ggplot(data = all_params, aes(x = V8, y = V2)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V2), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V2, ymin = V2-se, ymax = V2+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("alpha 5") +
  xlab("") + 
  theme(legend.position = "none") 

# alpha 45
summ <- summarySE(all_params, measurevar="V3", groupvars=c("V8")) 
ggplot(data = all_params, aes(x = V8, y = V3)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V3), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V3, ymin = V3-se, ymax = V3+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("alpha 45") +
  xlab("") + 
  theme(legend.position = "none") 

# theta IC
summ <- summarySE(all_params, measurevar="V4", groupvars=c("V8")) 
ggplot(data = all_params, aes(x = V8, y = V4)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V4), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V4, ymin = V4-se, ymax = V4+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("theta IC") +
  xlab("") + 
  theme(legend.position = "none") 

# theta slope
summ <- summarySE(all_params, measurevar="V5", groupvars=c("V8")) 
ggplot(data = all_params, aes(x = V8, y = V5)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V5), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V5, ymin = V5-se, ymax = V5+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("theta slope") +
  xlab("") + 
  theme(legend.position = "none") 

# stay bias
summ <- summarySE(all_params, measurevar="V6", groupvars=c("V8")) 
ggplot(data = all_params, aes(x = V8, y = V6)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V6), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V6, ymin = V6-se, ymax = V6+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("stay bias") +
  xlab("") + 
  theme(legend.position = "none") 

all_params_long <- 
  all_params %>%
  pivot_longer(
    cols = c(subj_5, subj_45),
    names_to = "nTotal",
    names_prefix = "subj_",
    values_to = "subj_nTotal"
  )

# Uncertain and certain condition separately
all_params_long$nTotal <- ifelse(all_params_long$nTotal=="5", 1, 2)
summ_group <- summarySE(all_params_long, measurevar="subj_nTotal", groupvars=c("nTotal", "V8"))
ggplot(data = all_params_long, aes(x = as.factor(nTotal), y = subj_nTotal, color = as.factor(V8))) +
  geom_flat_violin(aes(fill = as.factor(V8)), alpha = 0.4, position = position_nudge(x = 0.1))+
  geom_point(position = position_jitter(width = .05, height = 0), size = 2.5, shape = 20, alpha=0.2)+
  geom_line(data = summ_group, aes(x = nTotal, y = subj_nTotal, color = as.factor(V8)), size = 1.2, position = position_nudge(x = 0.1)) +
  geom_errorbar(data = summ_group, aes(x = nTotal, ymin=subj_nTotal-se, ymax=subj_nTotal+se, color = as.factor(V8)), width=0.2, size = 1.5, position = position_nudge(x = 0.1)) +
  geom_point(data = summ_group, aes(x = nTotal, y = subj_nTotal, color = as.factor(V8)), size=2.5, position = position_nudge(x = 0.1)) +
  theme_classic(base_size = 30) +
  ylab("model-based certainty") +
  scale_x_discrete(name = "condition", labels = c("1"="uncertain", "2"="certain")) +
  theme(legend.position = "none")

# Difference between certain and uncertain condition
summ <- summarySE(all_params, measurevar="subj_diff", groupvars=c("V8")) 
ggplot(data = all_params, aes(x = V8, y = subj_diff)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = subj_diff), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = subj_diff, ymin = subj_diff-se, ymax = subj_diff+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("certain - uncertain") +
  xlab("") + 
  theme(legend.position = "none") + 
  geom_hline(yintercept=0, linetype="dashed", color = "grey33", size=1)   


# sensitivity analysis to test age as a continuous factor
# =======================================================

all_params <- left_join(all_params, df_age, by = c("V7" = "sID"))
summary(lm(V2 ~ age, data = all_params)) # b = 0.33, p = 0.500
summary(lm(V3 ~ age, data = all_params)) # b = 0.25, p = 0.008
summary(lm(V4 ~ age, data = all_params)) # b = 0.83, p = 0.543
summary(lm(V5 ~ age, data = all_params)) # b = 2.43, p = 0.123
summary(lm(V6 ~ age, data = all_params)) # b = 0.00, p = 0.848
summary(lm(subj_diff ~ age, data = all_params)) # b = 9.59, p = 0.010

# FDR correction
p_values <- c(summary(lm(all_params$V2 ~ all_params$age))$coefficients["all_params$age", "Pr(>|t|)"],
              summary(lm(all_params$V3 ~ all_params$age))$coefficients["all_params$age", "Pr(>|t|)"],
              summary(lm(all_params$V4 ~ all_params$age))$coefficients["all_params$age", "Pr(>|t|)"],
              summary(lm(all_params$V5 ~ all_params$age))$coefficients["all_params$age", "Pr(>|t|)"],
              summary(lm(all_params$V6 ~ all_params$age))$coefficients["all_params$age", "Pr(>|t|)"]
)
p.adjust(p_values, method = "BH") # 0.679 0.041 0.679 0.308 0.848

## =============================================================================
## Compare parameters adolescents with adults, only for adolescents included in fMRI analysis
## =============================================================================

all_params_subset <- all_params[!all_params$V7 %in% participants_to_exclude_adolescents$exclude_fmri,]
all_params_subset <- all_params_subset[!all_params_subset$V7 %in% participants_to_exclude_adults$exclude_fmri,]
adolescent_params_subset <- all_params_subset[all_params_subset$V8 == "adolescents",]
adult_params_subset <- all_params_subset[all_params_subset$V8 == "adults",]

# alpha 5
summ <- summarySE(all_params_subset, measurevar="V2", groupvars=c("V8")) 
ggplot(data = all_params_subset, aes(x = V8, y = V2)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V2), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V2, ymin = V2-se, ymax = V2+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("alpha 5") +
  xlab("") + 
  theme(legend.position = "none") 

# alpha 45
summ <- summarySE(all_params_subset, measurevar="V3", groupvars=c("V8")) 
ggplot(data = all_params_subset, aes(x = V8, y = V3)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V3), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V3, ymin = V3-se, ymax = V3+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("alpha 45") +
  xlab("") + 
  theme(legend.position = "none") 

# theta IC
summ <- summarySE(all_params_subset, measurevar="V4", groupvars=c("V8")) 
ggplot(data = all_params_subset, aes(x = V8, y = V4)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V4), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V4, ymin = V4-se, ymax = V4+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("theta IC") +
  xlab("") + 
  theme(legend.position = "none") 

# theta slope
summ <- summarySE(all_params_subset, measurevar="V5", groupvars=c("V8")) 
ggplot(data = all_params_subset, aes(x = V8, y = V5)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V5), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V5, ymin = V5-se, ymax = V5+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("theta slope") +
  xlab("") + 
  theme(legend.position = "none") 

# stay bias
summ <- summarySE(all_params_subset, measurevar="V6", groupvars=c("V8")) 
ggplot(data = all_params_subset, aes(x = V8, y = V6)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = V6), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = V6, ymin = V6-se, ymax = V6+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("stay bias") +
  xlab("") + 
  theme(legend.position = "none") 


t.test(adolescent_params_subset$V2, adult_params_subset$V2) # p = 0.885
t.test(adolescent_params_subset$V3, adult_params_subset$V3) # p = 0.007 
t.test(adolescent_params_subset$V4, adult_params_subset$V4) # p = 0.353 
t.test(adolescent_params_subset$V5, adult_params_subset$V5) # p = 0.029 
t.test(adolescent_params_subset$V6, adult_params_subset$V6) # p = 0.270 

# Difference in subjective N between certainty conditions
# ------------------------------------------------------------------------------

all_params_subset$subj_5 <- all_params_subset$V2 * 5
all_params_subset$subj_45 <- all_params_subset$V3 * 45
all_params_subset$subj_diff <- all_params_subset$subj_45 - all_params_subset$subj_5
adolescent_params_subset <- all_params_subset[all_params_subset$V8 == "adolescents",]
adult_params_subset <- all_params_subset[all_params_subset$V8 == "adults",]


summ <- summarySE(all_params_subset, measurevar="subj_diff", groupvars=c("V8")) 
ggplot(data = all_params_subset, aes(x = V8, y = subj_diff)) +
  geom_flat_violin(fill="lightsteelblue")+
  geom_point(position = position_jitter(width = .03), size = 2.5, shape = 20, alpha=0.4)+
  geom_point(data = summ, aes(x = V8, y = subj_diff), shape = 18, size = 2.5) +
  geom_errorbar(data = summ, aes(x = V8, y = subj_diff, ymin = subj_diff-se, ymax = subj_diff+se), width = .2, size = 1.4)+
  theme_classic(base_size = 30) +
  ylab("certain - uncertain") +
  xlab("") + 
  theme(legend.position = "none") + 
  geom_hline(yintercept=0, linetype="dashed", color = "grey33", size=1)   


t.test(adolescent_params_subset$subj_diff, adult_params_subset$subj_diff) 
t.test(adolescent_params_subset$subj_5, adolescent_params_subset$subj_45, paired=T) 
t.test(adult_params_subset$subj_5, adult_params_subset$subj_45, paired=T) 


