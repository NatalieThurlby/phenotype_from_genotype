---
title: Corrections replies
marimo-version: 0.10.13
---

```{.python.marimo}
import marimo as mo
```

# Corrections responses

## Abstract

> 1. Simplify line “In our cells, proteins are constantly being created and are degrading, and are accumulating or interacting to produce the phenotypes that we see at a larger scale: height, levels of enzymes in blood, diseases”

- [x] rephrased (see [abstract.md line 7 (old, red) -> lines 7 & 8 (new, green)](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-da12d85f6c4c27d6363bc8f1f9e1f4b2ebe700e89af44d55c2c23dbb9e681b2f))

> 2. Clarify “The versions of the proteins that it is possible for an organism to produce are determined primarily by its protein coding DNA, while the selection of possible proteins that are actively produced in each cell are determined by the environment of the particular cell at each time”

- [x] Rephrased (see [abstract.md line 8,9 (red) to lines 8, 9 & 10 (green)](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-da12d85f6c4c27d6363bc8f1f9e1f4b2ebe700e89af44d55c2c23dbb9e681b2f))

##  Chapter 2: How phenotype arises from genotype

## 2.1 Big questions

> 3. Move Section “2.1.2. The future computational biologists want” to later part 

- [x] Moved to 2.5 "Phenotype". [Was in `c02-biology-background/1-big-questions.md` lines 85-102](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-ef36a6223ff6c1f978fbb26807df41f02b5cb3b96dd74b650bffc2a2024b79cd) and [now in `c02-biology-background/5-phenotype.md` lines 66-82](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-706b5b938050c73a6a4a3472251bddc21af70f76fee904313f531abff070d5d8)

## 2.2 Biological molecules

> 4. In the fourth para below fig 2.3 “post‑transcriptional modifications such as splicing” please make the spacing between “post‑transcriptional modifications” and “such” prominent. Also add RNA editing and RNAi as modes of post-transcriptional regulations.

