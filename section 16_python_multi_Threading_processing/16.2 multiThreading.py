# import threading
# import time

# def print_number():
#     for i in range(5):
#         time.sleep(2)
#         print(f"Numbers:{i}")
        
# def print_letter():
#     for letter in 'abcdef':
#         time.sleep(1)
#         print(f"letter: {letter}")

# t=time.time()    
# print_number()
# print_letter()

# finisted_time=time.time()-t      
# print(finisted_time)
# finished time = 16.011884450912476

# ---------------------------------------------------
# creating two thread for time efficience

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers:{i}")
        
def print_letter():
    for letter in 'abcdef':
        time.sleep(1)
        print(f"letter: {letter}")
        
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)        

t=time.time()    
# strat thread
t1.start()
t2.start()

# waiting for thread to complete
t1.join()
t2.join()

finisted_time=time.time()-t      
print(finisted_time)

# # output 
# letter: a
# Numbers:0
# letter: b
# letter: c
# Numbers:1
# letter: d
# letter: e
# Numbers:2
# letter: f
# Numbers:3
# Numbers:4
#execution time=10.006654977798462  50% efficent if we making two thrads