#Penugasan no.1 Buatlah sebuah program list (gunakan kaidah pemograman list) untuk menyimpan nama teman-mu:

#Mulai

#Nama yang akan dimasukkan : Harry, Vika, Nauval, Iffa, Afnan, Ilham fairuz, Ilhum, Issa, Alam, Ojat
#list dimisalkan "TMN"
print("Teman yang akan berada di dalam list antara lain : ")
TMN = ["Harry", "Vika", "Nauval", "Iffa", "Afnan", "Ilham fairuz", "Ilhum", "Issa", "Alam", "Ojat"]
print(TMN)

#print list 4, 6, 7
print("Teman yang berada pada index 4,6,7 adalah :", TMN[4], TMN[6], TMN[7])


#Ganti nama yang ada pada index list 3, 5, 9
print("Nama pada index 3, 5, 9 akan diganti menjadi :")
TMN[3]="azahra"
TMN[6]="Zaman"
TMN[9]="Daroj"
print(TMN[3], TMN[5], TMN[9])
print("Teman yang ada pada index yang baru adalah :", TMN)

#Penambahan anggota baru
print("Akan ditambahkan anggota baru yaitu: Oktavianus, Nadiya")
TMN.append("Oktavianus")
TMN.append("Nadiya")
print("Hasil setelah beberapa teman baru ditambahkan adalah:", TMN)

#Pengulangan list
temananda = []
namatemananda = input("Tuliskan nama teman anda : ")
while namatemananda != '':
    temananda.append(namatemananda)
    namatemananda = input("Tuliskan nama teman anda, klik enter untuk kembali : ")
print("Teman-teman anda adalah", temananda)
print("\n")

#Menampilkan panjang
print = ("panjang list/total teman adalah :", len(TMN))


#Selesai
input("Tekan enter untuk kembali")

#Mohon maaf apabila ada kesalahan, dikarenakan manusia tempatnya salah.





 
