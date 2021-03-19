#Dictionary
#Mulai
#Note DD = Data Diri
print("Data diri saya :")
DD= {"Nama":"Ivanindra",
     "Hobby1":"Dengerin musik",
     "Hobby2":"Bikin musik",
     "Hobby3":"Main game",
     "Sosial media1":"Fb = ivanpratama",
     "Sosial media2":"Ig = @ivan_pratama1",
     "Sosial media3":"twitter = ivanpratama110",
     "Lagu kesukaan1":"Giorgio by Moroder - Daft Punk",
     "Lagu kesukaan2":"Hold the line - Avicii",
     "Lagu kesukaan3":"Sad song - Illenium",
     "Makanan Favorit1":"Nasi padang",
     "Makanan Favorit2":"Ramen",
     "Makanan Favorit3":"Sashimi"}
#sebenernya masih banyak lagu kesukaan, tapi nanti terlalu banyak wkw

print (DD)
print(type(DD))

#Ubah salah satu dari hobi dan sosial media kalian, hapus lah 2 makanan favorit kalian, dan tambahkan lah 1 hoby kalian

#Mengubah hobby
print("Saya akan mengubah salah satu hobby, akan menjadi :")
DD['Hobby2']= 'Bersepeda'
print(DD)

#Mengubah Sosial Media
DD['Sosial media2']= "Ig @Disuru_Ganti_Akun"
print(DD)
#Menghapus 2 makanan favorit
del DD['Makanan Favorit1']
del DD['Makanan Favorit2']
print(DD)
#Menambah 1 Hobby lagi
DD['Hobby2'] = "Membaca buku"
print(DD)

#Selesai
input("Klik enter untuk kembali")
#Mohon maaf apabila ada kesalahan, dikarenakan manusia tempatnya salah.



