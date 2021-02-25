import requests
from requests import get
from bs4 import BeautifulSoup
import csv

def ScrapeSymbols():
  print("Scraping all symbols from Nasdaq OMX C25...")
  url = 'http://www.nasdaqomxnordic.com/shares/listed-companies/copenhagen'

  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}
  results = requests.get(url, headers=headers)

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