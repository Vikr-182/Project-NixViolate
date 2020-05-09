from requests import get
from bs4 import BeautifulSoup

finallink=[]
cnt = 0

for alpha in range(0,1):
    url='https://www.justice.gov/criminal-fraud/related-enforcement-actions/'+chr(alpha+97)
    try:
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        allEntries=soup.find("div",{"class":"node__content"})
        for para in allEntries.find_all('p')[1:-1]:
            link='https://www.justice.gov/'+para.a['href']
            resp=get(link)
            print(cnt+1)
            cnt = cnt + 1
            # print("Kar raha hu")
            so=BeautifulSoup(resp.text,'html.parser')
            dd=so.find("div",{"class":"node__content"})
            for para in dd.find_all('p'):
                if para.find('a'):
                    if para.a.text[:13]=='Press Release':
                        finallink.append('https://www.justice.gov'+para.a['href'])
                        break
    except:
        print("Not able to get it ")

# print("Huii!!")
print(finallink)
f = open("usefullinks.txt","a")
for j in range(len(finallink)-1):
    f.write(str(finallink[j]) + ",")
f.write(str(finallink[len(finallink)-1]))
f.close()

'''
for finallink in finallink:
    re=get(finallink)
    s=BeautifulSoup(re.text,'html.parser')
    date=s.find("div",{"class":"field--name-field-pr-date"}).text
    heading=s.find("div",{"class":"node-title"}).text
    subheading=s.find("div",{"class":"node-subtitle"}).text
    print(date,end=",")
    print(heading,end=",")
    print(subheading)
    print()

'''
