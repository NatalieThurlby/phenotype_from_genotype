# Install specific version of IRkernel that works with our specific version of R
install.packages('IRkernel', repos="https://cran.r-project.org" )
IRkernel::installspec()
