from threading import Thread
import time
import os
#Disediakan class thread control yang didalamnya ada inisialisasi fungsi, name dan threadnya
class MyThreadClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self): #fungsi yang akan mengembalikan PID dan nama dari thread itu sendiri(pada line16 maupun 17)
       print("ID of process running {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main(): #proses yang merjalan saat menjalankan skript
    from random import randint
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
  
    # Thread Running
    thread1.start()
    thread2.start()


    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("End")


if __name__ == "__main__":
    main()

    


