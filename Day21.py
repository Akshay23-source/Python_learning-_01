from multiprocessing import Process

def task():
    print("Process running")

p = Process(target=task)

p.start()
p.join()




from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in ["A", "B", "C"]:
        print(letter)

p1 = Process(target=print_numbers)
p2 = Process(target=print_letters)

p1.start()
p2.start()

p1.join()
p2.join()



import time
time.sleep(1)





