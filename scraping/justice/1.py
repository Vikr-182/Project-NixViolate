import sys
from requests import get
from bs4 import BeautifulSoup

finallink=[]

letter = sys.argv[1]

url='https://www.justice.gov/criminal-fraud/related-enforcement-actions/' + letter
try:
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    allEntries=soup.find("div",{"class":"node__content"})
    cnt = 0
except:
    print("RARA")
for para in allEntries.find_all('p')[1:-1]:
    cnt = cnt + 1
    link='https://www.justice.gov/'+para.a['href']
    try:
        resp=get(link)
        # print(link)
        print(cnt)
        so=BeautifulSoup(resp.text,'html.parser')
        dd=so.find("div",{"class":"node__content"})
        for para in dd.find_all('p'):
            if para.find('a'):
                if para.a.text[:13]=='Press Release':
                    finallink.append('https://www.justice.gov'+para.a['href'])
                    # print('\thttps://www.justice.gov'+para.a['href'])
                    break
    except:
        print("Not Able to get it")


string = ""
string += "Time-Stamp"
string += ","
string += "Heading"
string += ","
string += "Sub Heading\n"
f = open("./ref.csv","w")
for fl in finallink:
    try:
        re=get(fl)  
        s=BeautifulSoup(re.text,'html.parser')
        if s.find("div",{"class":"field--name-field-pr-date"}) and s.find(id='node-title') and s.find(id='node-subtitle'):
            date=s.find("div",{"class":"field--name-field-pr-date"}).text
            heading=s.find(id='node-title').text
            subheading=s.find(id='node-subtitle').text
            string += "\"" + date.replace("\n","") + "\""
            string += ","
            string += "\"" + heading.replace("\n","") + "\"" 
            string += ","
            string += "\"" + subheading.replace("\n","") + "\"" 
            string += "\n"
            print("\"" + date + "\"",end=",")
            print("\"" + heading + "\"",end=",")
            print("\"" + subheading + "\"")
    except:
        print("Not able to get it ")
f.write(string)

