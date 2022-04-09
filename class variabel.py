class Mahasiswa:
  def __init__(self, nama):
    self.__nama = nama

  def tampilkan_nama(self):
    print(f'Nama: {self.__nama}')

Wawan= Mahasiswa('Wawan sondok - D0219414')
Wawan.tampilkan_nama()
