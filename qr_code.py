import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)

print('Hello, welcome to our QR Code Generator APP!')
user_data = input("> ").strip()
qr.add_data(user_data)
qr.make(fit=True)

available_colors = ["red", "blue", "white", "pink", "green"]
user_color = input("What's the background color you prefer? (red, blue, white, pink, green) > ").strip().lower()

while user_color not in available_colors:
    print("Invalid color, please try again.")
    user_color = input("Choose a valid background color: (red, blue, white, pink, green) > ").strip().lower()

print(f"{user_color} applied!")

# Allow user to choose QR color
qr_color = input("Choose the QR code color (black, white, blue, red, green) > ").strip().lower()

data_name = input("Enter the name of your QR code image > ").strip()

# Generate and save the QR code
img = qr.make_image(fill_color=qr_color, back_color=user_color)
img.save(f"{data_name}.png")

print(f"QR Code saved as {data_name}.png!")
