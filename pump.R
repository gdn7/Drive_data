library(foreign)
library(MASS)
library(nnet)
getwd()
setwd("C:\\Users\\DELL\\Desktop\\Drive_Data")

pump=read.csv(file="Book1.csv")


model = nnet(pump,size=10, linout)
str(pump)

