class Mahasiswa:
  def __init__(self, merk):
    self.__merk = merk

  def tampilkan_merk(self):
    print(f'Nama: {self.__merk}')

jip = Mahasiswa('Wawan sondok - D0219414')
jip.tampilkan_merk()