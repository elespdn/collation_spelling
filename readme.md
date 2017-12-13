
#### Proposal:

# AUTOMATIC COLLATION OF MEDIEVAL LANGUAGES. ISOLATING ORTHOGRAPHICAL VARIATIONS.


When collating texts, scholars often need to distinguish between formal and substantive variation. Formal variation is often dismissed as non relevant for analyzing the relations among the witnesses, for example in stemmatics (even if this practice has been challenged by Andrews 2016). What is referred as formal variation may vary, from orthographical to morphological changes.

Orthographical variation, in particular, is a kind of formal variation considered non relevant for other than linguistic analysis. In the case of automatic collation, orthographical instability introduces a number of variations that should be kept distinguished from others (formal or substantive), for easiness of interpretation of the output.

Example 1
A: Lors conte li rois a la reine coment la dame del lac
B: Lors conte li rois a la reine comment la dame del lac
C: Lors conte li rois a la roine coment la dame del lac
D: Adonc li conte li rois comment la dame du lac

Example 2
A: et la reine se merveille mult
B: et ele s'an mervoille mout
C: et ele s'en merveille mult
D: et la reine s'en mervelle mult

In these examples, the orthographical variations are:

- reine / roine
- coment / comment
- del / du
- an / en
- merveille / mervoille /mervelle
- mult / mout,

while the substantial variations are:

- Lors conte / Adonc li conte
- a la reine / --
- et la reine / et ele
- se / s'en.

These variants might be considered all together or separatly. Current practices in automatic collation only support the first option, but cannot distinguish automaticaly between the two categories.

Various approaches have been applied in order to overcome this challenge. The attempts can be divided into two categories:

1. fuzzy match or **near match**. The program aligns not only on the basis of perfect matches, but also of imperfect matches. The original orthographical form is recorded, but variants in orthographical forms do not lead to a split in the alignment.
2. **normalization**. In this case the original forms would be turned into standard forms. In this case too, the original forms are not "lost", on the contrary they are available for the whole process, but not used during the alignment.

Here below we will test the two approaches. As a case study, small portion of four witnesses of the Old French prose *Lancelot* will be used. What apply to Old French can be valid for other medieval (and more in general, highly instable in their orthograph) languages. We will also focus on the open source program for automatic collation **CollateX**; this program proves to be the best option for aligning multiple witnesses of a text.


#### Goals of this study:

- assess which is the most efficient method for isolating orthographical variation in Old French and, more in general, medieval texts in the context of automatic collation. 
- test the use of NLP resources in the pre-processing of data for automatic collation
- further test and explore the near-match functionality in CollateX
- present additional visualization and export options for normalized collations in CollateX

---

Example available in [case_study](case_study) dir.

The results that better comply with the scholar's expectations ("ideal results") are reached using manual normalization (2a. Dictionary). They can be used for evaluating the others. 

#### 0. Normal
As a base for comparison, the texts will be first collated without any pre-processing. Collation is performed with *segmentation=False*, for easiness of comparison with the following results.

#### 1. Near match
For what concerns the first approach -Near Match-, CollateX offers a parameter 'near match' within the function 'collate'. Further experiments on this side should be assessed with the CollateX team; for instance, changes in the amount of edit distance or of the scoring system may lead to different results.

 --

For what concerns the second approach, i.e. normalization, two methods will be tested:

#### 2a. Dictionary
The original forms are normalized manually. A list of normalized forms is manually prepared and those forms will automatically take the place of the original ones for the collation. The output is rendered both in a table and as a graph.

Manual normalization gives the best results, but is also the most demanding way to prepare the text; it becomes almost impossible in the case of medium-size to long texts and small team working on them.


#### 2b. NLP
The original forms are normalized using linguistic information automatically extracted, and in particular 'lemma' and 'POS tag'. 

Lemmatization and POS tagging is performed with TreeTagger: parameters files are made available for Old French in the Medieval French Language Toolkit (https://github.com/sheiden/Medieval-French-Language-Toolkit). 

The list of words with POS and lemma info, that works as a dictionary, is created using [create\_dictionary\_using\_NLP.py](case_study/create_dictionary_using_NLP.py).

N.b.: the first attempts suggest that the automatic linguistic analysis needs to be checked manually and often corrected in order to have good results. It's worth clarifying that the aim in this scenario is not to have an excellent level of lemma and POS recognition, but to avoid mismatches, thus an error is not relevant as long as it won't lead to missing the alignment. 

#### Visualization and export note
The only visualization that allows at the moment to display the full results of the collation when a normalization has been performed, is the graph. In the case of a spelling variation, the graph will not split in two nodes, but one node only will be displayed, registering all the spelling variants on it. Thus the graph will split only if substantial variation occurs. (p.s.: check character encoding issues in the graph, e.g. 'ç')

As an additional visualization of the results, a table may be designed, which register the same information displayed on the graph. For instance, different colours or filling may signify different levels of variation and all the information can be shown through a dynamic rendering.

Furthermore, this information can be registered in the XML and in the XML/TEI output through attributes on the readings or on the group of readings.








