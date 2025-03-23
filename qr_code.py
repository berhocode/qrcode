import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L) #box_size=20, border=10
print('hello, welcome to our QRcode generator APP!')
user_data = input("> ")
qr.add_data(user_data)
qr.make(fit=True)
available_colors = ["red", "blue", "white", "pink", "green"]
user_color = input("what's the background color you prefer?  (red, blue, white, pink, green)> ")
if user_color not in available_colors:
    print("Invailable color, pls try again")
else:
    print(f"{user_color} applied!")
data_name = input("Enter the name of your QRcode img > ")
img = qr.make_image(back_color=user_color)
img.save(f"{data_name}.png")
 