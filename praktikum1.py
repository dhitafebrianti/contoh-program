class Kotak(object):
  def __init__(self,p,l,t):
    self.panjang = p
    self.lebar = l
    self.tinggi = t
    
  def hitungVolume(self) :
    return self.panjang * self.lebar * \
           self.tinggi
   
  def cetakData(self):
    print("panjang\t:", self.panjang)
    print("lebar\t:", self.lebar)
    print("tinggi\t:", self.tinggi)
 
  def cetakVolume(self):
    print("volume\t= ", self.hitungVolume())
  
class kotakWarna(Kotak):
  def __init__(self, p, l, t, w):
    self.panjang = p
    self.lebar = l
    self.tinggi = t
    self.warna = w
  def cetakData(self):
    print("panjang\t: ", self.panjang)
    print("lebar\t:", self.lebar)
    print("tinggi\t:", self.tinggi)
    print("warna\t:", self.warna)

def main () :


  kotakwarna1 = kotakWarna(6,5,4, "merah")
  
  
  kotakwarna1.cetakData()
  kotakwarna1.cetakVolume()
  
if __name__ == "__main__":
  main()
