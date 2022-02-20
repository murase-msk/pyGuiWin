#!/usr/bin/env python
import PySimpleGUI as sg
import cv2
import numpy as np

"""
Demo program that displays a webcam using OpenCV
"""

# Webカメラ
DEVICE_ID = 0
WIDTH = 1280
HEIGHT = 720
FPS = 30  # 24


def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])


def main():

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(0, 0))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(DEVICE_ID)
    recording = False

    # フォーマット・解像度・FPSの設定
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y', 'U', 'Y', 'V'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    # cap.set(cv2.CAP_PROP_FOCUS, 255)

    # フォーマット・解像度・FPSの取得
    fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    focus = cap.get(cv2.CAP_PROP_FOCUS)
    print("fourcc:{} fps:{}  width:{}  height:{}  focus:{}".format(fourcc, fps, width, height, focus))

    while True:
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Record':
            recording = True

        elif event == 'Stop':
            recording = False
            img = np.full((480, 640), 255)
            # img = np.full((720, 1280), 255)
            # this is faster, shorter and needs less includes
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['image'].update(data=imgbytes)

        if recording:
            ret, frame = cap.read()
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)


main()
