
from databasem import db, imlec
from random_link_generator import *


#print( db.get_dsn_parameters() )


def kullanıcı_ekle():
    #Öğretmen_1
    komut="INSERT INTO Kullanicilar(id,sifre,ad_soyad,ogretmen_mi) VALUES('123456','hocasifre','Yar. Doc. Fahri Özkurt', 'True');"
    imlec.execute(komut)
    db.commit()

    #Öğretmen_2
    komut = "INSERT INTO Kullanicilar(id,sifre,ad_soyad,ogretmen_mi) VALUES('654321','hocasifre','Asistan Şahin Kaynakçı', 'True');"
    imlec.execute(komut)
    db.commit()

    #Öğrenci_1
    komut = "INSERT INTO Kullanicilar(id,sifre,ad_soyad,ogretmen_mi) VALUES('987654','ogrsifre','Oğuzhan Görmüş', 'False');"
    imlec.execute(komut)
    db.commit()

    # Öğrenci_2
    komut = "INSERT INTO Kullanicilar(id,sifre,ad_soyad,ogretmen_mi) VALUES('456789','ogrsifre','Şehmuz Kovucu', 'False');"
    imlec.execute(komut)
    db.commit()

    # Öğrenci_3
    komut = "INSERT INTO Kullanicilar(id,sifre,ad_soyad,ogretmen_mi) VALUES('555555','ogrsifre','Süleyman Karabahtlı', 'False');"
    imlec.execute(komut)
    db.commit()


#kullanıcı_ekle()




#---------------------------------SINAVLA İLGİLİ İŞLEMLER----------------------------------

def sinavlar_tablosu_olustur():
    komut = """ CREATE TABLE Sinavlar(
                            url TEXT PRIMARY KEY,
                            sinav_adi TEXT NOT NULL,
                            ogretmen_id INTEGER NOT NULL,
                            baslangic_tarihi TEXT NOT NULL,
                            bitis_tarihi TEXT NOT NULL,
                            
                            soru_1 TEXT NOT NULL,
                            soru_1_a TEXT NOT NULL,
                            soru_1_b TEXT NOT NULL,
                            soru_1_c TEXT NOT NULL,
                            soru_1_d TEXT NOT NULL,
                            soru_1_e TEXT NOT NULL,
                            
                            soru_2 TEXT NOT NULL,
                            soru_2_a TEXT NOT NULL,
                            soru_2_b TEXT NOT NULL,
                            soru_2_c TEXT NOT NULL,
                            soru_2_d TEXT NOT NULL,
                            soru_2_e TEXT NOT NULL,
                            
                            soru_3 TEXT NOT NULL,
                            soru_3_a TEXT NOT NULL,
                            soru_3_b TEXT NOT NULL,
                            soru_3_c TEXT NOT NULL,
                            soru_3_d TEXT NOT NULL,
                            soru_3_e TEXT NOT NULL
                            );
                            """
    imlec.execute(komut)
    db.commit()


