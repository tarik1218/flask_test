import config
import psycopg2
from classlar import *
from main import *
from flask import Flask, render_template, request, \
    redirect, url_for

app = Flask(__name__)


kullanıcı=Kullanıcı()
sinav=Sınav()


@app.route("/")
def login():
    #eğer "çıkış yap" butonuna basıldıysa buraya girileceğinden kullanıcı sıfırlanıyor
    kullanıcı=Kullanıcı() #kullanıcı sıfırlandı

    #direk başlangıçta ise burası açılır "çıkış yap" a basılmadığı zaman veya hata ekranından sonra logine geri dön için
    return render_template('login_ekrani.html')

@app.route("/giris", methods=['POST', 'GET']) # yeni sayfa 2
def giris():
    if request.method == 'POST':
        girilen_id = str(request.form.get('id'))
        girilen_sifre = request.form.get('sifre')
        veritabanından_kullanıcı=kullanici_getir(girilen_id)
        if (len(veritabanından_kullanıcı)==0) or (len(veritabanından_kullanıcı)!=0 and veritabanından_kullanıcı[1]!=girilen_sifre):
            return render_template('hata_ekrani.html')
        else:
            kullanıcı.idsi=veritabanından_kullanıcı[0]
            kullanıcı.ad_soyadi = veritabanından_kullanıcı[2]
            kullanıcı.ogretmen_mi = veritabanından_kullanıcı[3]
            if kullanıcı.ogretmen_mi==True:
                return render_template('ogretmen_ekrani.html', isim=kullanıcı.ad_soyadi)
            else:
                return render_template('ogrenci_ekrani.html', isim=kullanıcı.ad_soyadi)

    #post değilse buraya girer, profile geri dön içindir.
    if kullanıcı.ogretmen_mi == True:
        return render_template('ogretmen_ekrani.html', isim=kullanıcı.ad_soyadi)
    else:
        return render_template('ogrenci_ekrani.html', isim=kullanıcı.ad_soyadi)



@app.route("/sinav_olustur", methods=['POST', 'GET'])
def sinav_olustur():
    if request.method == 'POST':
        return render_template('sinav_olusturma_sayfasi.html')

@app.route("/sinavlarim", methods=['POST', 'GET'])
def sinavlarim():
    if request.method == 'POST':
        return render_template('sinavlarim_sayfasi.html', rows=sinavları_listele())

@app.route("/sınav_olusturuldu", methods=['POST', 'GET'])
def sinav_olusturuldu():
    if request.method == 'POST':
        sinav_ekle(request.form.get('sinav_adi'),kullanıcı.idsi,request.form.get('baslangic_tarihi'),request.form.get('bitis_tarihi'),request.form.get('soru_1'),request.form.get('soru_1_a'),request.form.get('soru_1_b'),request.form.get('soru_1_c'),request.form.get('soru_1_d'),request.form.get('soru_1_e'),request.form.get('soru_2'),request.form.get('soru_2_a'),request.form.get('soru_2_b'),request.form.get('soru_2_c'),request.form.get('soru_2_d'),request.form.get('soru_2_e'),request.form.get('soru_3'),request.form.get('soru_3_a'),request.form.get('soru_3_b'),request.form.get('soru_3_c'),request.form.get('soru_3_d'),request.form.get('soru_3_e'))
        return render_template('sinav_olusturuldu_ekrani.html')

@app.route("/ara", methods=['POST', 'GET'])
def ara():
    if request.method == 'POST':
        link=request.form.get('link')
        veritabanından_sınav = sinav_getir(link)


        sinav.adi = veritabanından_sınav[1]

        sinav.soru_1 = veritabanından_sınav[5]
        sinav.soru_1_a = veritabanından_sınav[6]
        sinav.soru_1_b = veritabanından_sınav[7]
        sinav.soru_1_c = veritabanından_sınav[8]
        sinav.soru_1_d = veritabanından_sınav[9]
        sinav.soru_1_e = veritabanından_sınav[10]

        sinav.soru_2 = veritabanından_sınav[11]
        sinav.soru_2_a = veritabanından_sınav[12]
        sinav.soru_2_b = veritabanından_sınav[13]
        sinav.soru_2_c = veritabanından_sınav[14]
        sinav.soru_2_d = veritabanından_sınav[15]
        sinav.soru_2_e = veritabanından_sınav[16]

        sinav.soru_3 = veritabanından_sınav[17]
        sinav.soru_3_a = veritabanından_sınav[18]
        sinav.soru_3_b = veritabanından_sınav[19]
        sinav.soru_3_c = veritabanından_sınav[20]
        sinav.soru_3_d = veritabanından_sınav[21]
        sinav.soru_3_e = veritabanından_sınav[22]

        return redirect(url_for('sinava_giris',sinav_linki=link))

@app.route("/<sinav_linki>", methods=['POST', 'GET'])
def sinava_giris(sinav_linki):

    return render_template('sinava_giris_sayfasi.html', sinav_adi=sinav.adi,soru_1=sinav.soru_1,soru_1_aa=sinav.soru_1_a,soru_1_bb=sinav.soru_1_b,soru_1_cc=sinav.soru_1_c,soru_1_dd=sinav.soru_1_d,soru_1_ee=sinav.soru_1_e,soru_2=sinav.soru_2,soru_2_aa=sinav.soru_2_a,soru_2_bb=sinav.soru_2_b,soru_2_cc=sinav.soru_2_c,soru_2_dd=sinav.soru_2_d,soru_2_ee=sinav.soru_2_e,soru_3=sinav.soru_3,soru_3_aa=sinav.soru_3_a,soru_3_bb=sinav.soru_3_b,soru_3_cc=sinav.soru_3_c,soru_3_dd=sinav.soru_3_d,soru_3_ee=sinav.soru_3_e)