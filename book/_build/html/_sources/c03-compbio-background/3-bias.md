(compbio-bias)=
## Sources of bias in computational biology datasets

### Why we care
#### We want to trust science
[//]: # (TODO: Restructure this section so that the different sources of bias are in a sensible order and that I have proof for each. Rename "why we care" and "we want to trust science")

```{epigraph}
The imposing edifice of science provides a challenging view of what can be achieved by the accumulation of many small efforts in a steady objective and dedicated search for truth.

-- Charles H. Townes
```

[//]: # (TODO: Rewrite this so that the vibe is more "hey we all agree that we want to be able to rely on science and less "FUCK ALL OF YOU")

We want to trust the results of scientific research. Not only when it’s our own (because it’s fun and exciting to look for and find the truth), but because scientific research is generally paid for by tax, and the results that are generated by it drive policy, drug treatments, and innovations. 

In all fields, science is a search for the truth. And in all fields, there are concerns about what makes bad, unreliable, un-useful, or biased research; what must be done or not done to uphold science’s claim to truth, or at least reliability. Computational biology has a number of unique characteristics which make these questions worth discussing in its specific context. 

[//]: # (TODO: REf the "earlier" below:)
As mentioned earlier, in contrast to other fields, many bioinformatics datasets have been freely available and accessible on the internet since its inception. Computational biology might be a good place to look for what is required to really benefit from those open datasets, what can be gained from them (and what can’t), and what the next steps in reproducibility should be, beyond making data accessible.c

Secondly, the creation of these databases has birthed a lot of research that is highly reliant on a handful of large ontologies and databases, the completeness of which is unknown, and the cataloging process by which they are added to is extremely uneven. 

Thirdly, many of the new publications in this field showcase novel software and models which build on these resources, despite the fact that much of it is difficult to validate due to the lack of gold standard datasets. 

When scientific results are often based on statistics, it’s inevitable that some proportion of published scientific results will not be true. This isn’t a problem, as over time, researchers can double-check interesting scientific results, and the literature can be updated to reflect that. This is sciences self-correcting mechanism. If a result can be replicated in a different circumstance by a different person, it reinforces the likelihood that the result is true. A replication doesn’t have to reveal the exact same level of statistical significance  or effect size to be successful, but (usually, depending on definitions) just a similar result.

#### The reproducibility crisis 

```{epigraph}
In science consensus is irrelevant. What is relevant is reproducible results.

-- Michael Crichton
```

The reproducibility crisis is the realisation that worryingly large proportions of research results do not reproduce. Replication studies have found that only 11% of cancer research findings{cite}`Begley2012-oc`, 20-25% of drug-target findings{cite}`Begley2012-oc,Prinz2011-rh`, and 39% of psychology findings{cite}`Open_Science_Collaboration2015-vi` reproduced. Surveys of researchers across disciplines reveal that more than 70% of scientists say they have failed to reproduce another paper’s result, and over 50% say they have failed to reproduce their own results{cite}`Baker2016-tb`. It seems that science’s self-correcting mechanism is not working as intended.

This shocking irreproducibility is thought to be due to a multitude of factors, including poor data management, lack of available materials/details of experiments, publication bias, poor statistical knowledge, and questionable research practices{cite}`Bishop2019-hg`. 

[//]: # (TODO: Any time I explain any of this, I better be able to say WHY it's there: Go through and check that I can)

##### Null Hypothesis Significance Testing

```{epigraph}
Statistical significance is the least interesting thing about the results. You should describe the results in terms of measures of magnitude –not just, does a treatment affect people, but how much does it affect them.

-- Gene V. Glass
```

[//]: # (TODO: Check maths appears correctly and none missing)

Null Hypothesis Significance Testing (NHST) is the most popular method by which scientific hypotheses are tested and reported. This reporting usually consists mostly of a p-value, a measure of statistical significance: the likelihood that a false positive could be obtained just by chance. In other words p-values are a measure of type 1 error (false positives). The threshold for this, usually denoted by $\alpha$ is most often set to 0.05, as recommended by Fischer, however there have been many debates about whether this is the most sensible cut-off for science today. Despite the dominance of p-values as main or only reported statistic across scientific fields, they do not imply that a result is interesting (the effect might be small or the hypothesis uninteresting), or even that it’s likely to be true. Sometimes the p-value is not even reported, but only whether or not it crossed the p<0.05 threshold.

Two other useful quantities of NHST are effect size and statistical power. Effect size is the magnitude of the effect found by the statistical test. A very small effect can only be detected with a large enough sample size. Statistical power is a measure related to the type 2 error (false negatives), it is $1-\beta$ where $\beta$ is the false positive rate. A statistical power of 80% is customary, where it is calculated, in which case there is a 20% chance that a result is a false negative if the null hypothesis is accepted. A very highly powered test with a high (non-significant) p-value represents strong evidence that the null hypothesis is true, although it may often be reported as “failing to reach significance”. Low-powered tests, coinciding with low sample sizes, mean that both the acceptance or rejection of the null hypothesis is likely to be unreliable. 

[//]: # (TODO: Check math below and formatting.)
[//]: # (TODO: Add link to dance of the p-values)
P-values do not have a high prediction value for reproducibility, since they have a high spread, even when a test is reasonably highly powered. Statistician Geoff Cumming refers to this as the “dance of the p-values”. Instead, a measure of the expected truth of a finding can be estimated from the proportion of hypotheses that are true in a given field, the statistical power, the p-value threshold as:

$$
ppv=\frac{(1-\beta)p_{true}}{p_{true}(1-\beta-\alpha)+\alpha}
$$

Where $ppv$ stands for positive predictive value and $p_{true}$ is the proportion of true hypotheses in a field{cite}`Ioannidis2005-mo`. 

For this version of the formula (there is also a version that includes bias, which was instrumental in the Ionnaidis’ claim that “most published research findings are false”{cite}`Ioannidis2005-mo`), and standard choices for power and statistical significance of $\alpha=0.05$ and $\beta=0.2$, we would expect more findings to false than true if $p_{true}<0.0588$ (3.s.f). That might seem like a small number, but in some bioinformatics experiments, we hypothesise that millions of SNPs may be responsible for a trait, when only small numbers are. On the other hand, if half of researchers hypotheses were correct for a given field ($p_{true}=0.5$), the formula would yield $ppv=0.941$ (3.s.f.), but the low reproducibility of GWAS results, gene annotations, etc, implies that the proportion of true hypotheses is less than this.

The same approach can be used to calculate the limit for $p_{true}$ for which we’d expect there to be more false positives than false negatives. Using the same values for and  and , we get $p_{true}=0.2$, i.e. if less than 20% of hypotheses are true, then we are more likely to get false positives than false negatives. This is interesting as most published scientific results are claiming a positive result, so we are essentially erring on the side of publishing erroneous errors.

[//]: # (TODO: Instert image and fix reference and citations/links)

```{figure} ../images/p_hacking.png
---
height: 220px
name: p_hacking
---
Images that are illustrative of researchers approaches to p-values and p-hacking. The left image is [a popular tweet](https://twitter.com/FaustoBustos/status/1103435523777978368), while the right image is [an xkcd comic](https://xkcd.com/1478/)).
```

In addition to poor reporting and underpowered tests, the pressure on scientists to publish means that researchers may be tempted to (or may accidentally, due to statistical ignorance) employ data-mining tactics in order to harvest significant p-values. This practice is known as “p-hacking”, and evidence for its existence can be found in distributions of p-values in scientific literature{cite}`Head2015-ns`, as well as popular culture ({numref}`p_hacking`). This can include rerunning analysis with different models/covariates, collecting data until a significant p-value is reached, or performing 20 experiments and only publishing the results of one. 

```{epigraph}
The first principle is that you must not fool yourself – and you are the easiest person to fool. 
-- Richard Feynman 
```

[//]: # (TODO: Aside about how Fischer is the worst)
There are several suggested tonics to the problem of uninformative and ubiquitous p-values. Reporting p-values as numbers rather than in relation to a threshold (e.g. p<0.05) is starting point. Information about statistical power and effect size should also be provided. In addition to giving researchers reading a paper a better idea of the quality of it, this also allows science to self-correct a little easier, since individual p-values can then be combined into more reliable p-values, using for example Fischer’s method{cite}`Fisher1990-ro`. 

A more interesting solution is pre-registration, as used in clinical trials. This involves a detailed publication in advance of the analysis protocols that will be used in order to prevent tweaking analysis based on seeing the data. This solves p-hacking related problems, and makes a distinction between hypothesis-generating and hypothesis-testing research.

For cases where many hypotheses are being generated at once (for example in GWAS), multiple hypothesis corrections (e.g. the Bonferroni correction{cite}`Dunn1958-sj` or the False Discovery Rate{cite}`Benjamini1995-me`) can be employed to adjust the p-value to account for this.

##### Publication bias
[//]: # (TODO: Check where else Barbaric2007-zm is cited)
Although with current standard p-value and power cut-offs, negative results are more likely to be true than positive ones, negative results are much harder to publish. This bias is likely to be responsible for the draw of questionable research practices like p-hacking. It also means that there is a lot of unpublished, negative results which are likely to be repeated, since there is no way that someone could know it has already been done. A highly powered negative result could be very interesting, for example, we know hardly anything about which genes do not appear to affect phenotypes, since these results are not published{cite}`Barbaric2007-zm`, but they would help enormously with the challenge of creating a gold standard dataset for gene function prediction.

Registered reports are an attempt to remove these problems associated with publication bias, by linking the concept of pre-registration with that of publishing. Essentially, authors submit their introduction and methods section to a journal and at this point they undergo peer review and the journal agrees to publish the results, regardless of the result. At the time of writing over 170 journals were accepting registered reports and the number has been growing in recent months, across disciplines, although they are currently most popular in psychology and neuroscience{cite}`Hardwicke_undated-jj`. This solution also offers peer-review at a more helpful stage in the manuscript, when it’s still possible to make changes to the experiment.

#### Reproducibility in bioinformatics
In a field that has long had a huge number of open data repositories, and a relatively high level of statistical knowledge among researchers, in some ways bioinformatics might be expected to be ahead of the curve in terms of reproducible research. It certainly seems that as a field, it excelling at open research. At the same time, however, it is even more important for the work to be reproducible if data and software are being reused by multiple researchers.

The Gene Ontology Annotations (GOA) are a combination of experimental and computational annotations. While the supporting publications for the experimental annotations are available, the GO consortium do not provide the statistical evidence that they used alongside this (e.g. p-value, effect size), etc. 

[//]: # (TODO: Delete the when is a model useful section if I don't have any thoughts about it:)

#### When is a model useful? 
```{epigraph}
All models are wrong, but some are useful

-- George Box
```

Models are most useful to us when they generate testable hypotheses about the underlying mechanisms of a process. In this way, they can help to advance science. They can also be useful to us if they generate predictions for forecasts. These predictions can be tested, which helps us to improve the model, and if they are accurate, they can also help us to generate hypotheses, or they may be useful in and of themselves. 


(pqi)=
##### PQI
[//]: # (TODO: Check this is in a reasonable position and has the right level of headings.)
[//]: # (TODO: Explain that it is about where there is also proteins/proteomes)

The Proteome Quality Index (PQI) is an attempt to provide quality metrics about completed genome sequences. It was a group effort, which resulted in a paper{cite}`Zaucha2015-ez`, of which I am an author, as well as [an associated website (http://pqi-list.org/)](http://pqi-list.org/). I contributed to discussions about metrics, and paper editing.

The motivation for creating the index came from problems of reproducibility in the field of genomics. In creating a daily-updated tree of life (sTOL, sequenced Tree Of Life), it was found that many sequenced genomes were missing vital proteins due to poor sequencing{cite}`Fang2013-et`. Such genomes are reused by many researchers, for example in comparative genomics, and omissions of whole proteins and poor accuracy of others are likely to affect research results. 

The PQI website was intended to be both a way for users of past genomes to look up the quality of a genome in advance of some research and, more importantly as a talking point for quality guidelines for genomes/proteomes. While quality control and data submission guidelines were more developed in other areas of computational biology, similar guidelines for genome quality were lacking.

###### PQI features 

The PQI website provides a scoring system for proteomes, bringing together numerous different metrics which are normalised before being averaged into an intuitive star-rating (1-5 stars) with equal weight given to each metric. Proteomes can be searched for, filtered by the various ratings, downloaded, user-rated and commented on. Additional proteomes and metrics can be added/suggested by users via the website and documentation describing this is provided.

###### The original PQI metrics

[//]: # (TODO: Check how this paragraph ended in Google Doc. Had weird punctuation.)

PQI originally provided 11 measures of proteome quality, that are either local i.e. “clade-based” (in which proteomes are compared to similar organisms) or global (in which case it is compared to all other proteomes). A clade is a group of organisms that consists of a common ancestor and all its descendants, i.e. is a branch on the tree of life{cite}`Cracraft2004-ud`, so an appropriate ancestor must be chosen to define the clade. For PQI, since the purpose of these clades was to compare its’ constituent proteomes, we wanted clades that had similar variability. This was achieved by choosing parent nodes that are at least 0.01 in branch length away from the proteome (leaf node), and such that the clade contains at least 10 species. Trees and branch lengths to carry out these calculations were taken from sToL{cite}`Fang2013-et`. For clade-based metrics, proteomes score well if they have similar scores to the rest of the clade.

[//]: # (TODO: Check combination homology 3 and 4 from table below)

```{list-table} Description of the quality metrics in PQI
:header-rows: 1
:name: pqi-table

* - Metric name
  - Type
  - Description
  - Notes
* - 1\. Percentage X-content
  - Global
  - Percentage of proteome with amino acids denoted by ‘X’, excluding the first residue of each protein.
  - Amino acids that cannot be identified, or can have more than one value are represented by an ‘X’ in the amino acid sequence[139]. This occurs when coverage of the sequencing is low. Uncertainty in translation start sites mean the first residue of a protein is often uncertain (‘X’) even in the highest quality proteomes, so these are excluded from this measurement.
* - 2\. PubMed Publication Count
  - Global
  - The total number of publications related to the genome as listed for that entry in the PubMed database[140].
  - This is a measure of how well-studied a proteome is, assuming that proteomes that have been studied more will be of higher quality. 
* - 3\. CEG Domain
  - Global
  - Proportion of CEG set which contains homologous domains in the proteome, according to SUPERFAMILY
  - This method assumes that all eukaryotic genomes should contain a core set of well-conserved of eukaryotic genes. This score is not calculated for non-eukaryotes. This was done using the Core Eukaryotic Gene (CEG) library used by the CEGMA tool[141], which comes from the Eukaryotic Orthologous Group (KOG) sequence orthology database[142]. Domain-architecture similarity is calculated using the SUPERFAMILY HMM library.
* - 4\. Combination Homology
  - ???
  - ???
  - ???
* - 5\. Percentage of sequences in Uniprot
  - Global
  - Percentage of proteome sequences that appear in Uniprot with 100% sequence identity
  - This metric assumes that the majority of discrepancies between Uniprot protein sequences and the proteome protein sequences are due to proteome inaccuracies.
* - 6\. Number of domain superfamilies
  - Clade-based
  - Number of proteins assigned to domain superfamilies by SUPERFAMILY compared to average for clade.
  - Assignment to domain superfamilies was obtained using the SUPERFAMILY HMM Library. The number of superfamilies gives an indication of the diversity of the proteome, so a low number compared to the clade may indicate an incomplete proteome, while a high number could indicate that the proteome contains domain superfamiles that it shouldn’t. 
* - 7\. Percentage of sequence covered
  - Clade-based
  - Percentage of amino acid residues in proteome sequence that are covered by SCOP domain superfamily assignments, compared to the average for the clade. 
  - This metric measures the portion of structured protein sequences found in the proteome as opposed to disordered regions and gaps. This measure assumes related species have a similar breakdown of these types of proteins. A mismatch could indicate that the parts of the genome that are supposed to be protein-coding are an incorrect length, that it is missing proteins, or contains proteins that it shouldn’t.
* - 8\. Percentage of sequences with assignment
  - Clade-based
  - Percentage of amino acid residues in proteome that have SCOP superfamily assignment according to SUPERFAMILY, compared to the average for the clade.
  - Related species are assumed to have a similar percentage of domains with SUPERFAMILY assignments to SCOP superfamilies
* - 9\. Mean sequence length
  - Clade-based
  - The average length of proteins in the proteome (in amino acids), compared to the average for the clade.
  - This measure assumes that mean sequence length of proteins should be comparable with those of related species. 
* - 10\. Mean hit length
  - Clade-based
  - Average number of amino acids in superfamily assignments, compared to the average for the clade.
  - Longer hits represent better matches to SCOP domains. These are assumed to be similar for similar species.
* - 11\. Number of domain families
  - Clade-based
  - Number of distinct SCOP protein domain families that are annotated to the proteome, compared to the average for the clade.
  - The SCOP protein domain families are annotated to the proteome using a hybrid HMM/pairwise similarity method from the SUPERFAMILY resource. Similarly to the number of domain superfamilies, the number of families gives an indication of the diversity of the proteome at the SCOP family level. Domain families were included in addition to domain superfamilies, since they are more specific and may reveal differences that are not apparent at the superfamily level. 
* - 12\. Number of domain architectures
  - Clade-based
  - Number of unique domain architectures (combinations of SCOP domain superfamilies and gaps) in the proteome, according to SUPERFAMILY, compared to the average for the clade.
  - Similarly to the number of domain families superfamilies, the number of domain architectures gives an indication of the diversity of the proteome at the SCOP family level.
```

[//]: # (TODO: Format table caption better:)

{numref}`pqi-table` shows the original PQI metrics. 

As a proteome will get low scores in clade-based metrics when they are unusual compared to the rest of its clade, model organisms (e.g. Homo Sapiens) can get a low score in clade-based metrics since for the wrong reasons - since they are of such higher quality compared to those in it’s clade. The PQI website’s comment and user-rating features can be used to alert its users to these cases.

Since the publication of the PQI paper, the DOGMA metric{cite}`Dohmen2016-iv`, which scores proteomes based on conserved arrangements of protein domains, has been added to the PQI website. 

###### Potential improvements
The mapping from raw score to star rating for some metrics could be improved. For example, homo sapiens has ‘0’ X-content (the lowest/best possible value), but 4.1 stars.

[//]: # (TODO: Rephrase)
PQI was created with the potential to add further quality metrics by other researchers. Although the DOGMA metric was added and it is based on BUSCO{cite}`Simao2015-gc`, it might be sensible to add BUSCO, since it has become very popular, and any proteome/genome quality index would probably be seen as incomplete without it. The continued inclusion of the CEG Domain Combination Homology metric may be questioned since CEGMA is no longer being updated (nor is the KEG database upon which it is based), but BUSCO and CEGMA may be complementary since BUSCO has a weaker requirement for inclusion in the set of proteins, which means that it has more proteins, and vice versa.

To impact on the problem for model organisms for clade-based metrics, one solution would be to treat model-organisms differently in these circumstances, for example score clades containing model organisms against the model organism. An more subtle alternative to this would be using the NCBI’s Assembly database{cite}`Kitts2016-eo`, which has been released since PQI was published. The database tracks how many assemblies there are for each species as well as how many versions of each assembly there has been. This information could be used to weight the importance of proteomes in clade-based metrics. The number of assemblies and versions could also form a separate score.

Sequencing depth (coverage) and read length are also known markers of genome quality{cite}`Sims2014-df`. Average coverage for an assembly (except reference genomes) is also available in the NCBI Assembly database{cite}`Kitts2016-eo`. 

Some “third-generation” sequencing technologies create much longer read lengths, but potentially lower accuracies. A third category of metrics “technology-based” metrics could exist for proteomes where the metric is only really comparable within similar types of technologies. If technology-based metrics were implemented, it may also be sensible to have some metrics which only exist for specific technologies. For example, for nanopore sequencing, we could implement an indel-based quality metric{cite}`Watson2019-pz`. Including sequencing-technology-specific metrics may encourage contributions from other researchers who specialise in particular technologies. Sequencing technology is also available in the NCBI Assembly database{cite}`Kitts2016-eo`. 

The development of additional measures is required to deal with other potential problems in genome sequencing, for example GC content, amino acid bias, or contamination from other genomes. 

---
**Chapter References**

```{bibliography} /_bibliography/references.bib
:filter: docname in docnames
:style: unsrt
```