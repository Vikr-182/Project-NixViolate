import time
import requests as r
from bs4 import BeautifulSoup
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
print(start,end)
useful = []
link = "https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid="
count = 0
error = 0
for i in range(start,end):
    try:
        response = r.get(link + str(i))
        soup = BeautifulSoup(response.text, 'html.parser')
        dd=soup.find("td",{"class":"tableheader","align":"center"})
        print(i)
        li = dd.text.split(" ")
        key = 0
        for j in li:
            if j == 'imposed' or j == 'imposes':
                key = key + 1
            if j == 'penalty':
                key = key + 1
        if key >= 2:
            useful.append(i)
            print(dd.text)
        # get the item in this
    except:
        print("Not able to get it :(")


f = open("usefullinks.txt","a")
print(useful)
for j in range(len(useful)-1):
    f.write(str(useful[j]) + ",")
f.write(str(useful[len(useful)-1]))
f.close()
error = count
