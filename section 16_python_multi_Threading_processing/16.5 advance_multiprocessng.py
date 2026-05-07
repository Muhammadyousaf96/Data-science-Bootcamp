from concurrent.futures import ProcessPoolExecutor
import time 

def cube_number(number):
    time.sleep(1)
    return f"Number: {number*number*number}"

number=[1,2,3,4,5,6,7]
t=time.time()

if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(cube_number,number)
        for result in results:
            print(result)    
executing_time=time.time()-t
print(executing_time)

# output 

# Number: 1
# Number: 8
# Number: 27
# Number: 64
# Number: 125
# Number: 216
# Number: 343
# 3.1689305305480957