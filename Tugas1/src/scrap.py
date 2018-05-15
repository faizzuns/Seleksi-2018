#import the library used to query a website
# from urllib.request import urlopen
import urllib.request
import json
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#specify the url
wiki = "https://id.wikipedia.org/wiki/Indonesia_pada_Asian_Games"
hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

def getPage(endpoint):
    #Query the website and return the html to the variable 'page'
    r = urllib.request.Request(wiki + endpoint, headers= hdr)
    page = urllib.request.urlopen(r)

    #Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def searchMendallion(table):
    #data mendali tiap tahun
    mendallion_stats = table[0].findAll("tr")

    data_json = {}
    data_json['total_emas'] = int(mendallion_stats[len(mendallion_stats) - 1].findAll("td")[2].text)
    data_json['total_perak'] = int(mendallion_stats[len(mendallion_stats) - 1].findAll("td")[3].text)
    data_json['total_perunggu'] = int(mendallion_stats[len(mendallion_stats) - 1].findAll("td")[4].text)
    data_json['count'] = len(mendallion_stats) - 2

    data_json['data'] = []

    for i in range (1, len(mendallion_stats)-1):
        isi = mendallion_stats[i].findAll("td")
        dt = {}
        dt['ajang'] = isi[0].text
        dt['peringkat'] = int(isi[1].text)
        dt['emas'] = int(isi[2].text)
        dt['perak'] = int(isi[3].text)
        dt['perunggu'] = int(isi[4].text)
        dt['total'] = int(isi[5].text)
        data_json['data'].append(dt)

    with open('../data/data.json', "w+") as outfile:
        outfile.write(json.dumps(data_json, indent=2))

def searchSportsMedal(table):
    data_sports = table[1].findAll('tr')

    data_json = {}
    data_json['total_emas'] = int(data_sports[len(data_sports) - 1].findAll("td")[2].text)
    data_json['total_perak'] = int(data_sports[len(data_sports) - 1].findAll("td")[3].text)
    data_json['total_perunggu'] = int(data_sports[len(data_sports) - 1].findAll("td")[4].text)
    data_json['count'] = len(data_sports) - 2

    data_json['data'] = []

    for i in range (1, len(data_sports)-1):
        isi = data_sports[i].findAll("td")
        dt = {}
        dt['cabang'] = isi[1].text
        dt['emas'] = int(isi[2].text)
        dt['perak'] = int(isi[3].text)
        dt['perunggu'] = int(isi[4].text)
        dt['total'] = int(isi[5].text)
        data_json['data'].append(dt)

    with open('../data/data_sports.json', "w+") as outfile:
        outfile.write(json.dumps(data_json, indent=2))

def searchBadminton(table):
    #data pemain bulu tangkis
    data_bulu_tangkis = table[3].findAll("tr")

    data_json = {}

    data_json['data'] = []

    dt = {}

    for i in range(1, len(data_bulu_tangkis)-1):
        isi = data_bulu_tangkis[i].findAll("td")

        tipe = 0
        if 'Ganda' in isi[2].text:
            tipe = 1

        if tipe == 0:
            name = isi[1].text

            #name
            if name not in dt:
                dt[name] = {}
                if 'putra' in isi[2].text:
                    dt[name]['gender'] = 'Pria'
                else:
                    dt[name]['gender'] = 'Wanita'
                dt[name]['emas'] = 0
                dt[name]['perak'] = 0
                dt[name]['perunggu'] = 0

            #medali
            if 'Emas' in isi[0].text:
                dt[name]['emas'] += 1
            elif 'Perak' in isi[0].text:
                dt[name]['perak'] += 1
            elif 'Perunggu' in isi[0].text:
                dt[name]['perunggu'] += 1
        else:
            names = isi[1].findAll('a')

            name1 = names[0].text
            name2 = names[1].text

            if 'Christian Hadinata' in name1:
                temp = name1
                name1 = name2
                name2 = temp

            #name1
            if name1 not in dt:
                dt[name1] = {}
                if 'putra' in isi[2].text:
                    dt[name1]['gender'] = 'Pria'
                elif 'putri' in isi[2].text:
                    dt[name1]['gender'] = 'Wanita'
                else:
                    dt[name1]['gender'] = 'Wanita'
                dt[name1]['emas'] = 0
                dt[name1]['perak'] = 0
                dt[name1]['perunggu'] = 0

            #name2
            if name2 not in dt:
                dt[name2] = {}
                if 'putra' in isi[2].text:
                    dt[name2]['gender'] = 'Pria'
                elif 'putri' in isi[2].text:
                    dt[name2]['gender'] = 'Wanita'
                else:
                    dt[name2]['gender'] = 'Pria'
                dt[name2]['emas'] = 0
                dt[name2]['perak'] = 0
                dt[name2]['perunggu'] = 0

            #medali
            if 'Emas' in isi[0].text:
                dt[name1]['emas'] += 1
                dt[name2]['emas'] += 1
            elif 'Perak' in isi[0].text:
                dt[name1]['perak'] += 1
                dt[name2]['perak'] += 1
            elif 'Perunggu' in isi[0].text:
                dt[name1]['perunggu'] += 1
                dt[name2]['perunggu'] += 1

    dt.pop('Tim putra', None)
    dt.pop('Tim putri', None)

    for key in dt.keys():
        data = {}
        data['name'] = key
        data['gender'] = dt[key]['gender']
        data['emas'] = dt[key]['emas']
        data['perak'] = dt[key]['perak']
        data['perunggu'] = dt[key]['perunggu']
        data_json['data'].append(data)

    with open('../data/data_bulu_tangkis.json', "w+") as outfile:
        outfile.write(json.dumps(data_json, indent=2))

if __name__ == "__main__":
    soup = getPage("")

    table = soup.findAll("table", {"class" : "wikitable sortable"})

    searchMendallion(table)

    searchSportsMedal(table)

    searchBadminton(table)
