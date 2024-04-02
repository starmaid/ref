

import signal

import pybcapclient.bcapclient as bcapclient

running = True

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)

# this will run teh function when the signal happens