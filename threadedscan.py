import socket
import threading
import queue

IP = input("enter ip address: ")
q = queue.Queue()


# storing ports in queue with q.put
for i in range(1, 1001):
    q.put(i)

def scan():
    while not q.empty():
        port = q.get()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((IP, port))
            print(f'port {port} is open!')
        except:
            pass
    q.task_done()

# amount of threads to use
for i in range (10):
    t = threading.Thread(target=scan, daemon=True)
    t.start()

q.join()
print('finished')