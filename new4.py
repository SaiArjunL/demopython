from threading import *
from time import *

class one(Thread):
    def run(self):
        for i in range(5):
            print("Sai")
            sleep(1)

class two(Thread):
    def run(self):
        for i in range(5):
            print("Arjun")
            sleep(1)

a = one()
b = two()

a.start()
sleep(0.2)
b.start()
a.join()
b.join()
print("Ladeela")
