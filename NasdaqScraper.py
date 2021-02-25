import requests
from requests import get
import csv, time, os, calendar


def DownloadFiles():
  print("Downloading historical data from Yahoo...")
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

  stocks = []
  with open('symbols.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
          stocks.append(row)
  stocks = stocks[0]
  
  path = './Data/'
  try:
    os.mkdir(path)
  except OSError:
    print ("Creation of the directory %s failed - Most likely exists" % path)

  for symbol in stocks:
    print("Downloading data for {}".format(symbol))


    
    fromTime = calendar.timegm(time.strptime('Jan 1, 2010 @ 0:0:0 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
    toTime = calendar.timegm(time.gmtime())
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true'.format(symbol, fromTime, toTime)
    results = requests.get(url, headers=headers, allow_redirects=True)

    open('{}.csv'.format(path+symbol), 'wb').write(results.content)

    time.sleep(1) #To not ddos the site
