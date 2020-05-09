import time
import requests as r
from bs4 import BeautifulSoup
import csv

bro = open("../../scraping/rbi/usefullinks.txt")
data = list(csv.reader(bro))
useful = []
for j in range(len(data)):
    for i in range(len(data[j])):
        useful.append(int(data[j][i]))
print(useful)
bro.close()
#useful = [49230, 49231, 49242, 49273, 49284, 49303,
 #         47605, 47725, 47781, 47784, 47787, 47803]

link = "https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid="
j = 0
for i in useful:

    try:
        response = r.get(link + str(i))
        soup = BeautifulSoup(response.text, 'html.parser')
        dd = soup.find("table", {"class": "td", "align": "center"})
        # print(i)
        li = dd.text.split(" ")
        key = 0
        fname = str(j) + ".txt"
        j += 1
        print(dd.text, file=open(fname, "w"))
        # get the item in this
    except:
        print("Not able to get it :(")

print(useful)
