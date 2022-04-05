import threading


def my_func(thread_number): #fungsi yang akan ditampilkan pada variabel t
    return print('my_func called by thread N°{}'.format(thread_number))


def main(): #Fungsi utama untuk running perintah yang akan dijalankan pada saat run script ini
    threads = []
    for i in range(10): #lakukan looping hingga range 10
        t = threading.Thread(target=my_func, args=(i,)) 
        threads.append(t) #munculkan isi dari variabel t yang akan mengembalikan nilai dari fungsi my_func dan argument 1 adalah angka yang ditampilkan dari hasil looping
        t.start() #running thread
        t.join() #mengirimkan pada blok sistem untuk masuk antrian

if __name__ == "__main__":
    main()
