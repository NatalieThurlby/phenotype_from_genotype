(alspac-intro)=
# Testing Snowflake on ALSPAC data

(alspac-motivation)=
## Motivation
[//]: # (TODO: Write - to test Snowflake)
In order to test Snowflake, I needed a data set that had a wealth of phenotype and genotype information.

(alspac-study)=
## The ALSPAC cohort study
The Avon Longitudinal Study of Parents and Children, ALSPAC{cite}`Golding2001-oj` is a cohort of over 14,000 families from the Avon area with children born in 1991-1992. 
It is also known as "the Children of the 90s" study.
Many of these families continue to be part of the study to this day, including some of their own children through an extension of the project: children of the children of the 90s (COCO90s).

A wealth of phenotype information (over 80,000 variables) has been collected from these families over the years, through a series of voluntary surveys and clinics, including genotyping of over 9000 children using 23andMe.

[//]: # (TODO: Explain the contents of the ALSPAC catalogue)
ALSPAC's phenotype information, while extensive, is not mapped to phenotype terms in ontologies. 
All data held by ALSPAC can be searched for in the [ALSPAC variable catalogue](http://www.bristol.ac.uk/alspac/researchers/our-data/), after which it can then requested per variable or data type. 
At the time of writing, the cohort is around 30 years old, meaning that there is little information about phenotypes that manifest later in life, for example Alzheimer's or heart disease.
Many phenotype terms may not have any measurements, and there may be many variables associated with some others.

(alspac-exp-design)=
## Experiment Design
Due to the identifiable nature of the data, our ethics application did not allow us to access many different phenotypes to perform a cross-phenotype validation of the predictor. 
Instead, we were granted access to all of the genotype data only first, then allowed to request a small number of phenotypes of interest after running Snowflake.

[//]: # (TODO: ALSPAC could be run for ALSPAC only since there is no ethnic diversity within the ALSPAC genotypes - it was specifically restricted to europeans - https://academic.oup.com/ije/article/47/4/1207/5001767)

(choosing-phenotypes)=
### Choosing test phenotypes 
I created a shortlist of phenotypes of interest by first restricting the set of scores to phenotypes for which Snowflake makes a prediction within the ALSPAC cohort, then ordering this list by the {ref}`phenotype confidence score<phenotype-score>`, to ensure that Snowflake could give confident predictions for phenotypes that were requested.
I then mapped these to ALSPAC phenotypes by searching the ALSPAC variable catalogue.
This resulted in the four : `MP:0001501` *Abnormal Sleep Pattern* (measured using `FJCI250` *Sleep symptom score*), `MP:0001933` *Abnormal litter size* (measured by `mz010a` *Pregnancy size*), `MESH:D001259` *Ataxia* (measured by `kw2030` *Child ever thought to have a problem with clumsiness/coordination*), and `HP:0001249` *Intelligence/intellectual disability* (measured by `f8ws150` *Child had special needs*). 

(alspac-discussion)=
## Results

### Phenotype prediction
Unfortunately, the results of phenotype prediction with Snowflake on ALSPAC data show that snowflake cannot currently be used to accurately predict the following phenotypes in the ALSPAC cohort: `MP:0001501` *Abnormal Sleep Pattern* (measured using `FJCI250` *Sleep symptom score*), `MP:0001933` *Abnormal litter size* (measured by `mz010a` *Pregnancy size*), `MESH:D001259` *Ataxia* (measured by `kw2030` *Child ever thought to have a problem with clumsiness/coordination*), and `HP:0001249` *Intelligence/intellectual disability* (measured by `f8ws150` *Child had special needs*). 
These were assessed by bootstrapping the $F_{max}$ scores for each phenotype, which gave very low f_max scores (<0.1) and p>0.05 for each phenotype.

Meanwhile other top-scoring phenotypes could not be tested since they did not map well to available ALSPAC phenotypes, e.g. `HP:0007703` *Abnormality of retinal pigmentation* and `HP:0001120` *abnormal corneal size*.

### Variant function 
In addition to testing the test phenotypes, it's possible to look at highest-scoring SNPs (i.e. variants present in people with the highest snowflake "phenotype score") for all phenotypes (even those we did not have phenotype data for).
In this way snowflake can be used as a kind of variant prioritisation tool.

These showed some reassuring results:
- **1. Rediscovering known SNPs**: The highest-scoring phenotype in the ALSPAC study was *Abnormal fat cell morphology*. It's highest scoring SNP `rs6659176` is known (via GWAS) to be associated with obesity{cite}`kring2008genotype`.
- **2. making plausible cross-species variant function predictions:** One SNP, `rs2287780`, was predicted to be responsible for the phenotype of abnormal fetal growth. It is listed in SNPedia{cite}`cariaso2012snpedia` as being linked with vitamin B12 and folate production, which are well-known to be important for
fetal development. This SNP was flagged up by an ontology term associated with mouse genetics (“abnormal litter size”), meaning it is possible to find candidate human SNP/phenotype associations using information about other species.
- **3. making plausible multi-SNP trait predictions** a combination of 2 SNPs is required for the phenotype (ataxia – a disfunction of the central nervous system) to be predicted. One predicted (`rs13436090`) has been associated with autosomal dominant cerebellar ataxia (ADCA){cite}`yoshida2009severity`. The second SNP (`rs2269961`) is a new candidate SNP, a protein from which (Tocopherol-associated protein 2) is thought to be responsible for transporting vitamin E (a deficiency of which can cause spinocerebellar ataxia{cite}`brigelius1999vitamin`).

## Discussion 
(alspac-phenotype-problems)=

Snowlflake's phenotype prediction results were disappointing but could have a number of possible interpretations.

### Selection of phenotypes
For valid ethical reasons, it was only possible to request a small number of phenotypes from ALSPAC.
Snowflake isn't expected to work for all phenotypes, since we know there are many other mechanisms (some not even genetic) behind phenotype besides only the disruption of proteins through missense SNPs in protein-coding genes.
The fact that Snowflake was not successful in predicting any of the requested phenotypes could be an indication that none of these phenotypes has this mechanism behind it.
Alternatively, it could be an indication that Snowflake is not a successful method for predicting phenotypes even in these cases, and there are many reasons why that could be the case since Snowflake relies on a lot of other pieces of research and software to function. 

In selecting phenotypes, I chose phenotypes where (1) Snowflake was expected to make a {ref}`confident<phenotype-score>` prediction and (2) ALSPAC data could be used to validate this prediction. 
These two restrictions narrowed down the phenotypes considerably and the majority of the top-predicted phenotype terms (Abnormal Fat Cell Morphology, Abnormal Fetal Development) did not map cleanly to ALSPAC phenotypes.

Since I chose phenotypes primarily by looking at the distribution of scores for Snowflake, our lack of promising results could also be an indication that the phenotype-score (finding interesting distributions of phenotypes) is unsuccessful.

[//]: # (TODO: Aside missing heritability)
A more interesting test of Snowflake's abilities might be to choose phenotypes with high heritability, and specifically high missing heritability.

I also regret not considering the ethical implications of the choices of phenotypes to predict. 

[//]: # (TODO: discuss the heritability of the requested phenotypes)

(alspac-overlap-problem)=
### Overlap between training and validation data
ALSPAC is a popular cohort study for use in GWAS analyses.
As such, many links between genotype loci and phenotypes have been published from this data set, for example loci associated with birthweight{cite}`Horikoshi2013-la`, asthma and allergies{cite}`Hinds2013-gi`, autism spectrum disorders{cite}`Robinson2016-pj`, problematic peer relationships{cite}`St_Pourcain2015-be`, and lung function{cite}`Repapi2010-vx`.
This data informs GOA genotype-phenotype annotations, and through dcGO this data could already be present in Snowflake, meaning that there may be in some sense, overlap between the training and validation data, which could overestimate the accuracy of the predictor on unseen data{cite}`Wray2013-nl`.

For this reason, I do not think that it is sensible to try any further to use ALSPAC to validate or test Snowflake.



