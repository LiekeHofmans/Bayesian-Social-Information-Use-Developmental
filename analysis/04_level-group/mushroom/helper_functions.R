# Define helper function to run model fitting

# Define likelihood (actually probability, but difference between models is the same, just different scaling) of some param based on beta distribution
getParamProbBeta<- function(a,b,param,int){
  a = a; b = b; param = param
  int = int # range to integrate over
  lw <- param-int # area of integration chosen based on range of param that is meaningful difference .01 
  up <- param+int
  p.param<-1-pbeta(up,a,b,lower.tail=F)-pbeta(lw,a,b,lower.tail=T)
  return(p.param)
}


# Draw start values at random based on parameter limits
# I: model string
# O: start values
rand.starts = function(m){
  start = c();
  lim = lims[[m]];
  for(i in 1:ncol(lim)) start[i] = runif(1,ifelse(lim[1,i] < -1e7,-1e7,lim[1,i]), ifelse(lim[2,i] >  1e7, 1e7,lim[2,i]));start}


# Fit function
# Fit models most models using L-BFGS-B and the BASE using Brent
# Repeat the fitting until nfit successful fits have been obtained
# I: to be fitted data dfit, model string m, number of fits nfit
# O: best fit
get.fit = function(dfit, m, cost, nfit, fitOn){ # dfit = dI
  if(!(cost %in% c("ll","mad","mse"))) stop ("non-existant cost function")
  fit.v = Inf
  fit.c = 0
  sub.id <- dfit[1,1]
  
  
  while(fit.c < nfit){
    startz <- rand.starts(m)
    res.tmp = try(
      optim(startz,
            get(m),
            d = dfit,
            c = cost,
            fitOn = fitOn,
            method = 'L-BFGS-B',
            lower = lims[[m]][1,],upper = lims[[m]][2,],
            hessian = F)                                                   
      
      ,silent=T) 
    if(class(res.tmp) != "try-error"){
      fit.c = fit.c + 1
      if(res.tmp$value < fit.v){
        fit.v = res.tmp$value # get cost value                          
        fit.p = res.tmp$par # get best fitting parameter values
        #fit.h = res.tmp$hessian # get hessian matrix to get uncertainty on parameter estimate on idiv. level
      }
    } 
  }
  if(fit.v != -Inf){ 
    return(c(fit.v,fit.p,sub.id))} 
  else{return(NULL)}
}


## =============================================================================
## Fit parameters
## =============================================================================

# important here you set nfits run for each participant, also which cost function (e.g. "ll")
# I: data, and how many fits
# O: best fit
run = function(dfit, paramfits=T){
  nfits <- 50 # number of starting values to be used for optimization
  c <- "ll"
  fitOn <- "E2"
  fit <- get.fit(dfit,m,c,nfits,fitOn)
  if (paramfits) return(fit)
}
