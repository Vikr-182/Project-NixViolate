from requests import get
from bs4 import BeautifulSoup

url='https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=0'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
totalEntries=soup.find("div", {"class": "globalAlignRight"}).text

f=open("../records_Cleaned.csv", "a")

url='https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=0'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table=soup.find("div",{"class":"table-responsive"})
agency = "FINRA"
penalty = ""
violation = ""
violator = ""
date = ""
year = ""

for ttr in table.find_all('tr')[1:]:
    cnt = 0
    if ttr.find('td').find('a'):
        line='www.finra.org'+ttr.find('td').a['href']
    for ttd in ttr.find_all('td')[1:]:
        cnt = cnt + 1
        line = line + ",\"" + ttd.text.replace("\n","") +"\""
        if cnt is 1:
            violation = "\"" + ttd.text.replace("\n","") + "\""
        elif cnt is 3:
            violator = "\"" + ttd.text.replace("\n","") + "\""
        elif cnt is 4:
            year = "\"" + ttd.text.split("/")[2] + "\""
    f.write("{},,{},,,{},,{},,,,,{},,,,,,,,,,,,,,,,,,,,,,,,,,,,\n".format(
                    violator, penalty, year,violation,"FINRA"))
    #f.write(line+"\n")

f.close()    