def sinav_ekle(sinav_adi, ogretmen_id, baslangic_tarihi, bitis_tarihi, soru_1, soru_1_a, soru_1_b, soru_1_c, soru_1_d,
               soru_1_e, soru_2, soru_2_a, soru_2_b, soru_2_c, soru_2_d, soru_2_e, soru_3, soru_3_a, soru_3_b, soru_3_c,
               soru_3_d, soru_3_e):
    url = random_link()

    url = "'" + str(url) + "'"
    sinav_adi = "'" + str(sinav_adi) + "'"
    ogretmen_id = "'" + str(ogretmen_id) + "'"
    baslangic_tarihi = "'" + str(baslangic_tarihi) + "'"
    bitis_tarihi = "'" + str(bitis_tarihi) + "'"

    soru_1 = "'" + str(soru_1) + "'"
    soru_1_a = "'" + str(soru_1_a) + "'"
    soru_1_b = "'" + str(soru_1_b) + "'"
    soru_1_c = "'" + str(soru_1_c) + "'"
    soru_1_d = "'" + str(soru_1_d) + "'"
    soru_1_e = "'" + str(soru_1_e) + "'"

    soru_2 = "'" + str(soru_2) + "'"
    soru_2_a = "'" + str(soru_2_a) + "'"
    soru_2_b = "'" + str(soru_2_b) + "'"
    soru_2_c = "'" + str(soru_2_c) + "'"
    soru_2_d = "'" + str(soru_2_d) + "'"
    soru_2_e = "'" + str(soru_2_e) + "'"

    soru_3 = "'" + str(soru_3) + "'"
    soru_3_a = "'" + str(soru_3_a) + "'"
    soru_3_b = "'" + str(soru_3_b) + "'"
    soru_3_c = "'" + str(soru_3_c) + "'"
    soru_3_d = "'" + str(soru_3_d) + "'"
    soru_3_e = "'" + str(soru_3_e) + "'"

    komut = "INSERT INTO Sinavlar(url,sinav_adi,ogretmen_id,baslangic_tarihi,bitis_tarihi,soru_1,soru_1_a,soru_1_b,soru_1_c,soru_1_d,soru_1_e,soru_2,soru_2_a,soru_2_b,soru_2_c,soru_2_d,soru_2_e,soru_3,soru_3_a,soru_3_b,soru_3_c,soru_3_d,soru_3_e) VALUES(" + url + "," + sinav_adi + "," + ogretmen_id + "," + baslangic_tarihi + "," + bitis_tarihi + "," + soru_1 + "," + soru_1_a + "," + soru_1_b + "," + soru_1_c + "," + soru_1_d + "," + soru_1_e + "," + soru_2 + ","+ soru_2_a + "," + soru_2_b + "," + soru_2_c + "," + soru_2_d + "," + soru_2_e + "," + soru_3 + "," + soru_3_a + "," + soru_3_b + "," + soru_3_c + "," + soru_3_d + "," + soru_3_e + ");"
    imlec.execute(komut)
    db.commit()


def sinav_getir(url):
    url = "'" + str(url) + "'"

    komut = "SELECT * FROM Sinavlar WHERE url=" + url + ";"
    imlec.execute(komut)
    sinav = imlec.fetchall()
    return sinav[0]  # sınavı satır olarak getirir tüm nitelikleri ile


def sinavi_olusturanin_adini_getir(olusturan_id):
    olusturan_id = "'" + str(olusturan_id) + "'"

    komut = "SELECT ad_soyad FROM Kullanicilar WHERE id=" + olusturan_id + ";"
    imlec.execute(komut)
    gelen_veri = imlec.fetchall()[0][0]
    return gelen_veri

#üstteki fonksiyon alttaki fonksiyon içindir.
def sinavları_listele():
    komut = "SELECT * FROM Sinavlar;"
    imlec.execute(komut)
    rows = imlec.fetchall()
    for row in rows:
        yield {"sinav_adi": str(row[1]), "yayinlayan": str(sinavi_olusturanin_adini_getir(row[2])),
               "baslangic_tarihi": str(row[3]), "bitis_tarihi": str(row[4]), "linki": str(row[0])}



#---------------------------------KULLANICI İLE İLGİLİ İŞLEMLER----------------------------------


def kullanıcılar_tablosu_olustur():
    komut = """ CREATE TABLE Kullanicilar(
                    id TEXT PRIMARY KEY,
                    sifre TEXT NOT NULL,
                    ad_soyad TEXT NOT NULL,
                    ogretmen_mi Boolean NOT NULL
                    );
                    """
    imlec.execute(komut)
    db.commit()

def kullanici_ekle(id,sifre,ad_soyad,ogretmen_mi):
    id= "'"+str(id)+"'"
    sifre = "'" + str(sifre) + "'"
    ad_soyad = "'" + str(ad_soyad) + "'"
    ogretmen_mi = "'" + str(ogretmen_mi) + "'"

    komut = "INSERT INTO Kullanicilar(id,sifre,ad_soyad,ogretmen_mi) VALUES("+id+","+sifre+","+ad_soyad+", "+ogretmen_mi+");"
    imlec.execute(komut)
    db.commit()

def kullanıcı_sil(id):
    id="'"+str(id)+"'"

    komut="DELETE FROM Kullanicilar WHERE id="+id+";"
    imlec.execute(komut)
    db.commit()

def kullanici_getir(id):
    id="'"+str(id)+"'"

    komut = "SELECT * FROM Kullanicilar WHERE id=" + id + ";"
    imlec.execute(komut)
    kullanıcı = imlec.fetchall()
    if len(kullanıcı)==0:#kullanıcı sorgusu boş geldi ise
        return []
    else:
        return kullanıcı[0] #kullanıcıyı satır olarak getirir tüm nitelikleri ile

#kullanıcılar_tablosu_olustur()
#sinavlar_tablosu_olustur()
#kullanıcı_ekle()