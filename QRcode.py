import qrcode
import os
from datetime import datetime

data = input("Enter URL or text: ").strip()
if not data:
    print("Input cannot be empty!")
    exit()
fill_color = input("Enter QR color (default: black): ").strip() or "black"
back_color = input("Enter background color (default: white): ").strip() or "white"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"qr_{timestamp}.png"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)
img.save(file_name)

print(f"QR Code generated successfully: {file_name}")
 
try:
    os.startfile(file_name)
except:
    pass
