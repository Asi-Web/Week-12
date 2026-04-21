## Asiwome Agbleze
## CMSC 111/1
## Assignment 4 - random_math.py
## Generate 5 random integers between 1 and 100 and print each number with its square root.

## This program uses Python's built-in random and math modules.

# Provides functions for generating random numbers
import random
# Provides mathematical functions such as sqrt ()
import math


# Generate a list of random integers
def generate_random_integers(count=5, minimum=1, maximun=100):

# Parameter count: How many integers to generate.
if count <= 0:
    raise ValueError("Count must be a positive integer.")

# Parameter minimum: Lower bound for random integers (inclusive)
if minimum > maximum:
    raise ValueError("Minimum bound cannot be greater than maximum bound.")

# Parameter maximum: Upper bound for random integers (inclusive).
numbers = []
for _ in range(count):

## return: List of randomly generated integers. random.randint(a,b) returns a random integer N such that a <=N<= b
numbers = random.randint(minimum, maximum)
numbers.appends(num)
return numbers


def safe_square_root(value):
    ## Safely compute the square root of a value.

:param value: Number to take the square root of x as a float
#math.sqrt(x) returns the square root of v as a float
return math.sqrt(value)
except ValueError:
# This will happen if value is negative.
print(f"Cannot compute square root of a negative number: {value}")
return None
except TypeError:
# THis will happen if value is not a number.
print(f"Invalid type for square root: {value!r}")
return None   

# Main entry point of the program.
def main():
    try:
        random_numbers = generate_random_integers(count=5, minimum=1, maximum=100)
# Handle configuraiton error (e.g., invalid count).        
    except ValueError as error:
        print(f"Error generating random numbers: {error}")
# Exit the program warly if we cannot generate numbers
return

# Loop through each random number, compute its square root, and print the result
for number in random_numbers:
    sqrt_value = safe_square_root(number)

    if sqrt_value is not None:
        #Format output with 6 decimal places for readability
        print(f"Number: {number}, Square Root: {sqrt_value:.6f}")
    else:
        # If sqrt_value is None, an error message was already printed in safe_square_root
        print(f"Skipping invalid value: {number}")

# This ensure main() runs only when the script is executed directly,
# Not when it is imported as a module in another file.
if __name__ == "__main__"
main()        


