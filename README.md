水文水質データベース web crawler
=

[国土交通省水文水質データベース](http://www1.river.go.jp)から指定された観測所の一年間の時刻水位、流量及び雨量月表をexcelファイルにダウンロードするプログラムです。

## 使用方法

 * *web_crawler_water level.py*  
水位データダウンロード用
 * *web_crawler_discharge.py*  
流量データダウンロード用
 * *web_crawler_precipitation.py*  
雨量データダウンロード用

line 10 ```spot_ID``` で観測所記号を入力  
line 11 ```spot_name``` で出力ファイル名に書く観測所名を入力  
line 12 ```year``` でダウンロードする年を入力


研究で使う水位データをダウンロードするためのプログラムです。国土交通省水文水質データベースに載せてあるデータは月ごとのデータです。まずはweb_crawler.pyで月ごとのデータを文字コード変換して、一つ一つのexcelファイルに保存する。次にexcel to csv_akutami-mino.pyでダウンロードした月ごとのデータを研究で使える年ごとのcsvファイルに変換します。研究で二つの場所の同じ時刻のデータが必要だったので、この.pyファイルではakutamiとminoという二つの観測点のデータを融合しました。Line 9, 10のディレクトリーを消しました。
