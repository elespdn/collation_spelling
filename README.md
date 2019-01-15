# Strategies for the collation of medieval texts

In this folder there are examples of automatic collation with different strategies for handling **spelling variation** in medieval languages and for automatically identifying **formal (graphic and phonetic) vs substantive** textual variants.

The software used for collation is CollateX (Dekker-Middell 2011; Dekker et al. 2015) in its Python version (<https://pypi.org/project/collatex/>).

The strategies are:

- near match, i.e. in the alignment phase matches are found not only between equal tokens but also between similar tokens (edit distance value is set);
- manual dictionary, containing formal variants and corresponding normalised form;
- automatic dictionary, i.e. a dictionary with normalised forms created from linguistic analysis of tokens, in particular "POS_lemma".


Examples in various languages. For French and Spanish, NLP tools are available:

- for Old Spanish, Freeling with dedicated module (Padró-Stanilovsky 2012; Boleda 2011; Porta et al. 2013);
- for Old French, TreeTagger with two modules gathered in the Medieval French Language Toolkit (Schmid 1994; <https://github.com/sheiden/Medieval-French-Language-Toolkit>).

Both can be integrated, using an API or a Python Wrapper (TreeTagger).

For Italian, only manual dictionary is available.


## Repo structure

There is a folder for each language. Inside them, there are examples in Jupyter notebooks and folders for:

- data, containing the texts of the witnesses
- dictionaries, containing the dictionaries for normalization generated manually and automatically;
- results, containing html tables with the results.


## How to test

All the code is in Jupyter notebooks. It can be visualized here (Github website renders it, refresh the page if it takes too much time) or through the [nbviewer](http://nbviewer.jupyter.org/). If you want to run the code, download this repo, install [Juypter](https://jupyter.org/) on your machine and launch it, and open the notebooks.

The results of each example are in the folder 'Results' (see here above).

For step by step instructions, see below.



## Some bibliographic reference

Boleda, Gemma. 2011. «Extending the tool, or how to annotate historical language varieties». In In Proceedings of the 5th ACL-HLT Workshop on Language Technology for Cultural Heritage, Social Sciences, and Humanities, 1–9.

Dekker, Ronald Haentjens, Dirk van Hulle, Gregor Middell, Vincent Neyt, e Joris van Zundert. 2015. «Computer-Supported Collation of Modern Manuscripts: CollateX and the Beckett Digital Manuscript Project». Digital Scholarship in the Humanities 30 (3): 452–70. https://doi.org/10.1093/llc/fqu007.

Dekker, Ronald Haentjens, e Gregor Middell. 2011. «Computer-Supported Collation with CollateX: Managing Textual Variance in an Environment with Varying Requirements». In Supporting Digital Humanities (University of Copenhagen, 17-18 November 2011).

Padró, Lluís, e Evgeny Stanilovsky. 2012. «FreeLing 3.0: Towards Wider Multilinguality». In Proceedings of the Language Resources and Evaluation Conference (LREC 2012) ELRA. Istanbul, Turkey. May, 2012.

Porta, Jordi, Jos&eacute;-Luis Sancho, e Javier G&oacute;mez. 2013. «Edit transducers for spelling variation in Old Spanish». In Proceedings of the workshop on computational historical linguistics at NODALIDA 2013; May 22-24; 2013; Oslo; Norway. NEALT Proceedings Series 18, 70–79. Linköping University Electronic Press.

Schmid, Helmut. 1994. Probabilistic Part-of-Speech Tagging Using Decision Trees.

---


## Step by step testing

1. Download this repo:
    - Download this Github repository, using the green button 'Clone or download' above. Choose 'Download ZIP'.
    - Move the zip file to a safe place in your computer where you can find it later, e.g. the 'Documents' folder.
    - Unzip it

2. Install the Jupyter Notebook:
    - as explained in the [Jupyter website](https://jupyter.org/install.html), the best way to install it is through Anaconda: [download and install Anaconda](https://www.anaconda.com/download/).

3. Launch Jupyter Notebook:
    - Open the Terminal (Mac/Linux) or Command Prompt (Windows) and go to the folder where you moved the downloaded Repo, e.g. the 'Documents' folder (see step 1). Use the command ```cd``` to navigate your file system.
    - Run the Notebook with the following command: ```jupyter notebook```
    - A page will open in your default browser at 'http://localhost:8888'. Now you can navigate the files and open them using double click, as if you were in your computer (you actually are in your computer, it is just that you access through the browser :)

4. Test an example
    - Go to folder 'case_study_FR' and open 'example1.ipynb' (this is the extension of a Juypter notebook). The file will open in a new tab.
    - Select the first code cell (you'll see 'In [1]' on the left) just by placing your cursor into it and click. Then run the code using the 'Play' button in the bar above (8th button from left). The result will be (re)generated immediately. You can try with all the code cells below (all those having 'In' and a number on the left). The result will appear below each cell code.
    - Some of the results are saved in the 'Results' folder as html tables. You can open them not as Jupyter notebook, but going back to your file system and double-clicking them as with normal files. They should be open in a browser.

5. Test with your own data





