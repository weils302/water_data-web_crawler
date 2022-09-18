# 一年間の時刻流量月表ダウンロード

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import urllib.request
import chardet

spot_ID = ''
spot_name = ''  # 保存するファイル名に書く観測所の名前
year = ''
present_year = datetime.datetime.now().year

for a in range(1, 13):
    if a < 10:
        url = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=6&ID=%s&BGNDATE=%s0%s01&ENDDATE=%s1231'\
        '&KAWABOU=NO' % (spot_ID, year, a, present_year)
    else:
        url = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=6&ID=%s&BGNDATE=%s%s01&ENDDATE=%s1231'\
        '&KAWABOU=NO' % (spot_ID, year, a, present_year)
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
    df.to_excel('%s_%s_%a_流量.xlsx' % (spot_name, year, a))
    print(a)
