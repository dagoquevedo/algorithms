library(ggplot2)

data.ie <- read.csv('~/Documents/Courses/algorithms/A7/A7.csv')

data.ie$n = as.factor(data.ie$n)

ggplot(data = data.ie, aes(y = log(tiempo), x = n, fill = metodo)) + geom_boxplot() + stat_summary(fun.y=mean, geom="line", aes(group=metodo, colour=metodo)) + theme_minimal()

