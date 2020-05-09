import time
import requests as r
from bs4 import BeautifulSoup

useful = [49230, 49231, 49242, 49273, 49284, 49303,47605, 47725, 47781, 47784, 47787, 47803]

link = "https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid="
for i in useful:
    try:
        response = r.get(link + str(i))
        soup = BeautifulSoup(response.text, 'html.parser')
        dd=soup.find("table",{"class":"td","align":"center"})
        print(i)
        li = dd.text.split(" ")
        key = 0
        string.append(dd.text)
        print(dd.text)
    except:
        print("Not able to get it :(")

