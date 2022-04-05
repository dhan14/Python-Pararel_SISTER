import threading
import time
''''
Ada 3 fungsi yakni fungsi A,B dan C
Fungsi ini akan melakukan running, jika proses memakan waktu lama akan masuk pada proses tunda /sleep
lalu jika selesai kembalikan nilainya
'''
def function_A():
    print (threading.currentThread().getName()+str('--> starting \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return

def function_B():
    print (threading.currentThread().getName()+str('--> starting \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return

def function_C():
    print (threading.currentThread().getName()+str('--> starting \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C',target=function_C) 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
