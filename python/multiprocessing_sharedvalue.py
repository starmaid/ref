from multiprocessing import Process, shared_memory, Value, Array
import time
from ctypes import Structure, c_int32, c_uint32, c_longlong, c_double


class NetWrapper():
    def __init__(self) -> None:
        pass
    
    def startThread(self):
        
        track_number = Value('i', 7)
        self.jointsCommand = Array(c_int32, [0]*10)
        
        m = NetCommThreadManager(track_number)
        
        # after this point, the class is copied to the new process. Only values with shared memory can be accessed
        self.netProcess = Process(target=m.tick, args=(), daemon=True)
        self.netProcess.start()
        
        # in this time, it will count up
        time.sleep(5)
        
        with self.jointsCommand.get_lock():
            for i in range(0,10):
                self.jointsCommand[i] = 3
    
        # here, this prints the value we set in our instantiation - we retain a copy of the original object.
        #print(m.value)
        
        print(track_number.value)
        self.netProcess.kill()
        

class NetCommThreadManager():
    counter = 0
    
    def __init__(self, startvalue) -> None:
        self.counter = startvalue
        pass
    
    def tick(self):
        while True:
            print(self.counter.value)
            with self.counter.get_lock():
                self.counter.value += 1
            time.sleep(1)
    
    def send(self):
        pass
    
    def recv(self):
        pass
    
    
if __name__ == "__main__":
    n = NetWrapper()
    n.startThread()