library(ggplot2)

data <- read.csv('~/Documents/Courses/algorithms/A9/output.csv')

data$n = as.factor(data$n)

ggplot(data = data, aes(y = log(tiempo), x = n, fill = tipo)) + geom_boxplot() + theme_minimal()

