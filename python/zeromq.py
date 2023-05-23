# example for zeromq

import zmq

# request sends first, then recieves

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://127.0.0.1:50011')
sock.send_string('blah')
sock.recv()

# reply waits for something, and then replies

ctx = zmq.Context()
sock = ctx.socket(zmq.REP)
sock.connect('tcp://127.0.0.1:50011')
sock.recv()
sock.send_string('blah')
