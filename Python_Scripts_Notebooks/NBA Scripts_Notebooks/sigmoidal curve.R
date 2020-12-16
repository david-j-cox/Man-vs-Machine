library(tidyverse)

# Create some random data that might look like something you get
df <- data.frame(earning_budget = c(-8, 4, 1, -1, 10, 14, 0.7, -6, -1.5, 0.2, -12, -14, 12, 8), 
                 proportion_2pt = c(0.15, 0.75, 0.55, 0.45, 0.90, 0.92, 0.55, 0.17, 0.37, 0.5, 0.17, 0.15, 0.93, 0.90))

# Sort it by the x-axis value (this is important for visualization below). 
df <- df[order(df$earning_budget),]

# Here's what the data looks like right now. 
ggplot(data=df, mapping=aes(x=earning_budget, y=proportion_2pt)) + 
  geom_point() +
  xlim(-15, 15) +
  ylim(0, 1)

# sigmoidal function we'l fit to data
f <- function(x, a, b, c) {a/(1 + exp(-b*x))}

# nls is notoriously dependent on starting vals. Rather than pick arbitrary ones, 
# let's fit a rough model to get decent starting values for our paramaters
y ~ exp(log(a) + b + x)
fm_lm <-lm(log(proportion_2pt) ~ earning_budget, df)
starting_params <- list(a=exp(coef(fm_lm)[1]), b = coef(fm_lm)[2])

# fit function
fitmodel <- nls(proportion_2pt ~ f(earning_budget, a, b), df, start=starting_params)

# get the coefficients using the coef function
params=coef(fitmodel)

# function needed for visualization purposes
sigmoid = function(params, x) {
  params[1] / (1 + exp(-params[2] * x))
}

sigmoidal_line <- sigmoid(params, df$earning_budget)


# Plot data with the fit sigmoidal function
ggplot(data=df, mapping=aes(x=earning_budget, y=proportion_2pt)) + 
  geom_point() +
  geom_line(mapping=aes(x=df$earning_budget, y=sigmoidal_line)) +
  xlim(-15, 15) +
  ylim(0, 1)


