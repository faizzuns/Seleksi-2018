<h1 align="center">
  <br>
  Tugas 1 Seleksi Warga Basdat 2018
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

### Description
Program ini melakukan data scrapping ke web https://id.wikipedia.org/wiki/Indonesia_pada_Asian_Games dan pada web itu
saya mengambil data data mendali tiap Asian Games, Data mendali tiap cabang, dan nama nama atlet bulu tangkis berikut mendalinya

### Specifications

1. Lakukan data scraping dari sebuah laman web untuk memeroleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan data scraping pada spreadsheet berikut: [Topik Data Scraping](http://bit.ly/TopikDataScraping). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal 10 Mei 2018 pukul 20.00 WIB

3. Dalam mengerjakan tugas 1, calon warga basdat terlebih dahulu melakukan fork project github pada link berikut: https://github.com/wargabasdat/Seleksi-2018/tree/master/Tugas1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan pull request dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada repository tersebut, calon warga basdat harus mengumpulkan file script dan json hasil data scraping. Repository terdiri dari folder src dan data dimana folder src berisi file script/kode yang __WELL DOCUMENTED dan CLEAN CODE__ sedangkan folder data berisi file json hasil scraper.

5. Peserta juga diminta untuk membuat Makefile sesuai template yang disediakan, sehingga program dengan gampang di-_build_, di-_run_, dan di-_clean_

``` Makefile
all: clean build run

clean: # remove data and binary folder

build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary

```

6. Deadline pengumpulan tugas adalah __15 Mei 2018 Pukul 23.59__

7. Tugas 1 akan didemokan oleh masing-masing calon warga basdat

8. Demo tugas mencakup keseluruhan proses data scraping hingga memeroleh data sesuai dengan yang dikumpulkan pada Tugas 1

9. Hasil data scraping ini nantinya akan digunakan sebagai bahan tugas analisis dan visualisasi data

10. Sebagai referensi untuk mengenal data scraping, asisten menyediakan dokumen "Short Guidance To Data Scraping" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance)

11. Tambahkan juga gitignore pada file atau folder yang tidak perlu di upload, __NB : BINARY TIDAK DIUPLOAD__

12. JSON harus dinormalisasi dan harus di-_preprocessing_
```
Preprocessing contohnya :
- Cleaning
- Parsing
- Transformation
- dan lainnya
```

13. Berikan README yang __WELL DOCUMENTED__ dengan cara __override__ file README.md ini. README harus memuat minimal konten :
```
- Description
- Specification
- How to use
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```

### How to use
1. Open terminal
2. Change the dir to where you save the file
3. Run this program with command -> python scrap.py

Or you can run the Makefile with command "make" if you using Linux environment.

### JSON Structure
This program will build three JSON file :

1. data.json
  -total_emas
    merupakan jumlah mendali emas yang dimiliki Indonesia selama Asian Games
  -total_perak
    merupakan jumlah mendali perak yang dimiliki Indonesia selama Asian Games
  -total_perunggu
    merupakan jumlah mendali perunggu yang dimiliki Indonesia selama Asian Games
  -count
    jumlah data Asian Games yang diikuti oleh Indonesia
  -data
    Merupakan sebuah array yang berisi data-data Indonesia di tiap Asian Games

2. data_sports.json
-total_emas
  merupakan jumlah mendali emas yang dimiliki Indonesia selama Asian Games
-total_perak
  merupakan jumlah mendali perak yang dimiliki Indonesia selama Asian Games
-total_perunggu
  merupakan jumlah mendali perunggu yang dimiliki Indonesia selama Asian Games
-count
  jumlah data Asian Games yang diikuti oleh Indonesia
-data
  Merupakan sebuah array yang berisi data-data Indonesia di tiap Asian Games

3. data_bulu_tangkis.json
  -name
    nama dari atlet bulu tangkis
  -gender
    gender dari atlet bulu tangkis
  -emas
    jumlah mendali emas yang telah ia dapatkan
  -perak
    jumlah mendali perak yang telah ia dapatkan
  -perunggu
    jumlah mendali perunggu yang telah ia dapatkan


### Screenshots
![alt_text](https://github.com/faizzuns/Seleksi-2018/blob/master/Tugas1/screenshots/data.jpg)

![alt_text](https://github.com/faizzuns/Seleksi-2018/blob/master/Tugas1/screenshots/data_sports.jpg)

![alt_text](https://github.com/faizzuns/Seleksi-2018/blob/master/Tugas1/screenshots/data_bulu_tangkis.jpg)

### Reference
Library that I used:
1. BeautifulSoup4 for html parser
2. json for save the result into .json file
3. urllib.request to get the html script from the url we want

### Author
Nama    : <b>Ahmad Faiz Sahupala</b>
Email   : faiz.sahupala29@gmail.com

<h1 align="center">
  <br>
  Selamat BerEksplorasi!
  <br>
  <br>
</h1>

<p align="center">
  <br>
  Basdat Industries - Lab Basdat 2018
  <br>
  <br>
</p>
