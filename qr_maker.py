import qrcode as qr
s = str(input("enter your link here :"))
a = qr.make(s)
a.save("qr.jpeg")