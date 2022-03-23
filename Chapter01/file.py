f = open ('test.txt', 'w') #membaca file di luar
f.write ('first line of file \n') #menulis ke dalam file

f.write ('second line of file \n') #menulis ke dalam file

f.close()#keluarkan file nya
f = open ('test.txt') #buka file
content = f.read()
print (content) #render content yang ada di dalam file nya

f.close()
