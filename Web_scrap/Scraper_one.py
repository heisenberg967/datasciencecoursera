##imports
import requests
from BeautifulSoup import BeautifulSoup
import pandas as pd
import csv

##to be appended to
records = []
records2 = []
records3 = []
records4 = []
records5 = []
records6 = []
##scrapes top 500 companies in India
for i in range(1,25):
	url="https://www.fundoodata.com/companytypedata/2/list-of-india's-top-500-companies-in-india?&pageno="+str(i)+"&tot_rows=500&total_results=500&no_of_offices=0"
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	
	soupx = soup.findAll('div',attrs={'class':'normal-detail'})	 
	for soup2 in soup.findAll('div',attrs={'class':'heading'}):
		x = (soup2.text)
		records.append(x)
	
	for result in soupx:
		typ = result.findAll('tr')
		ind = typ[0].text[9:]
		records2.append(ind)
		sub = typ[1].text[13:]
		records3.append(sub)
		ctyp = typ[2].text[13:]
		records4.append(ctyp)
		level = typ[3].text[16:]
		records5.append(level)
		loc = typ[len(typ)-1].text[9:]
		records6.append(loc)

df = pd.DataFrame(records,columns=['Company Name'])
df2 = pd.DataFrame(records2,columns=['Industry'])
df3 = pd.DataFrame(records3,columns=['Sub-Industry'])
df4 = pd.DataFrame(records4,columns=['Company type'])
df5 = pd.DataFrame(records5,columns=['Level of Office'])
df6 = pd.DataFrame(records6,columns=['Location'])
frames=[df,df2,df3,df4,df5,df6]
result=pd.concat(frames, axis=1)
result.to_csv("company_list.csv",index=False,encoding='utf-8')