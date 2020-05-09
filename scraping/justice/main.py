from requests import get
import csv
import time
from bs4 import BeautifulSoup
bro = open("./usefullinks.txt")
data = list(csv.reader(bro))
print(data)
useful = []
for j in range(len(data)):
        for i in range(len(data[j])):
                    useful.append(data[j][i])
                    print(useful)
bro.close()
finallink=[]
#finallink = ['https://www.justice.gov/opa/pr/2010/September/10-crm-1096.html', 'https://www.justice.gov/opa/pr/2010/September/10-crm-1096.html', 'https://www.justice.gov/opa/pr/2004/July/04_crm_465.htm', 'https://www.justice.gov/opa/pr/2008/June/08-crm-491.html', 'https://www.justice.gov/opa/pr/2009/September/09-crm-1056.html', 'https://www.justice.gov/opa/pr/2010/September/10-crm-1034.html', 'https://www.justice.gov/opa/pr/2010/September/10-crm-1034.html', 'https://www.justice.gov/opa/pr/oil-executives-plead-guilty-roles-bribery-scheme-involving-foreign-officials', 'https://www.justice.gov/opa/pr/oil-executives-plead-guilty-roles-bribery-scheme-involving-foreign-officials', 'https://www.justice.gov/opa/pr/2008/November/08-crm-1041.html', 'https://www.justice.gov/opa/pr/airbus-agrees-pay-over-39-billion-global-penalties-resolve-foreign-bribery-and-itar-case', 'https://www.justice.gov/opa/pr/mobile-telesystems-pjsc-and-its-uzbek-subsidiary-enter-resolutions-850-million-department', 'https://www.justice.gov/opa/pr/2007/December/07_crm_1024.html', 'https://www.justice.gov/opa/pr/2010/December/10-crm-1481.html', 'https://www.justice.gov/opa/pr/2010/December/10-crm-1481.html', 'https://www.justice.gov/opa/pr/2014/January/14-crm-019.html', 'https://www.justice.gov/opa/pr/2013/December/13-crm-1356.html', 'https://www.justice.gov/opa/pr/mozambique-s-former-finance-minister-indicted-alongside-other-former-mozambican-officials', 'https://www.justice.gov/opa/pr/2010/August/10-crm-903.html', 'https://www.justice.gov/opa/pr/2010/August/10-crm-903.html', 'https://www.justice.gov/opa/pr/2010/August/10-crm-903.html', 'https://www.justice.gov/opa/pr/alstom-pleads-guilty-and-agrees-pay-772-million-criminal-penalty-resolve-foreign-bribery%20', 'https://www.justice.gov/opa/pr/two-members-billion-dollar-venezuelan-money-laundering-scheme-arrested', 'https://www.justice.gov/opa/pr/florida-businessman-pleads-guilty-foreign-bribery-charges-connection-venezuela-bribery-scheme', 'https://www.justice.gov/opa/pr/2010/January/10-crm-048.html', 'https://www.justice.gov/opa/pr/2006/September/06_crm_595.html', 'https://www.justice.gov/opa/pr/former-venezuelan-national-treasurer-sentenced-10-years-prison-money-laundering-conspiracy', 'https://www.justice.gov/opa/pr/two-florida-executives-one-florida-intermediary-and-two-former-haitian-government-officials', 'https://www.justice.gov/opa/pr/2011/December/11-crm-1678.html', 'https://www.justice.gov/opa/pr/four-businessmen-and-two-foreign-officials-plead-guilty-connection-bribes-paid-mexican', 'https://www.justice.gov/opa/pr/avon-china-pleads-guilty-violating-fcpa-concealing-more-8-million-gifts-chinese-officials', 'https://www.justice.gov/opa/pr/avon-china-pleads-guilty-violating-fcpa-concealing-more-8-million-gifts-chinese-officials', 'https://www.justice.gov/opa/pr/2013/December/13-crm-1356.html', 'https://www.justice.gov/opa/pr/2011/July/11-crm-911.html', 'https://www.justice.gov/opa/pr/2010/January/10-crm-048.html']
finallink = useful
string = ""
print(len(useful))
for finallink in finallink:
    try:
        print(finallink + "getting")
        re=get(finallink)
        s=BeautifulSoup(re.text,'html.parser')
        if s.find("h1",{"class":"node-title"}) is not None:
            date=s.find("span",{"id":"date-display-single"}).text
            heading=s.find("h1",{"id":"node-title"}).text
            string += data 
            string += ","
            string += heading
            string += ","
            print(date,end=",")
            print(heading,end=",")
            #print(subheading)
            print()
        else:
            print("None")
    except:
        print("Not able to find anything")

print(string)
