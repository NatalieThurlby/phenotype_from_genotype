## Summary
[//]: # (TODO: Rewrite this section so that it is just a summary of the different sources of error AND a summary of the different excitingt types of data. BUT NOT downbeat/dramatic e.g. no wonder it doesn't work.)
[//]: # (TODO: Citations in summary section)
[//]: # (TODO: Decide how to spell multiomics)

The purpose of this introductory chapter was to provide an overview of how we think phenotype arises from genotype. It’s also to explain why it’s a hard problem! 

To summarise, there are multiple kinds of genetic variation, and even the simplest (the SNP) can exist on multiple parts of the genome, and may or may not affect structure or function of transcribed proteins. Even if the SNP is in a coding region, and is non-synonymous (affects protein structure), it may fall in a disordered region of a protein (leaving us without structural information), we may not know where that protein is transcribed, or it may affect the transcription of multiple different proteins. Furthermore, the SNP may affect phenotype differently with homozygous or heterozygous calls, and the protein may affect phenotype by influencing a network of other proteins, or the protein may exist as a redundant part of a pathway which will only affect phenotype if three other SNPs have specific calls. Even after all this, the presentation of many phenotype depends heavily on the environment.

Given all this complexity, it may seem no wonder that phenotype prediction is currently inaccurate{cite}`Zhou2019-jk`. However, diverse information about biological entities exists, for example gene and protein sequence, protein structure, variant frequencies and functions, and gene expression. Multi-omics approaches that combine these data types have been successful at elucidating mechanisms behind certain phenotypes{cite}`Hasin2017-tk,Ritchie2015-ds,Kristensen2014-iw`. There is now the opportunity for genome-wide phenotype predictions to do the same. Obtaining an accurate prediction of phenotype and protein function, even for a subclass of variants/proteins, has the potential to greatly impact people. A method which predicts phenotype directly from the molecular biology would be desirable as it would create a model for how phenotype emerges from genotype, in addition to predictions for important genes.

---
**Chapter References**

```{bibliography} /_bibliography/references.bib
:filter: docname in docnames
:style: unsrt
```