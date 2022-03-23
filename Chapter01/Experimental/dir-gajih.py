# Flow Control

# Variable int input
waktu1 = int(input("Mulai kerja: "))
waktu2 = int(input("Selesai kerja: "))
waktu3 = int(input("Waktu lembur: "))

# Penkondisian ketika di input
if waktu1 > 0:
    print('Waktunya kerja')
    if waktu2-waktu1 == 7:
        print("Jam Kerja selesai")
    elif waktu2-waktu1 > 7:
        print("Waktunya lembur")
        if (waktu2-waktu1)+(waktu3-waktu2) >= 7:
            print("Waktunya lembur + bonus")
else:
    print("Anda kurang beruntung tidak lembur")
    

# Array

# Variabel array
genap = [2, 4, 6, 8, 10]
ganjil = [1, 3, 5, 7, 9]

nap = 0
jil = 0

# Buat looping for menggunakanvariable dari array  yang udah dibuat
for val in genap:
    nap = nap+val
    for val in ganjil:
        jil = jil+val

print("Ini adalah bilangan Genap", nap )
print("Ini adalah bilangan Ganjil", jil )