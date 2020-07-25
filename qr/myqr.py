import qrcode
mydata="www.youtube.com"
#creating an instance
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(mydata)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('qr1.png')