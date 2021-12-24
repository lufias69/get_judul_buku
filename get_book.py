# # keyowords = ["komputer dan internet", ]

# from bs4 import BeautifulSoup
# import requests
import pandas as pd
from urllib.request import urlopen
import json

buku_dict = dict()

k = list()
jumlah_keyword = input("Berapa Jumlah Keyword yang akan dimasukkan: ")
for i in range(int(jumlah_keyword)):
    input_ = input("input keyword "+str(i+1)+": ")
    k.append(input_)
print("")

nama_file = input("input nama file: ")
# nama_file = nama_file+".xlsx"

print("Processing ...")

# kata_kunci = input("Masukkan Kata Kunci Untuk Buku yang Dicari: ")
keywords = k
# keyoword = keyoword.replace(" ", "%20")
buku_dict = dict()
buku_dict ["link"] = list()
buku_dict ["description"] = list()
buku_dict ["thumbnail"] = list()
buku_dict ["authors"] = list()
buku_dict ["penerbit"] = list()
buku_dict ["tahun"] = list()
buku_dict ["judul"] = list()



for keyoword in keywords:
    print(keyoword, end="-")
    keyoword = keyoword.replace(" ", "%20")
    
    url = "https://www.gramedia.com/api/algolia/search/product/?q="+keyoword+"&page=1&per_page=40"

    response = urlopen(url)
    data_json = json.loads(response.read())

    x = 1
    for i in data_json:
        print(x, end=',')
        x+=1

        url_buku = "https://www.gramedia.com/api/products/v2/"+i['slug']
        buku_dict ["link"] .append(url_buku)
        response2 = urlopen(url_buku)
        buku_json = json.loads(response2.read())

        buku_dict ["judul"].append(buku_json['name'])
        buku_dict ["thumbnail"].append(buku_json['thumbnail'])
        buku_dict ["description"] .append(buku_json['description'])

        try:
            buku_dict ["authors"].append((i['authors'][0]['title']))
        except:
            print()
            buku_dict ["authors"].append('-')

        buku_dict ["tahun"].append((i['publishDate'].split('-')[0]))
        buku_dict ["penerbit"].append(buku_json['publisher'])
    
df = pd.DataFrame.from_dict(buku_dict)

df.to_excel(nama_file+".xlsx")
df
print("done !")