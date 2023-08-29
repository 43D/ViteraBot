import threading

running = True

def editor():
    while(running):
        print("thread")

def uploader():
    while(running):
        print("thread")

thread1 = threading.Thread(target=editor, args=())
thread2 = threading.Thread(target=uploader, args=())

thread1.start()
thread2.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Recebido sinal de interrupção. Parando o programa no proximo clico...")
    running = False

thread1.join()
thread2.join()