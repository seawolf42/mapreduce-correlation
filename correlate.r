data <- read.csv('data.csv')
cor(data[sapply(data, is.numeric)])
