import os
import datetime
import time
from glob import glob
import cv2
from pyzbar import pyzbar
import keyboard

SCAN_DELAY = 1
QRdata = []


def getQr(filename):
    all_data = []
    img = cv2.imread(filename)    # Считываем файл с изображением
    qrcodes = pyzbar.decode(img)  # Создается список найденных кодов
    for qrcode in qrcodes:
        qrcodeData = qrcode.data.decode('utf-8')
        all_data.append(qrcodeData.split('&'))
    return all_data


def LoadQRSample(dir_path=os.path.dirname(os.path.realpath(__file__)) + "\\QRsample\\"):
    for filename in glob('QRsample/*.jpg'):
        QRdata.append(getQr(filename))


def ScanQR():
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        if data:
            return data
    return


def DebounceScanQR():
    while True:
        scan = ScanQR()
        time.sleep(SCAN_DELAY)
        rescan = ScanQR()

        if (scan == rescan) and (scan != None):
            return scan


LoadQRSample()


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:

    data = DebounceScanQR()

    match data:
        case "Water":
            print("Water")
        case "Iron":
            print("Iron")
        case "Paper":
            print("Paper")
        case "Ribbon":
            print("Ribbon")
        case _:
            print("Uknown")
