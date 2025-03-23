# QR Code Generator

This simple Python-based QR Code Generator allows users to generate custom QR codes with their preferred backgrounds and colors. The generated QR codes are saved as images.

## Features
- Generate QR codes from user input.
- Choose a custom background color.
- Choose a custom QR code color.
- Save the generated QR code as an image file.

## Installation

### Prerequisites
- Python 3.x installed on your system
- `qrcode` library (Install using pip if not already installed)

### Install the required dependencies
```sh
pip install qrcode[pil]
```

## Usage
1. Run the script:
```sh
python qrcode_generator.py
```
2. Enter the text/data you want to encode in the QR code.
3. Choose a background color from the available options (red, blue, white, pink, green).
4. Choose a QR code color (black, white, blue, red, green).
5. Provide a filename to save the QR code image.
6. The generated QR code will be saved as an image (.png) in the same directory.

## Example
```
Hello, welcome to our QR Code Generator APP!
> https://github.com/berhocode
What's the background color you prefer? (red, blue, white, pink, green) > blue
Choose the QR code color (black, white, blue, red, green) > black
Enter the name of your QR code image > my_qr_code
QR Code saved as my_qr_code.png!
```

## Author
**Berhocode** 🚀
