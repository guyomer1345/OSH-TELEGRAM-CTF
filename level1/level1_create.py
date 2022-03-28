import sys
import logging
import os

logging.basicConfig(level=logging.INFO)

PADDING = "False"
BASE_DIR = os.getcwd()
LEVEL_FILE = os.path.join(BASE_DIR, 'Level1.txt')
BINARY_HEADER = 2


def text_to_binary(text: str) -> str:
    return bin(int.from_bytes(text.encode(), 'big'))


def encrypt_binary(binary_text: str) -> str:
    return binary_text[BINARY_HEADER:].replace("0", "False").replace("1", "True")


def main(text):
    binary_text = text_to_binary(text)
    encrypted_message = encrypt_binary(binary_text)

    with open(LEVEL_FILE, 'w') as f:
        f.write(PADDING  + encrypted_message)

    logging.info(f'Successfuly wrote Level 1 in {LEVEL_FILE}')

if __name__ == "__main__":
    try:
        text = sys.argv[1] # Doesn't work with spaces!!
        main(text)
    except IndexError:
        logging.error('Please enter text to encode')
