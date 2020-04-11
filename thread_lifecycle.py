""" Two threads cooking soup """

import threading
import time

class ChefAvinash(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        print('Avinash started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Avinash is done cutting sausage.')

# main thread
if __name__ == '__main__':
    print("Anantharamu started & requesting Avinash's help.")
    Avinash = ChefAvinash()
    print('  Avinash alive?:', Avinash.is_alive())

    print('Anantharamu tells Avinash to start.')
    Avinash.start()
    print('  Avinash alive?:', Avinash.is_alive())

    print('Anantharamu continues cooking soup.')
    time.sleep(0.5)
    print('  Avinash alive?:', Avinash.is_alive())

    print('Anantharamu patiently waits for Avinash to finish and join...')
    Avinash.join()
    print('  Avinash alive?:', Avinash.is_alive())

    print('Anantharamu and Avinash are both done!')
