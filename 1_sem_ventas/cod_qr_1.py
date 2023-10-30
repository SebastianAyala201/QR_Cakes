import qrcode

input = "https://www.peru.travel/Contenido/AcercaDePeru/Imagen/es/1/0.0/Principal/Machu%20Picchu.jpg"

qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black',back_color='green')
img.save('imagenprueba.png')