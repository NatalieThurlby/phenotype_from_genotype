# Install specific version of IRkernel that works with our specific version of R
package = "https://cran.r-project.org/package=IRkernel&version=1.1.1"
install.packages('glue')
install.packages('pillar')
install.packages('repr')
install.packages('evaluate')
install.packages('IRdisplay')
install.packages('pbdZMQ')
install.packages('crayon')
install.packages('jsonlite')
install.packages('uuid')
install.packages('digest')

utils::install.packages(pkgs = package, repos = NULL)
IRkernel::installspec()

