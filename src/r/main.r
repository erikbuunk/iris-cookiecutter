setwd("~/Documents/Computer/Python/iris-cookiecutter")

# load dataset
iris <- read.csv("./data/orig/IRIS.csv")

# create a simple plot
pdf(file = "./results/figures/r_output.pdf")
plot(iris$sepal_length, iris$sepal_width)
dev.off()
