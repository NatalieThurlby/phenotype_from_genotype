# Install specific version of IRkernel that works with our specific version of R
IRkernel = "https://cran.r-project.org/package=IRkernel&version=1.1.1"
glue = "https://cran.r-project.org/package=glue&version=1.2.0"

utils::install.packages(pkgs = glue, repos = NULL)

install.packages('pillar')
install.packages('repr')
install.packages('evaluate')
install.packages('IRdisplay')
install.packages('pbdZMQ')
install.packages('crayon')
install.packages('jsonlite')
install.packages('uuid')
install.packages('digest')

utils::install.packages(pkgs = IRkernel, repos = NULL)
IRkernel::installspec()

