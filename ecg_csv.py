import csv
import random
import time
import os
from datetime import datetime

def main():
    for data in data_gen():
        data_entry(data[0],data[1],data[2])


def data_gen():
        x = 25
        l=0
        while True:
            now=datetime.now()
            ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
            
            try:
                # inRaw =analogInput(2) # Reading from CH0
                val=random.randint(-600,600)
                
                # data_entry(val,x)
                # sleep(2)
                # inInt = int(inRaw)
                # sensor_data.append(str(inInt)+','+str(x))
                # print(inInt)
            except:
                val = 0

            l+=1
            time.sleep(0.001)
            # data_entry(val,x)
            # print('yielded')
            # yield val,x
            yield l,val,ok_date

def data_entry(slno,data,value):
    with open('ecg1.csv','a',newline='') as ecg_file:
        csv_writer=csv.writer(ecg_file)
        csv_writer.writerow([slno,data,value])

main()
