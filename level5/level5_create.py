import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.getcwd()
SUCESS_MESSAGE = "completed successfully"
COMMAND  = f'pyinstaller --noconfirm --onefile --console --icon "{BASE_DIR}/level5.ico"  "{BASE_DIR}/level5.py"'


def create_challenge_exe(flag):
    with open('./level5_format.py', 'r') as f:
        data = f.read().replace('REAL_FLAG', flag)
    
    with open('./level5.py', 'w') as f:
        f.write(data)

    os.system(COMMAND)
    os.remove('./level5.py')


def main(flag):
    create_challenge_exe(flag)


if __name__ == "__main__":
    try:
        flag = sys.argv[1] # Doesn't work with spaces!!
        main(flag)
    except IndexError:
        logging.error('Please enter the flag to hide in exe')

