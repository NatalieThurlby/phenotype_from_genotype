## Batch correction

### What are batch effects?
<!--TODO: What are batch effects: borrow from relevant part of thesis-->

### Batch-effect removal methodologies
There are a number of batch correction analyses which attempt to remove batch effects from RNA-seq data. Batch correction can be very useful for understanding baseline gene expression, but can lead to inflated p-values for downstream analysis (notably for differential gene expression, using ComBat{cite}`Johnson2007-zh`), where a more sensible approach is to include batch as a confounder for statistical tests. 

#### Surrogate Variable Analysis
Surrogate Variable Analysis (SVA){cite}`Leek2007-ba` is used in cases where you do not have a covariate that drives batch effect (i.e. you do not have information about processing date, technicians, processing centres, etc), but you expect that batch effects will be present. SVA estimates which samples belong to which batches, before using ComBat to remove the effect due to those batches.

#### ComBat
ComBat{cite}`Johnson2007-zh` is a popular batch effect removal procedure, which was first developed for use with microarray data, but continues to be a popular choice for RNA-seq data. Generally, it is a well-trusted method for both of these types of gene expression data{cite}`Chen2011-ke`, but more recently has been shown to “over-correct” batches for RNA-seq data{cite}`Liu2016-wa`.

ComBat is an Empirical Bayes method, meaning that the prior distribution is estimated from the data. It is designed to “borrow/share information” between genes in order to get a better estimate of batch effects, and assumes that batch effects affect many genes in similar ways. 

### Pre-batch-corrected data
Visual inspection of {numref}`combine-pca-before` shows that data appears to cluster by experiment more strongly than by tissue group, meaning that batch correction is necessary to compare across experiment samples.

# Code to create combine-pca-before

### Method
<!--TODO: write method overview, e.g. simulate data, and apply batch correction to show it would work on this kind of thing, then apply it to our actual data-->

#### Simulating tissue-specific gene expression count data with batch effects
Simulated data can be used to test that methodologies are applicable to new data types. Since simulated data has a well-defined ground truth, we can test the performance and accuracy of a methodology using it. If the real data is similar to the simulated data, we can assume that methodologies will perform similarly on the real data.

Data can be simulated based on its expected distribution. For gene expression data, a negative binomial distribution is chosen to represent the underlying gene expression counts because the distribution is always positive, and does not assume mean and variance are equal. The parameters for the simulated distribution for each gene can be chosen based on estimates from existing data sets. This allows for any number of samples to be simulated. Additional effects (e.g. noise) can be added to this base level of gene expression and pre-decided fold changes for differences between samples (e.g. differential expression of tissue-specific genes, or batch effects) can be achieved by multiplying the simulated data. 

In order to test whether ComBat can be used to deal with combining the experiments chosen (considering the unbalanced design), a simulated data set of tissue-specific batch-affected gene expression data was created. In order to do this, decisions had to be made about the scale and distribution of the batch effect and tissue-specific effects. These were estimated from a subset of the FANTOM5 and GTEx datasets.

##### Measures of tissue specificity
The expected fold-change due to tissue-specific effects must be pre-decided in order to simulate the dataset. The size of the effect and number genes affected were estimated using data from the Human Protein Atlas (available at https://www.proteinatlas.org/download/proteinatlas.tsv.zip), which contains for each tissue-specific gene, the transcripts per million (TPM) for tissues that were found to be tissue-enriched (at least a 5 fold change, compared to all other tissues), group-enriched (at least a 5 fold change between the group of 2-7 tissues compared to all other tissues) or tissue enhanced (at least a 5 fold change between the tissue and the average of all other tissues), and the transcripts per million of the most highly expressed tissues that were not. Taken together (tissue-enriched, group-enriched and tissue-enhanced), we here refer to these genes/tissues as tissue-specific.

# Code to make: The HPA data and data simulated by a log-normal fitted to the data, for both the distribution of tissue-specific fold-change over all tissue-specific gene-sample pairs (left) and the number of tissue-specific genes per tissue over the 37 HPA tissues (right)

For any of these tissue-specific genes/tissues, the fold change per tissue per gene was calculated. The distribution of fold changes was compared to an exponential, log-normal and power-law distribution using the python `powerlaw` package. The log-normal distribution was the best fit ($D=0.11$), and the parameters fitting the fold changes to the log-normal distribution were estimated as $\mu=1.57, \sigma=1.66$. Visually inspecting the graph reveals that the data simulated from these parameters appears to fit the data well (orange line, left-hand plot, {numref}`dist-tissue-specific`).

The number of genes that were found to be in some sense tissue-specific was also extracted from the HPA data, and compared to log-normal, exponential and power-law distributions. Again, the log-normal distribution fitted best ($D=0.10$). It was parameterised by $\mu=5.44, \sigma=0.70$. The small number of tissues (37) makes it hard to assess the accuracy of this fit, but visual inspection of the graph (orange line, right-hand plot, {numref}`dist-tissue-specific`) reveals it to be reasonable.

##### Simulation Method
The `polyester` R package{cite}`Frazee2015-kg` was used to simulate RNA-seq count data with the same design of tissues, samples, and experiments as in the combined data set. To make the data set more manageable, the data set was simulated for 1000 genes. The `create_read_numbers` function is used to simulate base reads based on the FANTOM5 data set, and add tissue-specific effects (as calculated earlier) and batch effects. 

The simulated data set is $Y_{ijk}\propto Negative Binomal (mean=\mu_{jk},size=r_{jk})$ for replicate $i$, gene $j$, and sample $k$. The means are given by $\mu_{jk}=\mu'_j+\lambda+{jk} \cdot mod$ where $\mu'_j$ are the estimated base means per gene, $\lambda_{jk}$ are the generated log-fold changes in matrix format, including both batch and tissue effects (`coeffs_batch.csv`), and $mod$ is the model design matrix. The dispersion parameter (size), $r_{jk}$ is calculated based on $\mu_{jk}$ and the fit between mean and size (estimated from the FANTOM5 data).

In order to do this, the FANTOM5 data was cleaned to contain only the set of genes present in all experiments (`common_genes.csv`) and `NaN` values for expression counts were set to 0. This data was then used as input to polyester to parameterize the negative binomial distributions for the simulated base expression counts. Parameters calculated by polyester include means per gene and size, and probability of a zero count per gene. 

Tissue effects were calculated as previously described, and included in the coefficient matrix.  Batch effects were assumed to affect 50% of the 1000 simulated genes. In all cases, each affected gene all had a log-fold change randomly generated normally distributed ($\mu=0,\sigma=1$) effect due to batch, which was persistent across samples.

##### Limitations
A good indication of the size or extent of batch effects was not readily available. Batch effects (log-fold changes - and proportion of genes affected by them) were chosen such that the simulated distributions most closely (according to visual inspection of PCA and box-plots).

The simulated data set is read counts and the fold changes are calculated from TPM data, however the simulated data does not include effects due to gene length or library size.

---
**Page References**

```{bibliography} /_bibliography/references.bib
:filter: docname in docnames
:style: unsrt

```{code-cell} ipython3

```