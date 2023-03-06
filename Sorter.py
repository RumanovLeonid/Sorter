"""Импорт функция задержки"""
from time import sleep
import cv2

SCAN_DELAY = 1


def scan_qr():
    """Сканирование QR кода"""
    _, img = cap.read()
    qr_code, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        if qr_code:
            return qr_code
    return None


def debounce_scanqr():
    """Исключение ложного срабатывания"""
    while True:
        scan = scan_qr()
        sleep(SCAN_DELAY)
        rescan = scan_qr()

        if (scan == rescan) and (scan is not None):
            return scan


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    data = debounce_scanqr()
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
