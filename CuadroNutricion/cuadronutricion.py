import qrcode

input = "https://6mij3yavm2cpow3qt03esw.on.drv.tw/www.content.blog/tablanNutricional.html"

qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black',back_color='white')
img.save('Cuadro_nutricion.png')