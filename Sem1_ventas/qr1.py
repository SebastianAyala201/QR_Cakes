import qrcode 
# Post 1
input = "https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1"

qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black',back_color='green')
img.save('qr1.png')
