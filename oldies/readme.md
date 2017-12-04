#### Proposal:

# AUTOMATIC COLLATION OF MEDIEVAL LANGUAGES. HOW TO DEAL WITH SPELLING VARIATION

Spelling variation is a well known challenge for the collation of medieval texts (and not only). This is because often, though not always, the user is interested in substantial variation, and not in spelling variation. Thus the automatic collation of texts "as they are", that is without any pre-processing, may bring disappointing results, because the program will recognize as a variant both spelling and substantial differences.

Various approaches have been applied in order to overcome this challenge and to have only substantial differences recognized as variants by the program performing automatic collation. These attempts can be divided into two categories:

1. fuzzy match or **near match**. The program aligns not only on the basis of perfect matches, but also of imperfect matches;
2. **normalization**. In this case the original forms would be turned into standard forms. Please note that the original forms are not "lost", on the contrary they are available for the whole process, but not used during the alignment.

This study will test the two approaches, using two corpora:
- a section of the 'Divina Commedia' in the three witnesses copied by Boccaccio (Italian, XIV century)
- one or more paragraphs of the prose 'Lancelot' in seven witnesses (French, XIII century)

The open source program **CollateX** will be used for the automatic collation.


#### Goals of this study:

- assess which is the most efficient method for overcoming spelling variation and obtaining only substantial variation in the automatic collation of medieval texts, at the current state of the art
- test the use of NLP resources in the pre-processing of data for automatic collation
- further test and explore the near-match functionality in CollateX
- present additional visualization and export options for normalized collations in CollateX

---

In the two examples

- [dante_firstlines](dante/dante_firstlines.ipynb) (easier, better starting from here)
- [lancelot_conte](lancelot/lancelot_conte.ipynb) 


four ways will be tested.

The results that better comply with the scholar's expectations ("ideal results") are reached using manual normalization (2a. Dictionary). They can be used for evaluating the others. 

#### 0. Normal
As a base for comparison, the texts will be first collated without any pre-processing. Collation is performed with *segmentation=False*, for easiness of comparison with the following results.

#### 1. Near match
For what concerns the first approach -Near Match-, CollateX offers a parameter 'near match' within the function 'collate'. Further experiments on this side should be assessed with the CollateX team; for instance, changes in the amount of edit distance or of the scoring system may lead to different results.

 --

For what concerns the second approach -Normalization-, two methods will be tested:

#### 2a. Dictionary
The original forms are normalized manually. A list of normalized forms is manually prepared and those forms will automatically take the place of the original ones for the collation. The output is rendered both in a table and as a graph.

Manual normalization gives the best results, but is also the most demanding way to prepare the text; it becomes almost impossible in the case of medium-size to long texts and small team working on them.


#### 2b. NLP
The original forms are normalized using linguistic information automatically extracted, and in particular 'lemma' and 'POS tag'. In both cases for the lemmatization and POS tagging it is possible to use TreeTagger: parameters files are made available for Italian in D(h)ante by Angelo Basile (Fondazione Bruno Kessler - http://dh.fbk.eu/D%28h%29ante), and for French in the Medieval French Language Toolkit (https://github.com/sheiden/Medieval-French-Language-Toolkit). In this scenario, a list of normalized forms are prepared, not manually, but automatically, using 'lemma' + 'POS tag'. For example, 'camin' and 'cammin' both become 'SScammino', which means that the lemma is 'cammino' and that it is a noun (sostantivo S) singular S. 

The list of words with POS and lemma info, that works as a dictionary, is created using [create\_pos\_lemma.py](lancelot/create_pos_lemma.py).

N.b.: the first attempts suggest that the automatic linguistic analysis needs to be checked manually and often corrected in order to have good results. It's worth clarifying that the aim in this scenario is not to have an excellent level of lemma and POS recognition, but to avoid mismatches, thus an error is not relevant as long as it won't lead to missing the alignment. Also, while the Medieval French Toolkit offers both POS and lemma tagging, D(h)ante only has POS tagging and not lemma identification, which is added manually.

#### Visualization and export note
The only visualization that allows at the moment to display the full results of the collation when a normalization has been performed, is the graph. In the case of a spelling variation, the graph will not split in two nodes, but one node only will be displayed, registering all the spelling variants on it. Thus the graph will split only if substantial variation occurs. (p.s.: check character encoding issues in the graph, e.g. 'ç')

As an additional visualization of the results, a table may be designed, which register the same information displayed on the graph. For instance, different colours or filling may signify different levels of variation and all the information can be shown through a dynamic rendering.

Furthermore, this information can be registered in the XML and in the XML/TEI output through attributes on the readings or on the group of readings.








