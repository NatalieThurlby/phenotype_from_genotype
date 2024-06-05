# Install specific version of IRkernel that works with our specific version of R
package = "https://cran.r-project.org/package=IRkernel&version=1.0.2"
install.packages(pkgs = package)
IRkernel::installspec()

