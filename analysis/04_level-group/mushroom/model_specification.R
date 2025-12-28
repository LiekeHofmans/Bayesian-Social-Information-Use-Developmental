# Define models

# set priors
prior_blue <- 1 
prior_red  <- 1 # with alpha en beta 1 we have a flat prior

# ------------------------------------------------------------------------------
# Model 0: n_self = nTotal, n_other = 25
# ------------------------------------------------------------------------------

M0.lims <- matrix(c(1,2), nrow=2) # random free parameters; not used
M0 <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  # none
  
  ## Estimate prior
  nPerceived <- d$nTotal
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- 25
  blue_other <- n_other*si/100
  red_other <- n_other - blue_other 
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  likelihood_E2 <- getParamProbBeta(blue_post, red_post, e2/100, .01)
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, si, conf)) 
  
}


# ------------------------------------------------------------------------------
# Model 1a: Perceived own certainty differs from objective certainty
# ------------------------------------------------------------------------------

M1a.lims <- matrix(c(0.1, 100), nrow=2) 
M1a <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha  <- par[1]
  
  ## Estimate prior
  nPerceived <- d$nTotal * alpha
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- 25
  blue_other <- n_other*si/100
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  likelihood_E2 <- getParamProbBeta(blue_post, red_post, e2/100, .01)
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, si, conf)) 
  
}
# ------------------------------------------------------------------------------
# Model 1b: Perceived own certainty differs from objective certainty, differently for each nTotal
# ------------------------------------------------------------------------------

M1b.lims <- matrix(c(0.1, 100, 0.1, 100), nrow=2) 
M1b <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- 25
  blue_other <- n_other*si/100 
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  likelihood_E2 <- getParamProbBeta(blue_post, red_post, e2/100, .01)
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, si, conf)) 
  
}

# ------------------------------------------------------------------------------
# Model 2a: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence same for each peer confidence level
# ------------------------------------------------------------------------------

M2a.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 1000), nrow=2) 
M2a <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta <- par[3]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- theta 
  blue_other <- n_other*si/100
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other 
  red_post <- red_self + red_other 
  
  likelihood_E2 <- getParamProbBeta(blue_post, red_post, e2/100, .01)
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, si, conf)) 
  
}


# ------------------------------------------------------------------------------
# Model 2b: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence linearly depends on peer confidence level
# ------------------------------------------------------------------------------

M2b.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 500, 1, 500), nrow=2)
M2b <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta_IC <- par[3]
  theta_slope <- par[4]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- theta_IC + theta_slope * (conf-1) # low confidence set to 0
  blue_other <- n_other*si/100 
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  
  likelihood_E2 <- getParamProbBeta(blue_post, red_post, e2/100, .01)
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, si, conf)) 
  
}



# ------------------------------------------------------------------------------
# Model 2c: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence different for each peer confidence level
# ------------------------------------------------------------------------------

M2c.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 1000, 1, 1000, 1, 1000), nrow=2) 
M2c <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta_low  <- par[3]
  theta_med  <- par[4]
  theta_high <- par[5]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- ifelse(conf==1, theta_low, ifelse(conf==2, theta_med, theta_high))
  blue_other <- n_other*si/100
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  
  
  likelihood_E2 <- getParamProbBeta(blue_post, red_post, e2/100, .01)
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, si, conf)) 
  
}


# ------------------------------------------------------------------------------
# Model 3a: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence linearly depends on peer confidence level
#           Add stay bias
# ------------------------------------------------------------------------------
M3a.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 500, 1, 500, 0.01, 0.99), nrow=2)
M3a <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta_IC <- par[3]
  theta_slope <- par[4]
  stay_bias <- par[5]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- theta_IC + theta_slope * (conf-1) # low confidence set to 0
  blue_other <- n_other*si/100
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  # Stay bias
  prob_stay <- stay_bias
  
  
  likelihood_E2 <- vector()
  # -stay or go- 
  for (i in 1:nrow(d)) {
    if (d$estimate1[i] == e2[i]){ # if stay
      likelihood_E2[i] <- prob_stay + (1-prob_stay)*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # LH: added beta distr because there is still a small probability that under move, participant kept their E1
    } else { #if go
      likelihood_E2[i] <- (1-prob_stay)*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # prob of E2, where "go-distribution" equals 1 - prob_stay
    }
  }
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, prob_stay, si, conf)) 
}


