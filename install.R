# Install specific version of IRkernel that works with our specific version of R
package = "https://cran.r-project.org/package=IRkernel&version=1.1.1"
utils::install.packages(pkgs = package, repos = NULL)
IRkernel::installspec()

