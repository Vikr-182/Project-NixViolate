from nltk import *
from nltk.tree import Tree
import sys
import csv
bro = open("../../scraping/rbi/usefullinks.txt")
data = list(csv.reader(bro))
useful = []
for j in range(len(data)):
        for i in range(len(data[j])):
                    useful.append(int(data[j][i]))

bro.close()
length = len(useful)


def get_chunk(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    contchunk = []
    currchunk = []

    for i in chunked:
        if type(i) == Tree:
            currchunk.append(" ".join([token for token, pos in i.leaves()]))
        elif currchunk:
            named_entity = " ".join(currchunk)
            if named_entity not in contchunk:
                contchunk.append(named_entity)
                currchunk = []
        else:
            continue
    return contchunk


for i in range(0, length):
    fname = str(i) + ".txt"
    f = open(fname, "r")
    a = f.readlines()
    article = a[0]
    words = article.split(" ")
    date = ""
    violator = ""
    violation = ""
    penalty = ""
    agency = "RBI"
    for i in range(0, len(words)):
        if(words[i] == "dated"):
            date = words[i+1] + " " + words[i+2] + " " + words[i+3]
            break

    for i in range(0, len(words)):
        if(words[i] == "penalty"):
            Q = words[i+3] + " " + words[i+4]
            b = Q.split(" ")
            try:
                if(b[1] == "lakh" or b[1] == "Lakh"):
                    try:
                        penalty = float(b[0]) * 100000
                    except:
                        penalty = 100000
                if (b[1] == "Crore" or b[1] == "crore"):
                    try:
                        penalty = float(b[0]) * 10000000
                    except:
                        penalty = 10000000
            except:
                pass
            break
    sys = ""
    for i in range(0, len(words)):
        if(words[i] == "on"):
            sus = ""
            for j in range(1, 6):
                try:
                    sus += words[i+j]+" "
                except:
                    pass
            break
    res = get_chunk(sus)
    try:
        violator = res[0]
    except:
        violator = ""
    sus = ""
    for i in range(0, len(words)):
        if(words[i] == "for"):
            sus = ""
            for j in range(1, 14):
                try:
                    sus += words[i+j]+" "
                except:
                    pass
            break
    violation = sus
    name = "format.csv"


    print(violator)
    print("{},,{},,,{},,{},,,,,{},,,,,,,,,,,,,,,,,,,,,,,,,,,,".format(
#    print("{},,{},,,,{},{},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,".format(
  #      violator, penalty,date, violation,"US Department of Justice"))
        violator, penalty, date, violation, "Reserve Bank of India"), file=open("../../website/templates/data/records_Cleaned.csv", "a"))
