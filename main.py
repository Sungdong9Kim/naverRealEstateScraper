#from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

html = requests.get("https://m.land.naver.com/complex/info/467?tradTpCd=A1&ptpNo=&bildNo=&articleListYN=Y")
bsObj = BeautifulSoup(html.text,"html.parser")
priceList = bsObj.findAll("span")
for price in priceList:
    print(price)