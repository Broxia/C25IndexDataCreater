import NasdaqSymbolScraper, NasdaqScraper
import pandas as pd
import numpy as np
import csv
from os import listdir
from os.path import isfile, join

NasdaqSymbolScraper.ScrapeSymbols()
NasdaqScraper.DownloadFiles()
path = './Data/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print("Generating data.csv...")
d = {'Date': []}
firstFile = True
for f in onlyfiles:
  with open(path + f, 'r') as file:
      print("Adding data from {}...".format(f))
      dl = list(csv.reader(file))
      if('404 Not Found' in dl[0][0]):
        print("Data not found for {}".format(f))
        continue
      symbol = str(f).replace(".CO.csv", "")
      symbol.replace("-", " ")
      d[symbol] = []
      for row in dl:
        if('Date' in row[0]):
          continue
        d[symbol].append(row[4])

        if firstFile:
          d['Date'].append(row[0])

  firstFile = False

lenShouldBe = len(d['Date'])
for col in d:
  if len(d[col]) != lenShouldBe:
    i = 0
    while i < lenShouldBe - len(d[col]):
      d[col].insert(0, 'NaN')

df = pd.DataFrame.from_dict(d)
df.set_index('Date', inplace=True)
df.to_csv('data.csv')