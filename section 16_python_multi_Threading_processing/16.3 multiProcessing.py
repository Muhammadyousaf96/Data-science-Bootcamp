import multiprocessing
import time

import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"square_number:{i*i}")
        
def cubic_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"cubic_number: {i*i*i}")
        
if __name__ == "__main__":
    
    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cubic_number)
    
    t=time.time()  
    p1.start()
    p2.start()
      
    p1.join()
    p2.join()
    
    finished_time=time.time()-t
    print(finished_time)
  
# output  
# square_number:0
# cubic_number: 0
# square_number:1
# square_number:4
# cubic_number: 1
# square_number:9
# cubic_number: 8
# square_number:16
# cubic_number: 27
# cubic_number: 64
#finished_time: 7.621584415435791
