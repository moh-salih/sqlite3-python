import sqlite3


class DB:
    _conn = None
    
    def __init__(self):
        self._conn = sqlite3.connect('veritabani.db')
       
    def __del__(self):
        self._conn.commit()
        self._conn.close()

class DatabaseInitializer(DB):
    def __init__(self):
        super().__init__()
        self._conn.execute("CREATE TABLE IF NOT EXISTS tbl_sayilar(id INT NOT NULL, sayi INT NOT NULL)")

class Veritabani(DB):
    def __init__(self):
        super().__init__()

    def kaydet(self, index, sayi):
        self._conn.execute('INSERT INTO tbl_sayilar (id, sayi) VALUES ({}, {})'.format(index, sayi))
    
    def listele(self):
        return self._conn.execute('SELECT * FROM tbl_sayilar ORDER BY id')

def kullanciDanVeriAl():
    veritabani = Veritabani()
    while True:
        girilenSayilar = input('0 ile 50 arasinda sayilar giriniz: ').split()   
    
        if(len(girilenSayilar) == 0):
            break
    
        for index in range(len(girilenSayilar)):
            veritabani.kaydet(index, girilenSayilar[index])
        
def listele():
    veritabani = Veritabani()
    son_satir = -1
    for veri in veritabani.listele():
        if veri[0] != son_satir:
            print('\nSatir({}):\t'.format(veri[0]), end='')
            son_satir = veri[0]
        print(veri[1], end='\t')

def main():
    DatabaseInitializer()
    veritabani = Veritabani()
    kullanciDanVeriAl()
    listele()

if __name__:
    main()