- [x] Fixed formatting
<!-- TODO: Check formatting in pdf -->
- [x] Added a paragraph for RNA editing and RNAi (see [`c02-biology-background/2-biological-molecules.md](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-91c018084b944733647b6e94d11f82d5940b80b1b3812115d44d03ab4fe5c288) lines 103-106)

> 5. In the section “2.2.1.3. “RNA makes Proteins”, a.k.a. Translation” it may be worth mentioning landmark work of Christian Anfinsen about how sequence of amino acid strings of protein acts as a “code” to precisely determine three-dimensional structure of the protein.

- [x] Included reference (this was an interesting read, thank you!) [lines 128-130](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-91c018084b944733647b6e94d11f82d5940b80b1b3812115d44d03ab4fe5c288) and rephrased sentence about protein folding [lines 162-163](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-91c018084b944733647b6e94d11f82d5940b80b1b3812115d44d03ab4fe5c288) , which may have previously come off a bit dismissive. 

> 6. In 2.2.1.4 “a different amino acid in a hormone protein could cause the protein to be expressed differently” could change it to “a different amino acid in a hormone protein could cause the protein to be expressed or function differently”

- [x] fixed - [line 179](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-91c018084b944733647b6e94d11f82d5940b80b1b3812115d44d03ab4fe5c288) 

> 7. In 2.3.2 “(protein‑coding nucleotides)” to “(protein‑coding part of DNA)”; there is repeating word: “in in”, please modify it.

- [x] fixed [line 24](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8d030ab9e7c40ffca168ed40ae78c0c47734bc20457e80589fd9dbe99964f3db)

### 2.3 A closer look at DNA

> 8. In 2.3.3.1. “A gene for X” what does “the same gene can make multiple different proteins” mean is not clear, does it mean different isoforms of the protein?

- [x] Yes isoforms - [edited (line 56)](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8d030ab9e7c40ffca168ed40ae78c0c47734bc20457e80589fd9dbe99964f3db) to clarify this and linked back to the earlier explanation of what isoforms are.

> 9. In 2.3.6.2 “However, synonymous SNVs could still have an effect on highlevel traits, since different nucleotides are translated at different speeds.” Here translation at different speed can have effect on both folding and abundance of protein (Kimchi-Sarfaty et al, 2007, Science) Please add few sentences along these lines.

- [x] Added this reference and some others about the affect on human health - [lines 152-155](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8d030ab9e7c40ffca168ed40ae78c0c47734bc20457e80589fd9dbe99964f3db)

### Misc

> 10. It is not clear at many place what is different proteins being referred that is encoded by the same gene? It means protein isoforms or something else?

- [x] Yes isoforms, I have tried to change this phrasing throughout to make this clear, e.g. [line 101](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-91c018084b944733647b6e94d11f82d5940b80b1b3812115d44d03ab4fe5c288), [line 53-54](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8d030ab9e7c40ffca168ed40ae78c0c47734bc20457e80589fd9dbe99964f3db), [line 11](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-08097eecc2b61eab5cfe30e0fba539fa84d256ac388416af299e20ae2634eb8d)

> 11. make the motivation for your work stronger

- [x] Did this more throughout, e.g. [line 19](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-08097eecc2b61eab5cfe30e0fba539fa84d256ac388416af299e20ae2634eb8d)/

> 12. in general, needs further references to relevant works

- [x] Added throughout (see [edits to bibliography](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-432f8fda6369eedbb05aa3069eca36a9836423f87c42b95de569a9ba012c32da)).

## Chapter 3: From Genotype to Phenotype: what is measured

### 3.2 from genotype to phenotype: what is measured

> 13. There seems to active and passive voice mix up please follow one mode at least within a chapter.

- [x] Fixed this in several places, [e.g. lines 5-6, 10-12](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55)

> 14 In 3.2.1.1 “Whole genomes for different organisms can be compared to one another to give us insight about the organisms, or within an organism, individuals can be compared to understand the importance of sections of DNA for that organism.” Not clear what the term plural organisms mean here?

- [x]  Clarified! ([lines 28-30](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55) was talking about comparative genomics. Have removed the word organism as I can see how that would be unclear if I meant species or individuals!)

> 15. In this section there should be a clear demarcation between whole genome assembly, gene annotation and then variants calling; there appears to be some mix up for me that impedes the smooth flow of information content.

- Assembly is described in `3.1.2`. Gene annotation is now described in an aside in in `3.2.1.3 Genes` ([lines 78-82](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55)). I moved the section about getting variant data from Whole Genome Sequencing from the GWS section to `3.2.1.4 Variant` ([lines 110-113](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55)) (I think this was the offending part).

> 16. Possibly mention about OMIM and HGMD databases

- [x] Added this to the end of 3.2.5 [line 275](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55)

> 17. 3.2.2.2 “Measures of mRNA abundance (i.e. gene expression data) are generally considered the best measures of translation (compared to protein abundance for example), and therefore the best data to tell us how DNA’s blueprints are being used in different scenarios” Appears to contrary to general belief that protein abundance are in general better measure. In situations where protein abundances are not easily measurable or trackable mRNA expression can be used as a good proxy for protein abundance. In fact your later aside “Gene Expression and Protein Abundance data” clearly reflects this.

- [x] Yes, this was a big mistake/miscommunication. I had confused popularity and quality, so I have been much, much clearer about this now, see [lines 144-146](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55).

> 18. 3.2.4. Phenotypes Please provide smooth link between this section to the next “connecting genotypes and phenotypes”.

- [x] Edited the end of one section and start of the other [lines 256-263](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-49c4f1ebf98422fe00d33a073c5a2dc1003ee13ee64142edb15624f26a4acc55).

### Misc

> 19. What is the link between 3.3 and 3.4 is it clear?

- [x] the computational methods (3.4) often use the ontologies and databases described in the previous sections (3.3 and previous). I've added [a sentence](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8c93eb1af6e5d1b25ddd80d382340750d494bdc918718ed18b46d4f1c3ed5fc4) to signpost this better at the start of 3.4.

> 20. Section 3.5 can be moved towards the end of the chapter before 3.7 summary

- [ ] I didn't do this because 3.5 (which mentions the different sources of bias in computational biology) motivates 3.6 (which introduces a project that I worked on - PQI - which aims to combat this). So I think it's already as late as it can be? 

> 21. Also in the summary it is foremost importance to highlight the core of the chapter genotypes and phenotypes, and linking them and related data sources. The description about bias, potential statistical pitfalls can be mentioned later.

- [x] Oh yeah, I see what you mean: the summary wasn't really a summary of the majority of the chapter - especially the opening line. I've [rewritten the section](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-bcf4d4e486b88b11d2defe26f81a7d1c466505c182f6bf5fabe0dcfe6321d892) to hopefully change the focus.

> 22. be more specific about your contribution

- My contributions are listed in a yellow box at the start of the PQI section and at the start of the Chapter, but I also added a new box to match at the start of the superfamily section [lines 68-73](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8c93eb1af6e5d1b25ddd80d382340750d494bdc918718ed18b46d4f1c3ed5fc4).

> 23. the superfamily section needs to be expanded

- [x] Added a bit more detail, especially [lines 40-56](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-8c93eb1af6e5d1b25ddd80d382340750d494bdc918718ed18b46d4f1c3ed5fc4) explained how the website is generally used, added a screenshot of the website showing a domain assignment, added a box to highlight what I contributed and was a bit more specific about that.

## Chapter 4 and previous chapter 5 (now merged into Chapter 4 as requested)

### Chapter 4

> 24. By focusing of protein domain regions alone, have you restricted yourself to a narrower range of genotype-phenotype predictions?

- [x] Yes, this was already described in section 4.6.1.3. But I now signpost it earlier: [4.1 "Introduction line 7](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-219eb4568ad9ea242d95775ed76e1ab41495946cd3b63be8537e504eb7753e68) and [4.2.1 "Approach" lines 27-31](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-d4f356ee102daac79e17db1d410f2ce356ff29860363b50dc1c613ab0815e86f) by describing that Snowflake is not meant to perfectly predict all phenotypes, but to uncover mechanisms for some phenotypes.

> 25. 4.2.2.2. Restricted phylogeny could have been better for deleterious variant predictions?

- [x] Added to discussion 4.7.1.2 ([line 69](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-1117b05358b708c0e605e15ba5fcb6ba657969d27fcb49ea77a703a1f04d6d82))as this is an interesting question, but it would be very substantial work and my belief is that it would make the coverage (even more) unusable.

> 26. 4.2.2.3 and 4.2.2.4 Schematic illustration of detailed steps would have been very helpful

- [x] Figure 4.2 contains these steps, but added some extra detail in the description underneath ([lines 94-101](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-d4f356ee102daac79e17db1d410f2ce356ff29860363b50dc1c613ab0815e86f)).

> 27. Did you try different clustering methods and check of consistency?

- [x] This is discussed in 4.5.2 - initial tests were done (which did show some variability) but a large enough benchmarking set was not available, so the clustering type was mostly chosen via theoretical justifications (non-spherical clusters). 

> 28. Did you use different distance measure and figure best performing one? Or the Euclidean measure was the only choice?

- [x] Yes, I did try euclidean as well as what I actually did, which was not euclidean, but can only motivate choice theoretically because there wasn't good enough data to trial lots of different things. This is discussed in 4.5.2.

> 29. Why did you not use UK biobank data instead of 1000 genomes data?

- [x] 1000 genomes are genomes chosen to have the most diverse possible genomes, while UKBiobank was not. The tool can take in any background set and it would be possible for people to use UKBiobank data as a background if they wanted to. Added a sentence to explain this in.

> 30. If you explain in more detail how your contribution has significantly enhanced the snowflake it would have been excellent.

 This information can be found in the yellow contributions box at the very start of the chapter, but I edited this to make it clearer ([lines 34-40](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-d4f356ee102daac79e17db1d410f2ce356ff29860363b50dc1c613ab0815e86f)), namely my contributions were:
    - Creation of inputs to Snowflake
    - Alternative clustering and scoring methods, particularly for intrinsic dimensionality
    - Scoring outputs
    - Improvements to speed and memory usage
    - Multiple imputation for missing calls
    - Inclusion of dimensionality reduction

> 31. What is typical range of phenotype score? What is max and min in your application across datasets? Although would depend on the dataset, can you provide a flavor for a typical range?

- The global-local phenotype score $\mu$ > 0, but has no upper limit since it is defined by distances within and between clusters, and this naturally depends on the number of SNPs (number of dimensions) and their FATHMM scores (how large the maximum distance is in that dimension). In some phenotypes a large score (representing a prediction) may be ~12, while in others it may be ~2.
- There is also a transformed score,  which is adjusted to make the scores and cut-off comparable across phenotypes. This transformed score ranges from -1 to 1, with scores over 0 representing a binary prediction that an individual has the phenotype. 
- [x] This is now described in the thesis.

> 32. Insert pseudocode (4.2.2)

- [x] Added more detail to the steps listed in 4.2.2 (1. Score variants for deleteriousness, 2. Map variants to phenotype, using dcGO and SUPERFAMILY and 3. Cluster individuals per phenotype and 4. Extract score and prediction) in pseudocode style so as to provide a place for an overview  ([lines 94-101](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-d4f356ee102daac79e17db1d410f2ce356ff29860363b50dc1c613ab0815e86f)). Each sub-part is described in detail in sections 4.2, 4.3 and 4.4.

> 33. compare with new version of snowflake (it it’s available)

- [x] Unfortunately code not available.

> 34. expand the metrics/clustering part to better justify choice of dataset

- Assuming here you meant the choice of 1000 genomes/having a diverse background set
- [x] I've added a short section for that [lines 341-346](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-e58c597f05b462d85935eb9f32352c687c71f9c23f1ce32bd122601061dd08e0)/

> 35. the actual results section is very short, need to be expanded and more detailed

- [x] Added to the ALSPAC section a part that explains some of the more promising aspects of Snowflake as a variant function predictor and related them to the paper about Nomaly

### Previous Chapter 5: ALSPAC

> 36. What is current state of application of snowflake to ALSPAC
- Completed, but ultimately an unsuccessful experiment. Snowflake did not perform well on the small number of chosen phenotypes and as discussed, there is a chance that the dataset has been used for GWAS that has informed DcGO, meaning that I don't think it is a good idea for future studies.

> 37. In section “5.2.1. Selection of phenotypes” limitation of snowflake could be due to relatively limited data? Or mutations in regions beyond domains? Did you check?

- [x] Yes - due to limited data in my opinion. **Some other phenotypes appear to be successful (see new section.)**

> 38. “In selecting phenotypes, I considered only (1) whether Snowflake considered these to be phenotypes where it could make a confident prediction and (2) whether the phenotypes in ALSPAC could be used to validate this prediction. I did not consider additional information that might indicate whether these were phenotypes we might expect to be able to predict, for example, whether these phenotypes were heritable, or consider whether they are desirable to predict. Since I chose these purely by looking at the distribution of scores for Snowflake, our lack of promising results could be an indication that the phenotype‑score (finding interesting distributions of phenotypes) is unsuccessful.” This para is not clear to me. Can you explain?

- [x] rephrased paragraph ([from line 66](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-7abea8191361686e4897ca1164747e30d728f638daf51ad42467a56009d14149))

> 39. In terms of snowflake application to ALSPAC. Did you consider randomizing the data or generate hypothetical random data and apply snowflake and compare the phenotype score with the ones you got for the original application of snowflake to ALSAPAC?

- No, in this case I think with such a small number of phenotypes (each with a very small number of positives), I don't think it would be fruitful unfortunately.

> 40. extremely short, consider merging with Chapter 4

- [x] Merged with chapter 4. Now [in Snowflake chapter](https://github.com/NatalieZelenka/phenotype_from_genotype/pull/61/files#diff-7abea8191361686e4897ca1164747e30d728f638daf51ad42467a56009d14149).

## Chapter 5

> 41.  Integration of gene expression (tissue-specific) did improve genotype-phenotype prediction to want extent though?

- It made 85,637 additional correct predictions, and only 23 more incorrect ones. Due to low coverage, this only corresponded to .001 Fmax, but it was highly statistically significant. 

> 42. Why GTex datasets were not considered

- I was already familiar with the FANTOM5 dataset, which provided data in a more usable format for me at the time. GTex later was included: as you could see in table 8.1

> 43. How does isoform expression factor in to this equation?

- All isoforms contributed towards the cut-off, and currently since the only incorrect predictions made by filip relate to development-related phenotypes, there is little to be gained in investigating this before improving coverage, but added to discussion.

> 44. Why proteomics data was not considered?

- Was not available in large enough quantities (see Chapter 8)

> 45. How did you deal with expression data supported by multiple different studies (biological replicates) to be expressed as against to those supported by limited number of studies or samples?

- A minimum avergage threshold must be chosen for each data set, but aside from this, all replicates (technical and biological) were treated equally for the purposes of filip.

> 46. I have an issue with being completely having belief in uberon as the gene expression is far more prone to rapid rewiring/reprogramming as compared to protein coding regions.

- Filip is designed to improve protein function predictions, so the gene expression data always relates to protein-coding regions.
- Uberon was used as one part of creating a mapping between traits, cells, tissues, and samples (necessary for the functioning of filip).

> 47. CAFA 2 Fmax appears quite low (extrapolating from machine learning studies)
- Yes. In general the Fmax is low for all teams - I think this is partially because any protein could have thousands of different predictions for function (as there are thousands of different protein function terms).

> 48. it might be worth discussing how much results depend on the chosen dataset, and/or on the use of DcGo.
- Yes I agree this would be interesting. I have already discussed the dataset in quite a lot of detail in the discussion, but:
- [x] added the point about dcGO and generally the uncertainty in how it would generalise to the discussion.

## Chapter 6. Ontolopy

>  49. Very interesting package that can be used to glean data from OBO files and manipulate them in a customized form. Can Ontolopy be used to build knowledge graphs? Or can be enhanced in future to do so?

- Not at present and I think that's probably beyond it's scope unless something quite dramatic happens!

> 50. Like gene ontologies are there one to many mappings, in that case is it possible to glean to most relevant mapping in a context specific manner?

- Ontolopy is only a package for interrogating and combining existing biomedical ontologies - so unless the ontologies loaded in have this information somehow (e.g. Gene Ontology has some information about how mappings were created and you could filter by this if you wanted).

> 51. How reliable are uberon to sample mappings in general? Are there some examples to clearly demonstrate this?

- I found them to be very reliable. See the combining chapter for a very detailed discussion of how the small number of discrepencies (<1%) could all be traced back to specific errors in the data and it helped me catch those.

## Chapter 7.  Combining RNA‑seq datasets

> 52. Are there specific demonstrable benefits of Combining RNA‑seq datasets at the data level not at the primary results level. These data might have been acquired in distinct conditions from slightly distinct sample. Are the data being treated either as biological or technical replicates?

- Yes agreed. This is something that I was very concerned with and I spent a lot of time thinking about whether it was possible to use  ComBat or ComBat-Seq to "remove" batch effects (see 7.4.2 and the appendix), but in the end I don't think that is possible with such an unbalanced dataset. My take is that this dataset is only really useful if you want to make a binary comparison between expressed/not expressed - but conveniently that is exactly what filip requires.

> 53. Does combining gene expression improve correlation with protein abundance?

- I'm not sure, but I think because the dataset still very much contains batch effects, it wouldn't make sense to test correlations. I would imagine that it would improve the agreement with protein abundance data over presence/absence of translation, but I haven't tested that.
- [x] I've added it to the discussion!