import zmq
import time
import threading as th

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6000")

def shutdown():
    global context
    for i in range(10):
        time.sleep(1)
        print(i)
    print('closing')
    context.destroy(linger=0)

t0 = th.Thread(target=shutdown)
t0.start()

#  Do 10 requests, waiting each time for a response
while True:
    try:
        print(f"Sending request...")
        socket.send_string("Hello")

        #  Get the reply.
        
        print('listening')
        message = socket.recv()
        print(f"Received reply [ {message} ]")
        time.sleep(1)
    except:
        break