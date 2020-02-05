library(ggplot2)

data.ie <- read.csv('~/Documents/Courses/algorithms/A2/output.csv')

data.ie$n = as.factor(data.ie$n)

ggplot(data = data.ie, aes(y = log(time), x = n, fill = type)) + geom_boxplot() + theme_minimal()