from pathlib import Path
import os 
import shutil
from pexpect import popen_spawn


def darknet(message):
    os.chdir("C:/Yolo_v4/darknet/build/darknet/x64")
    process = popen_spawn.PopenSpawn('darknet.exe detector test data/verse2.data \
                                    cfg/yolov4-verse2.cfg backup/yolov4-verse2_last.weights \
                                    -dont_show -ext_output -save_labels') #Running Darknet
    print(message)
    return process



def predict_labels():
    message = 'Darknet Started'
    darknet_process = darknet(message)
    for i in range(1,7290):
        print(i)
        carla_scene = (f"C:/Users/User/Desktop/objs/Photo{i}.jpg".encode())
        darknet_process.send(carla_scene+b'\n')

def calculate_accuracy():
    X=""
    y=""
    ypath='C:/Yolo_v4/darknet/build/darknet/x64/data/objs/'
    Xpath='C:/Users/User/Desktop/objs/'
    correct=0
    for i in range(1,7290):
        try:
            with open(f'{Xpath}Photo{i}.txt') as f:
                X= f.read()
            with open(f'{ypath}Photo{i}.txt') as g:
                y=g.read()
            if len(X)==0 and len(y)==0:
                correct+=1
            elif len(y)==38 and len(X)==30 and X[0]==y[0]:
                correct+=1
            elif len(y)==76 and len(X)==60 and ((X[0]==y[0] and X[30]==y[38]) or (X[0]==y[38] and X[30]==y[0])):
                correct+=1

        except FileNotFoundError:
            continue
    print(correct/7289)


def calculate_accuracy_for_class():
    X=""
    y=""
    ypath='C:/Yolo_v4/darknet/build/darknet/x64/data/objs/'
    Xpath='C:/Users/User/Desktop/objs/'
    correct=0
    theclass='3'
    for i in range(1,7290):
        try:
            with open(f'{Xpath}Photo{i}.txt') as f:
                X= f.read()
            with open(f'{ypath}Photo{i}.txt') as g:
                y=g.read()
            if len(y)==38 and len(X)==30 and y[0]==theclass and X[0]==y[0]:
                correct+=1
            elif len(y)==76 and len(X)==60 and (y[0]==theclass or y[38]==theclass) and (X[0]==theclass or X[30]==theclass)  :
                correct+=1

        except FileNotFoundError:
            continue

    print(correct/431)


def calculate_accuracy_for_no_detection():
    X=""
    y=""
    ypath='C:/Yolo_v4/darknet/build/darknet/x64/data/objs/'
    Xpath='C:/Users/User/Desktop/objs/'
    correct=0
    theclass='3'
    for i in range(1,7290):
        try:
            with open(f'{Xpath}Photo{i}.txt') as f:
                X= f.read()
            with open(f'{ypath}Photo{i}.txt') as g:
                y=g.read()
            if len(y)==0 and len(X)==0:
                correct+=1

        except FileNotFoundError:
            continue
    print(correct/6055)


def access_datas():s
    line=""
    L=[] 
    path='C:/Yolo_v4/darknet/build/darknet/x64/data/objs/'
    for i in range(1,7290):
        try:
            with open(f'{path}Photo{i}.txt') as f:
                line = f.read()
                if len(line)==38*2:
                    L.append(i)        
        except FileNotFoundError:
            continue

    print(f"The vehicles in front are {len(L)}")











    
