""" Avinash finishes cooking while Anantharamu cleans """

import threading
import time

def kitchen_cleaner():
    while True:
        print('Anantharamu cleaned the kitchen.')
        time.sleep(1)

if __name__ == '__main__':
    Anantharamu = threading.Thread(target=kitchen_cleaner)
    Anantharamu.daemon = True
    Anantharamu.start()

    print('Avinash is cooking...')
    time.sleep(0.6)
    print('Avinash is cooking...')
    time.sleep(0.6)
    print('Avinash is cooking...')
    time.sleep(0.6)
    print('Avinash is done!')
