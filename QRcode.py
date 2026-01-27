import qrcode

data = input("Enter URl: ")
qr = qrcode.QRCode()

qr = qrcode.QRCode(
    version=1,                 # size of QR (1–40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,                # size of each box
    border=4                    # white border
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("custom_qr.png")

print("Custom QR Code generated!")