# ------------------------------------------------------------------------------
# Model 3b: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence linearly depends on peer confidence level
#           Add stay bias that depends on own certainty
# ------------------------------------------------------------------------------
M3b.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 500, 1, 500, 0.01, 0.99, 0.01, 0.99), nrow=2)
M3b <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta_IC <- par[3]
  theta_slope <- par[4]
  stay_bias_5 <- par[5]
  stay_bias_45 <- par[6]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- theta_IC + theta_slope * (conf-1) # low confidence set to 0
  blue_other <- n_other*si/100 
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  # Stay bias
  prob_stay <- ifelse(d$nTotal==5, stay_bias_5, stay_bias_45)
  
  likelihood_E2 <- vector()
  # -stay or go- 
  for (i in 1:nrow(d)) {
    if (d$estimate1[i] == e2[i]){ # if stay
      likelihood_E2[i] <- prob_stay[i] + (1-prob_stay[i])*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # LH: added beta distr because there is still a small probability that under move, participant kept their E1
    } else { #if go
      likelihood_E2[i] <- (1-prob_stay[i])*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # prob of E2, where "go-distribution" equals 1 - prob_stay
    }
  }
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, prob_stay, si, conf)) 
  
}


# ------------------------------------------------------------------------------
# Model 3c: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence linearly depends on peer confidence level
#           Add stay bias that linearly depends on peer confidence level
# ------------------------------------------------------------------------------
M3c.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 500, 1, 500, 0.01, 0.99), nrow=2)
M3c <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta_IC <- par[3]
  theta_slope <- par[4]
  stay_bias <- par[5]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- theta_IC + theta_slope * (conf-1) # low confidence set to 0
  blue_other <- n_other*si/100
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  # Stay bias
  prob_stay <- stay_bias / conf
  
  
  likelihood_E2 <- vector()
  # -stay or go- 
  for (i in 1:nrow(d)) {
    if (d$estimate1[i] == e2[i]){ # if stay
      likelihood_E2[i] <- prob_stay[i] + (1-prob_stay[i])*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # LH: added beta distr because there is still a small probability that under move, participant kept their E1
    } else { #if go
      likelihood_E2[i] <- (1-prob_stay[i])*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # prob of E2, where "go-distribution" equals 1 - prob_stay
    }
  }
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, prob_stay, si, conf)) 
  
}


# ------------------------------------------------------------------------------
# Model 3d: Perceived own certainty differs from objective certainty, differently for each nTotal
#           Perceived peer confidence linearly depends on peer confidence level
#           Add stay bias that exponentially depends on peer confidence level
# ------------------------------------------------------------------------------
M3d.lims <- matrix(c(0.1, 100, 0.1, 100, 1, 500, 1, 500, 0.01, 0.99), nrow=2)
M3d <- function(par, d, c, mfit=T, fitOn="E2") {
  
  ## Free params
  alpha_5  <- par[1]
  alpha_45  <- par[2]
  theta_IC <- par[3]
  theta_slope <- par[4]
  stay_bias <- par[5]
  
  ## Estimate prior
  nPerceived <- d$nTotal 
  nPerceived <- ifelse(nPerceived==5, nPerceived * alpha_5, nPerceived * alpha_45)
  blue_self <- d$estimate1 * nPerceived / 100 + prior_blue
  red_self <- (100-d$estimate1) * nPerceived / 100 + prior_red
  
  likelihood_E1 <- getParamProbBeta(blue_self, red_self, d$estimate1/100, .01)
  
  ## Estimate posterior
  # SI & E2
  si <- d$estimate_peer
  conf <- d$confidence_peer
  e2 <- d$estimate2
  
  # how do we weigh SI ? 
  n_other <- theta_IC + theta_slope * (conf-1) # low confidence set to 0
  blue_other <- n_other*si/100 
  red_other <- n_other - blue_other
  
  # Posterior (Bayes update)
  blue_post <- blue_self + blue_other
  red_post <- red_self + red_other
  
  # Stay bias
  prob_stay <- stay_bias^conf
  
  
  likelihood_E2 <- vector()
  # -stay or go- 
  for (i in 1:nrow(d)) {
    if (d$estimate1[i] == e2[i]){ # if stay
      likelihood_E2[i] <- prob_stay[i] + (1-prob_stay[i])*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # LH: added beta distr because there is still a small probability that under move, participant kept their E1
    } else { #if go
      likelihood_E2[i] <- (1-prob_stay[i])*getParamProbBeta(blue_post[i],red_post[i],e2[i]/100,.01) # prob of E2, where "go-distribution" equals 1 - prob_stay
    }
  }
  
  ## Output fit 
  if (mfit){
    if (fitOn=="E1E2") {
      cost <- ((sum(log(likelihood_E1))) + sum(log(likelihood_E2)))*-2
    } else {
      cost <- (sum(log(likelihood_E2)))*-2
    }
    return(cost)
  }
  return(cbind(blue_self, red_self, blue_post, red_post, prob_stay, si, conf)) 
  
}

# Create vector of model names 
ms <- c('M0', 'M1a', 'M1b', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M3d')

# Create list of the parameter constraints for each model
lims <- list(M0.lims, M1a.lims, M1b.lims, M2a.lims, M2b.lims, M2c.lims, M3a.lims, M3b.lims, M3c.lims, M3d.lims)
names(lims) <- ms