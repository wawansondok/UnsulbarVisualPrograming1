class Hewan:

     def __init__(self, nama, warna):
         self.nama = nama     
         self.warna = warna

class Kucing(Hewan):
     def makan(self):
         print("Kucing sedang makan")

binatang = Kucing("catty", "Balmon")
 
print(binatang.nama)
binatang.makan()


print(binatang.warna)
binatang.makan()
