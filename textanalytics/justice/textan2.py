import csv
import sys
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
sentArr = []

guiltwords = ["Pleads", "Agrees", "Charged"]
violWords = ["Resolve", "Alleged", "Guilty"]

dateDict = {}


def violationCheck(text):
    violation = ""
    a = text.split(" ")
    found = 0
    for i in range(0, len(a)):
        if(a[i] == violWords[0] or a[i] == violWords[1]):
            found = 1
            for j in range(1, 5):
                try:
                    violation += a[i+j] + " "
                except:
                    pass
            break
        if(a[i] == violWords[2]):
            found == 1
            for j in range(1, 5):
                try:
                    violation += a[i+j] + " "
                except:
                    pass
            break
    if (found == 1):
        return violation
    else:
        for i in range(0, len(a)):
            if(a[i] == "for"):
                found == 1
                for j in range(1, 7):
                    try:
                        violation += a[i+j] + " "
                    except:
                        pass
                break
        if(found == 1):
            return violation
        else:
            return -1


def guiltyCheck(text):
    a = text.split(" ")
    found = 0
    idx = -100
    violator = ""
    for i in range(0, len(a)):
        if(a[i] in guiltwords):
            found = 1
            idx = i
            break

    if (found == 1):

        for i in range(0, idx):
            violator += a[i]+" "
        violator = violator.rstrip(" ")
        violator = violator.rstrip("and")
        violator = violator.rstrip("and  ")
        return violator
    else:
        return -1


def penaltyCheck(text):
    a = text.split(" ")
    cost = ""
    found = 0
    for i in range(0, len(a)):
        try:
            if (a[i][0] == "$"):
                found = 1
                cost += a[i].lstrip("$") + " "+a[i+1]
                break
        except:
            pass
    if(found == 1):
        b = cost.split(" ")
        num = float(b[0])
        if(b[1] == "Million"):
            return num * 1000000
        elif(b[1] == "Billion"):
            return num*1000000000
    else:
        return -1


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


with open('JusticeData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if(line_count == 0):
            line_count += 1
            continue

        l = len(row)
        sent = ""
        for i in range(1, l):
            sent += row[i] + " "

        dateDict[sent] = row[0]
        sent = sent.rstrip(" ")
        sentArr.append(sent)

        # print(row)

for sent in sentArr:
    a = sent.split(" ")
    Agency = "DOJ"
    violation = ""
    sus = ""
    violator = " "
    penalty = 0
    try:
        date = dateDict[sent]
    except:
        date = " "
    for i in range(10):
        try:
            sus += a[i]+" "
        except:
            pass
    res = get_chunk(sus)
    res2 = guiltyCheck(sus)
    if (res2 == -1):
        try:
            violator = res[0]
        except:
            pass
    else:
        violator = res2

    res = penaltyCheck(sent)
    if(res == -1):
        peanlty = 0
    else:
        penalty = res
        if(res == None):
            penalty = 0

    res = violationCheck(sent)
    if(res == -1):
        violation = " "
    else:
        violation = res
        # print(violation)
    sys.stdout = open('../../website/app/data/records_Cleaned.csv', 'a')
    print("{},,{},,,{},,{},,,,,{},,,,,,,,,,,,,,,,,,,,,,,,,,,,".format(
        violator, penalty,date, violation,"US Department of Justice"))
    # company , penalty, violation date ,
