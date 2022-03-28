from pyaes import AESModeOfOperationCTR
from random import seed, randint
from time import time
from base64 import b64encode
import sys
import logging
import datetime

logging.basicConfig(level=logging.INFO)


def get_seed():
    now = time()
    seed = round(now, 4)
    return now, seed


def set_seed(seed_number):
    seed(seed_number)


def create_key(seed_number):
    seed(seed_number)
    key = [chr(randint(0, 200)) for _ in range(12)]
    key = ''.join(key).encode()
    return key


def encrypt_message(key, message):
    aes = AESModeOfOperationCTR(key=key)
    return aes.encrypt(message)

def main(flag):
    try:
        now, seed = get_seed()
        key = create_key(seed)
        en_flag = b64encode(encrypt_message(key, flag))
        timestamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
        with open('level7.txt', 'w') as f:
            f.write(f'Flag is {en_flag}, Timestamp is {timestamp}')

        logging.info('Successfuly created level 7 details are in: level7.txt')
    except:
        main(flag)


if __name__ == "__main__":
    try:
        flag = sys.argv[1] # Doesn't work with spaces!!
        main(flag)
    except IndexError:
        logging.error('Please enter the flag to encrpyt')
