import threading
import os
import math
import datetime
start_time=datetime.datetime.now()
lock = threading.Lock()
input_file="file"
output_file="a"
# input_file, output_file = output_file, "decrypt" #decrypt
size = math.ceil(os.path.getsize(input_file)/1048576)#Mb
file_read = open(input_file, "rb")
file_wright=open(output_file, "wb")
threads = []
parts = []
key=b""

for i in range(1048576):
    key=key + b"a"

def devision():
    lock.acquire()
    try:
        parts.append(file_read.read(1048576))
        file_wright.write(encrypt(parts[len(parts) - 1],key))
    finally:
        lock.release()

#xor
def encrypt(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

for i in range(size):
    threads.append(threading.Thread(target=devision))
    threads[-1].start()

for thread in threads:
    thread.join()

file_wright.close()
file_read.close()
print("OK")
print(datetime.datetime.now()-start_time)