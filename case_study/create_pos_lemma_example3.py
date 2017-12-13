
import treetaggerwrapper, os, re

# create a folder where to store intermediate results.
try:
    os.makedirs('data/example3/process')
except OSError:
    pass

# put together the texts of all the witnesses
with open('data/example3/W1.txt') as W1, \
     open('data/example3/W2.txt') as W2, \
     open('data/example3/W3.txt') as W3, \
     open('data/example3/W4.txt') as W4, \
     open('data/example3/process/p1_all_texts.txt', 'w', encoding='utf-8') as all_texts:
    all_texts.write(W1.read() + ' ' + W2.read() + ' ' + W3.read() + ' ' + W4.read())

# each word a new line, in alphabetical order: sorted()
infile = open('data/example3/process/p1_all_texts.txt').read()
outfile = open('data/example3/process/p2_all_words.txt', 'w', encoding='utf-8')
words = infile.split()
for word in sorted(words):
    outfile.write(word + '\n')

# delete duplicates
infile = 'data/example3/process/p2_all_words.txt'
lines_seen = set() # holds lines already seen
outfile = open('data/example3/process/p3_single_words.txt', 'w', encoding='utf-8')
for line in open(infile, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

# pos and lemma tagging
infile = 'data/example3/process/p3_single_words.txt'
outfile = 'data/example3/process/p4_single_words_analyzed.txt'
open(outfile, 'w', encoding='utf-8')
tagger = treetaggerwrapper.TreeTagger(TAGLANG='stein')  ## already tried with ,TAGOUTENC='utf8' but does not change anything) 
tagger.tag_file_to(infile, outfile)


# clean pos and lemma tagging, keeping only the first lemma suggested
infile = 'data/example3/process/p4_single_words_analyzed.txt'
outfile = 'data/example3/process/p5_single_words_analyzed_clean.txt'
patterns = [('_.*', ''),
            ('\d.*', ''),
            ('\|.*', ''),
            ('�', 'ö'),
            ('<nolem>', 'UNKNOWN')]
t = open(infile).read()
for (p1,p2) in patterns:
    print(p1)
    p = re.compile(p1)
    t = p.sub(p2, t)
o = open(outfile, 'w', encoding='utf-8')
o.write(t)
o.close()


# create pos_lemma.csv
infile = open('data/example3/process/p5_single_words_analyzed_clean.txt', 'r')
outfile = open('pos_lemma_example3.csv', 'w', encoding='utf-8')
for aline in infile:
    values = aline.split()
    original = values[0]
    pos = values[1]
    lemmas = values[2]
    outfile.write(original + ',' + pos + '_' + lemmas + '\n')
infile.close()
outfile.close()






