library(ggplot2)

setwd('/Users/dago/Documents/Courses/algorithms/A11')
data = read.csv('out.csv',sep=';')


data_t1 = data[data$tipo == 1, ]
data_t2 = data[data$tipo == 2, ]

par(mfrow=c(1,2))
hist(data_t1$key,probability = FALSE,ylim = c(0,9000),xlab ='Posición',ylab='Frecuencia',main = 'Módulo')
hist(data_t2$key,probability = FALSE,ylim = c(0,9000),xlab ='Posición',ylab='Frecuencia',main = 'Multiplicación')

agg = aggregate(data, by=list(data$repeticion,data$tipo), FUN=mean, na.rm=TRUE)
agg$tipo = as.factor(agg$tipo)

ggplot(data = agg, aes(y = colision, x = tipo)) + geom_boxplot() + theme_minimal()


