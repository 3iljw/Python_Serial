import serial
import csv
import os
from datetime import datetime
from pathlib import Path
import threading
import queue

path = str(Path().absolute())
start = datetime.now()
create = start.strftime("%Y%m%d%H%M%S")
que = queue.Queue()

def save_data() :
    while th1.open :
        while que.qsize() :
            data = que.get()
            x = [hex(i)[2:] for i in list(data)]
            y = [j if len(j)==2 else '0'+j for j in x ]
            # try :
            #     print(now, y[0])
            # except IndexError as e:
            #     continue
            try :
                with open (path+'\\RS485DATA\\'+create+'.csv', 'a', newline='') as f :
                    w = csv.writer(f)
                    w.writerow([now, y[0]])
            except FileNotFoundError :
                os.mkdir(path+'\\RS485DATA')
                w = csv.writer(f)
                w.writerow([now, y[0]])
                
def write_data(ser) :
    while th2.open :
        data = input('Type your input : ')
        data = (str(data)).encode()
        ser.write(data)

ser = serial.Serial(
    port = 'COM3', 
    baudrate = 115200, 
    parity = 'N', 
    stopbits = 1, 
    bytesize = 8,
    timeout = 0.1
)

th1 = threading.Thread(target=save_data)
th2 = threading.Trread(target=write_data, args=(ser,))
th1.open = True
th2.open = True
th1.start()
th2.start()


now = datetime.now()
try :
    while 1 :
        mcu_feedback = ser.read()
        que.put(mcu_feedback)
    ser.close()
except :
    th1.open = False
    th1.join()

