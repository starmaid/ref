import threading
import time

class Data():
    a = 1
    b = 10
    
    
class A():
    def __init__(self) -> None:
        self.d = Data()
        self.running = False
        pass
    
    def run(self):
        self.d.a = 2
        
        self.running = True
        th = threading.Thread(target=self.loop)
        th.start()
        
        time.sleep(5)
        self.running = False
        
        print(th.is_alive())
        
        print(f'{self.d.a} {self.d.b}')
        
        th.join()
        
        print(th.is_alive())
        
        pass
    
    def loop(self):
        while self.running:
            self.d.b += 1
            print(f'{self.d.a} {self.d.b}')
            time.sleep(1)
        


if __name__ == "__main__":
    a = A()
    a.run()