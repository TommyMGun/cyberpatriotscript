import requests
import bs4
import os

'''url = requests.get('https://www.uscyberpatriot.org/Pages/Readme/readme_cpxii_exrd_comp_se_ubu14_9rmd5b49nd.aspx')
#soup = bs4.BeautifulSoup(url.text, 'lxml')

s = soup.select('#ctl00_PlaceHolderMain_ctl02__ControlWrapper_RichHtmlField > pre > span')
s = str(s)
s=s.split("\n",1)[1]'''


def win_automation():
	#url = input('Please enter README link >')
	url='https://www.uscyberpatriot.org/Pages/Readme/readme_cpxii_exrd_comp_se_ubu14_9rmd5b49nd.aspx'
	url = requests.get(url)
	soup = bs4.BeautifulSoup(url.text, 'lxml')
	print(soup.select('#ctl00_PlaceHolderMain_ctl02__ControlWrapper_RichHtmlField > pre > span'))




#def linux_automation():



if os.name == 'nt':
	print('Detected OS: Windows\n')
	win_automation()
	
else:
	print('Detected OS: Unix\n')
