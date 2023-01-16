class Mahasiswa:
    def __init__ (self):
        self.__nama = "Bagus"
 
    #memberi tahu bahwa nama adalah property dari objek
    @property
    def nama(self):
        pass
     
    #memeberikan fungsi getter pada property nama
    @nama.getter
    def nama(self):
        return self.__nama
 
    #memeberikan fungsi setter pada property nama
    @nama.setter
    def nama(self,nama):
        self.__nama = nama
     
 
 
m = Mahasiswa()
m.nama = "BAGOES ABIYYU AZHAR"
print(m.nama)