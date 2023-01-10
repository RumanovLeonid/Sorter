import os
import qrcode

print("Генератор QR кодов.")
print("")

data = input("Введите данные для кодировния: ")

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "\\" + data + ".jpg"

qr = qrcode.QRCode()
qr.add_data(data)

img=qr.make_image()
img.save(filename)
