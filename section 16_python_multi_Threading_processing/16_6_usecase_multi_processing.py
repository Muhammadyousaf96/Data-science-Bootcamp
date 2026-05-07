import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(1000000)

def computer_factorial(number):
    print(f"computer factorial {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [50090, 20000, 3044]

    start_time = time.time()

    with multiprocessing.Pool() as pool:          # ✅ capital P
        results = pool.map(computer_factorial, numbers)

    end_time = time.time()

    print(f"results: {results}")
    print(f"time taken {end_time - start_time} seconds")  # ✅ fix subtraction