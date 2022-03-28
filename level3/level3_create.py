import qrcode
import os
from base64 import b64encode
import logging
import sys

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.getcwd()

VERSION = 1
BOX_SIZE = 10
BORDER = 4 
FILL_COLOR = 'black'
BACK_COLOR = 'white'
LEVEL_FILE = os.path.join(BASE_DIR, 'Level3.txt')


def create_qr():
    img = qrcode.make()
    qr = qrcode.QRCode(
        version=VERSION,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=BOX_SIZE,
        border=BORDER,
    )

    return qr


def add_data_to_qr(qr, data):
    qr.add_data(data)
    qr.make(fit=True)

    return qr


def encode_qr(qr) -> str:
    img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR).convert('RGB')
    img.save('./temp.png')
    with open('./temp.png', 'rb') as reader:
        data = reader.read()
    
    os.remove('./temp.png')
    encoded_qr = b64encode(data).decode()

    return encoded_qr


def main(link: str):        
    qr = create_qr()
    qr = add_data_to_qr(qr, link)
    encoded_qr = encode_qr(qr)

    with open(LEVEL_FILE, 'w') as f:
        f.write(encoded_qr)

    logging.info(f'Successfuly wrote Level 3 in {LEVEL_FILE}')


if __name__ == "__main__":
    try:
        link = sys.argv[1] # Doesn't work with spaces!!
        main(link)
    except IndexError:
        logging.error('Please enter link to encode')
