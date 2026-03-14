import threading

import threading

def task():
    print("Thread is running")

t = threading.Thread(target=task)

t.start()


import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in ["A", "B", "C", "D"]:
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()



t1.join()
t2.join()




t1.start()
t2.start()

t1.join()
t2.join()

print("Program finished")






t1.start()
t2.start()

t1.join()
t2.join()

print("Program finished")