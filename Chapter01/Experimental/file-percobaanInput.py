#Percobaan implementasi Input ke dalam file
f = open ('input_file.txt', 'w') #membaca file di luar
nama = input ("Masukan Nama :")
npm = input("Masukan NPM : ")
kelas = input("Masukan Kelas : ")
f.write (nama) #menulis ke dalam file
f.write (npm) 
f.write (kelas)
f.close()#keluarkan file nya
f = open ('input_file.txt') #buka file
content = f.read()
print (content) #render content yang ada di dalam file nya

f.close()
