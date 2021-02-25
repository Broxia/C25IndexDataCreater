import requests
from requests import get
from bs4 import BeautifulSoup
import csv

def ScrapeSymbols():
  print("Scraping all symbols from Nasdaq OMX C25...")
  url = 'http://www.nasdaqomxnordic.com/shares/listed-companies/copenhagen'

  headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)',}
  try:
    results = requests.get(url, headers=headers, timeout=10)
  except Exception as e:
    print(e)
  symbols = []

  soup = BeautifulSoup(results.text, "html.parser")

  table = soup.find_all('td')

  i = 0
  td = 0
  while i < len(table):
    if td == 1:
      symbol = table[i].text.replace(' ', '-')
      symbol = symbol + ".CO"
      symbols.append(symbol)
      print("Found: {}".format(symbol))
    if td == 6: 
      td = 0
    else: 
      td +=1
    i+=1

  print("Writing symbols to symbols.csv...")
  with open('symbols.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(symbols)