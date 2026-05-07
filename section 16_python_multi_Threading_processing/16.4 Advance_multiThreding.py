from concurrent.futures import ThreadPoolExecutor
import time 

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"
number=[1,2,3,4,5,6,7,4,5,6,7,8,99,23]
t=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,number)
    for result in results:
         print(result)    
         
executing_time=time.time()-t
print(executing_time)

# output
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
# Number: 6
# Number: 7
# Number: 4
# Number: 5
# Number: 6
# Number: 7
# Number: 8
# Number: 99
# Number: 23
#executing_time:  5.004369020462036