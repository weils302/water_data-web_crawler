水文水質データベース web crawler
=

[国土交通省水文水質データベース](http://www1.river.go.jp)から指定された観測所の一年間の時刻水位、流量及び雨量月表をexcelファイルにダウンロードするプログラムです。

## 使用方法

### データダウンロード
 * *web_crawler_water level.py*  
水位データダウンロード用
 * *web_crawler_discharge.py*  
流量データダウンロード用
 * *web_crawler_precipitation.py*  
雨量データダウンロード用

line 10 ```spot_ID``` で観測所記号を入力  
line 11 ```spot_name``` で出力ファイル名に書く観測所名を入力  
line 12 ```year``` でダウンロードする年を入力


### 二つの観測所のデータをCSVファイルに合併（研究解析用）
***閏年データに未対応です。***
* *excel to csv.py*  
line 8 ```input_file_name1```と line 9 ```input_file_name2```にダウンロードした二つの観測所データからそれぞれいずれか一つのファイル名を入力する。  
line 10 ```spot1_path```と line 11 ```spot2_path```に入力ファイルのdirectoryを入力する。
