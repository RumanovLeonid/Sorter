import cv2
import datetime
import os
from pyzbar import pyzbar
from glob import glob


QRdata = []


def getQr(filename):
    all_data = []
    img = cv2.imread(filename)    # Считываем файл с изображением
    qrcodes = pyzbar.decode(img)  # Создается список найденных кодов
    for qrcode in qrcodes:
        qrcodeData = qrcode.data.decode('utf-8')
        #if qrcode.type == 'QRCODE' in qrcodeData:  # проверяем тип кода и проверяем вхождение строки 'fn='
        all_data.append(qrcodeData.split('&'))
    return all_data

def LoadQRSample(dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\QRsample\\"):
    for filename in glob('QRsample/*.jpg'):  # Считываем тип файлов только jpg
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
        start = datetime.datetime.now().second
        
        dataStart = ScanQR()
        dataStop = dataStart

        delta = datetime.datetime.now().second - start      
       
        if delta < 1 and (dataStart == dataStop): continue
        elif dataStart is None: continue 
        else:
            return dataStart 

LoadQRSample()


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    data = DebounceScanQR()
    print("[+] QR Code detected, data:", data)
    #cv2.imshow("img", img)    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
#cv2.destroyAllWindows()