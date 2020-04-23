# Japan-Hourly-City-wise-Population-Change-Density-Dataset (Before & After COVID-19 Emergency Declaration)
# （CSV）緊急事態宣言前後における7都府県の人口変動分析
CSV file representation of population change data originally published as PDF

This repository is an independant effort to convert government published graph data originally in PDF to csv format, to allow utilization by analysis software. The data, [as publicly published by the government of Japan and NTT Docomo](https://corona.go.jp/toppage/pdf/area-transition/20200418_docomo.pdf), addresses population changes before and after the emergency declaration due to the COVID-19 outbreak.

Presently, the method used to convert graph images (inside the PDF) to CSV is to:
(1) Take a screenshot of plots
(2) Use photoshop to increase contrast and remove unneeded artifacts, thus making the algorithm's work easier. The can be found in '/input'
(3) Manually estimate origin and step points for both x and y axes, then store them in a csv file
(4) Running an image processing algorithm 'img2csv.py' to parse the images and extract the datapoints
(5) Saving the datapoints to '/csv'

The csv data for the following cities/areas were extracted and made available:
- Shibuya　渋谷
- Yokohama　横浜
- Chiba　千葉
- Funabashi　船橋
- Oomiya　大宮
- Umeda　梅田
- Nanba　難波
- Sannomiya　三ノ宮
- Tenjin　天神
