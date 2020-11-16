from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import itertools  
import os
from subprocess import *
import subprocess
import sys
import time
import random
import csv

# ecg=subprocess.Popen('python Cardio/run.py')
x=0
y=0
open_terminal=True
ecg=1

def doc_reg(request):
    detail=[]
    if request.method=='POST':
        fname=request.POST['name']
        lname=request.POST['lastname']
        detail.append(fname)
        detail.append(lname)
        messages.info(request,fname)
        return redirect('/doc_log')
    else:
        return render(request,'doc_reg2.html')

def doc_log(request):
    return render(request,'doc_login.html')

def home(request):
    global ecg
    detail=[]
    if request.method=='POST':
        full_name=request.POST['full_name']
        age=request.POST['age']
        phone=request.POST['phone']
        gender=request.POST['gender']
        detail.append(full_name)
        detail.append(age)
        detail.append(phone)
        detail.append(gender)
        print(detail)
        messages.info(request,full_name)
        print('user created')
        ecg=subprocess.Popen('python spi.py')
        # theproc.communicate()
        return redirect('/reading')
    else:
        return render(request,'home.html')


def fetch_ecg():
    global x
    with open('ecg_sibam.csv','r') as ecg:
        ecg_reader=csv.reader(ecg)
        nline=next(itertools.islice(csv.reader(ecg), x, None))
        x+=1
        yield nline

def fetch_pcg():
    global y,open_terminal,ecg
    if(open_terminal==True):
        ecg.terminate()
        open_terminal=False
        # ecg=subprocess.Popen('python pcg_csv.py')
    print('Inside fetch 2')
    with open('data.csv','r') as pcg:
        ecg_reader=csv.reader(pcg)
        nline=next(itertools.islice(csv.reader(pcg), y, None))
        y+=1
        yield nline


def fetch_value(request):
    data={}
    sensor_data=[]
    for ls in fetch_ecg():
        # print("ecg is :",ls)
        return JsonResponse(ls,safe=False)

def fetch_value2(request):
    data={}
    sensor_data=[]
    for ls in fetch_pcg():
        # print("pcg is :",ls)
        return JsonResponse(ls,safe=False)

def reading(request):
    return render(request,'reading.html')


def final(request):
    global ecg
    # ecg.terminate()
    ecg=subprocess.Popen('python Cardio/run.py')
    #messages.info(request,fname)
    return render(request,'final.html')