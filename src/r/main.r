# Example Script for R

# retrievee commandline argument for setting the working directory
args = commandArgs(trailingOnly=TRUE)
if (length(args)>0) {
    setwd(args[1])
}

# load dataset
iris <- read.csv("data/orig/IRIS.csv")

# create a simple plot
pdf(file = "results/figures/r_output.pdf")
plot(iris$sepal_length, iris$sepal_width)
dev.off()
