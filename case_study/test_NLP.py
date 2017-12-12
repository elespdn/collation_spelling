
import treetaggerwrapper, os, re


# create a folder where to store intermediate results.
# They can be used for refining the data in between.
try:
    os.makedirs('data/example1/halfway')
except OSError:
    pass


def lemmatization(indir, outdir):
    for infile, outfile in zip(indir, outdir):
            open(outfile, 'w', encoding='utf-8')
            tagger = treetaggerwrapper.TreeTagger(TAGLANG='stein')
            tagger.tag_file_to(infile, outfile)


# CLEAN THE OUTPUT OF THE LEMMATIZATION
# ('_.*', ''),
# ('\d', '')
##

def clean(indir, outdir):
    patterns = [('_.*', ''),
                ('\d.*', ''),
                ('\|.*', '')]
    for infile, outfile in zip(indir, outdir):
        t = open(infile).read()

        for (p1,p2) in patterns:
            print(p1)
            p = re.compile(p1)
            t = p.sub(p2, t)

        o = open(outfile, 'w', encoding='utf-8')
        o.write(t)
        o.close()


# EXTRACT ONLY THE LEMMAS
def make_pos_lemma(indir, outdir):
    for infile, outfile in zip(indir, outdir):
        infile = open(infile, 'r')
        outfile = open(outfile, 'w')
        for aline in infile:
            values = aline.split()
            original = values[0]
            pos = values[1]
            lemmas = values[2]
            outfile.write(original + ',' + pos + '_' + lemmas + '\n')

        infile.close()
        outfile.close()


# WSSin = 'C:/Users/Elena/Documents/example-3wss/WSSin'
# I have tried to put all the input file into one folder and point to that one,
# instead of specifying the single files, but this way it does not work

W1in = 'data/example1/W1.txt'
W2in = 'data/example1/W2.txt'
W3in = 'data/example1/W3.txt'
W4in = 'data/example1/W4.txt'
WSSin = [W1in, W2in, W3in, W4in]

W1out = 'data/example1/halfway/W1-lemmatized.txt'
W2out = 'data/example1/halfway/W2-lemmatized.txt'
W3out = 'data/example1/halfway/W3-lemmatized.txt'
W4out = 'data/example1/halfway/W4-lemmatized.txt'
WSSout = [W1out, W2out, W3out, W4out]

W1out_clean = 'data/example1/halfway/W1-lemmatized-clean.txt'
W2out_clean = 'data/example1/halfway/W2-lemmatized-clean.txt'
W3out_clean = 'data/example1/halfway/W3-lemmatized-clean.txt'
W4out_clean = 'data/example1/halfway/W4-lemmatized-clean.txt'
WSSout_clean = [W1out_clean, W2out_clean, W3out_clean, W4out_clean]

W1out_pos_lemma = 'data/example1/halfway/W1-pos_lemma.txt'
W2out_pos_lemma = 'data/example1/halfway/W2-pos_lemma.txt'
W3out_pos_lemma = 'data/example1/halfway/W3-pos_lemma.txt'
W4out_pos_lemma = 'data/example1/halfway/W4-pos_lemma.txt'
WSSout_pos_lemma = [W1out_pos_lemma, W2out_pos_lemma, W3out_pos_lemma, W4out_pos_lemma]



lemmatization(WSSin, WSSout)

clean(WSSout, WSSout_clean)

make_pos_lemma(WSSout_clean, WSSout_pos_lemma)
