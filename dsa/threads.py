from threading import Thread

def display():
    print("hello")
t1=Thread(target=display)
t1.start()

