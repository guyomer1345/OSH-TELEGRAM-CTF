import os
from random import randint
import logging
import sys

logging.basicConfig(level=logging.INFO)

FLAG_FILE = './Level4.png'
FOLDER_AMOUNT = 3
ROOT = "./Level4/"
PATH = ROOT + '/'.join([str(randint(0, FOLDER_AMOUNT-1)) for x in range(FOLDER_AMOUNT)])


def create_flag_file(flag: str) -> None:
    with open(FLAG_FILE, 'rb') as reader:
        data = reader.read()
    
    data += flag.encode()
    with open(PATH + '/Level4.png', 'wb') as f:
        f.write(data)
    


def create_dir(path:str , d: int):
    print("creating folder ", path)
    os.system("md {}".format(path))
    if d <= 3:
        for i in range(FOLDER_AMOUNT):
            os.chdir(path)
            create_dir(str(i), d+1)
            os.chdir("..")
        
    
def main(flag):
    create_dir("Level4", 1)
    create_flag_file(flag)

    logging.info(f'Successfuly wrote level 4 in Level4 {PATH}')


if __name__ == "__main__":
    try:
        flag = sys.argv[1] # Doesn't work with spaces!!
        main(flag)
    except IndexError:
        logging.error('Please enter flag to append to image')
