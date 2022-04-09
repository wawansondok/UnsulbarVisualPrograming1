class BuahMangga():
    __jml_mangga = 4 # private attribute
 
    def __init__(self, nama_buah):
        self.nama = nama_buah
 
    def harga_mangga(self,harga_mangga):
       hasil = self.__jml_mangga * harga_mangga
       return hasil
 
mangga = BuahMangga("Mangga Madu")
print(mangga.harga_mangga(3000))