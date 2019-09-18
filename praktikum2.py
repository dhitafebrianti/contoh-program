class Pegawai:
  def __init__(self, nama, gaji=0):
    self.nama = nama
    self.gaji = gaji
  def tunjangan(self, persen):
    self.gaji = self.gaji + (self.gaji* persen)
  def kerja(self):
    print(self.nama, "Pekerjaannya")
  def __repr__(self, nama) :
    return "<Pegawai:\n nama = %s, gaji = %s" %(self.nama, self.gaji)
class Koki(Pegawai):
  def __init__(self, nama):
    Pegawai. __init__(self, nama, 100000)
  def Kerja(self):
    print(self.nama, "membuat makanan")
class Pelayanan(Pegawai):
  def __init(self, nama):
    Pegawai. __init__(self, nama, 50000)
  def Kerja(self):
    print(self.nama, "melayani costumer")
class PizzaRobot(Koki):
  def __init__(self, nama):
    Koki. __init__(self, nama)
  def Kerja(self):
    print(self.nama, "membuat pizza")
    
if __name__ == "__main__":
  agus = PizzaRobot ("agus")
  print(agus)
  agus.kerja()
  agus.tunjangan(0.20)
  print(agus)
  print
  
  for kelas in Pegawai, Koki, Pelayan, PizzaRobot:
    objek = kelas(kelas. __name__)
    objek.kerja()
   
   
