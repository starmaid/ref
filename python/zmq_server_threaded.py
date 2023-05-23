import zmq
import time
import threading as th

ctx = zmq.Context()
sock = ctx.socket(zmq.REP)
sock.bind('tcp://*:6000')

myvalue = 0

def shutdown():
    global ctx
    for i in range(10):
        time.sleep(1)
        print(i)
    print('closing')
    ctx.destroy(linger=0)

def update():
    global ctx
    global myvalue
    while ctx is not None:
        myvalue = time.monotonic()
        time.sleep(0.5)

def runserver():
    global myvalue
    while True:
        message = sock.recv()
        print(f"Received request: {message}")
        sock.send_string(f"{myvalue}")



t0 = th.Thread(target=shutdown)
t1 = th.Thread(target=update)
t2 = th.Thread(target=runserver)
t0.start()
t1.start()
t2.start()

