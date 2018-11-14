
In this folder there are examples of automatic collation with different strategies for handling formal vs substantive textual variations.

The software used for collation is CollateX (Dekker-Middell 2011; Dekker et al. 2015) in its Python version (<https://pypi.org/project/collatex/>).

The strategies are:

- near match, i.e. in the alignment phase matches are found not only between equal tokens but also between similar tokens (edit distance value is set);
- manual dictionary, containing formal variants and corresponding normalised form
- automatic dictionary, i.e. a dictionary with normalised forms created from linguistic analysis of tokens, in particular "POS_lemma".


Examples in various languages; for French and Spanish, NLP tools are available:

- for Old Spanish, Freeling with dedicated module (Padró-Stanilovsky 2012; Boleda 2011; Porta et al. 2013). 
- for Old French, TreeTagger with two modules gathered in the Medieval French Language Toolkit (Schmid 1994; <https://github.com/sheiden/Medieval-French-Language-Toolkit>)-

Both can be integrated, using an API or a Python Wrapper (TreeTagger).

For Italian, only manual dictionary is available.


---

Biblio

Boleda, Gemma. 2011. «Extending the tool, or how to annotate historical language varieties». In In Proceedings of the 5th ACL-HLT Workshop on Language Technology for Cultural Heritage, Social Sciences, and Humanities, 1–9.

Dekker, Ronald Haentjens, Dirk van Hulle, Gregor Middell, Vincent Neyt, e Joris van Zundert. 2015. «Computer-Supported Collation of Modern Manuscripts: CollateX and the Beckett Digital Manuscript Project». Digital Scholarship in the Humanities 30 (3): 452–70. https://doi.org/10.1093/llc/fqu007.

Dekker, Ronald Haentjens, e Gregor Middell. 2011. «Computer-Supported Collation with CollateX: Managing Textual Variance in an Environment with Varying Requirements». In Supporting Digital Humanities (University of Copenhagen, 17-18 November 2011).

Padró, Lluís, e Evgeny Stanilovsky. 2012. «FreeLing 3.0: Towards Wider Multilinguality». In Proceedings of the Language Resources and Evaluation Conference (LREC 2012) ELRA. Istanbul, Turkey. May, 2012.

Porta, Jordi, Jos&eacute;-Luis Sancho, e Javier G&oacute;mez. 2013. «Edit transducers for spelling variation in Old Spanish». In Proceedings of the workshop on computational historical linguistics at NODALIDA 2013; May 22-24; 2013; Oslo; Norway. NEALT Proceedings Series 18, 70–79. Linköping University Electronic Press.

Schmid, Helmut. 1994. Probabilistic Part-of-Speech Tagging Using Decision Trees.
