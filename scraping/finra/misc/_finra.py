from requests import get
from bs4 import BeautifulSoup

url='https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=0'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
totalEntries=soup.find("div", {"class": "globalAlignRight"}).text

f=open("finra.csv", "w+")
f.write("link;case_summary;Document_Type;Name;Date\n")
f.close()
f=open("finra.csv", "a")
for i in range (0,int(int(totalEntries.split()[-1])/15)):
    url='https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page='+str(i)
    print(url)
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table=soup.find("div",{"class":"table-responsive"})
    for ttr in table.find_all('tr')[1:]:
        if ttr.find('td').find('a'):
            line='www.finra.org'+ttr.find('td').a['href']
        for ttd in ttr.find_all('td')[1:]:
            line = line + ";\"" + ttd.text +"\""
        f.write(line+"\n")

f.close()    


