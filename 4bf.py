import time
import math

def delayed_square_root(number, milliseconds):
    seconds = milliseconds / 1000

    time.sleep(seconds)

    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

input_number = 25100
input_milliseconds = 2123

delayed_square_root(input_number, input_milliseconds)
