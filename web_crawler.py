from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request
import chardet

for a in range(1, 13):
    if a < 10:
        url = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=2&ID=305091285502140&BGNDATE=20150%s01&ENDDATE=20201231&KAWABOU=NO' % a
    else:
        url = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=2&ID=305091285502140&BGNDATE=2015%s01&ENDDATE=20201231&KAWABOU=NO' % a
    res = requests.get(url)
    # rawdata = urllib.request.urlopen(url).read()
    # print(chardet.detect(rawdata))
    res.encoding = 'EUC-JP'
    soup = BeautifulSoup(res.text, 'lxml')  # , from_encoding = chardet.detect(rawdata))
    # print(soup.original_encoding)
    tables = soup.select('table')
    df_list = []
    for table in tables:
        df_list.append(pd.concat(pd.read_html(table.prettify())))
    df = pd.concat(df_list)
    df.to_excel('mino_2015_%a.xlsx' % a)
    print(a)
