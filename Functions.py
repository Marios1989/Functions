# Functions
def spam():
    """"Prints 'Eggs!' """
    print("Eggs! ")

    spam()

# Call and Response
def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print()
    "%d squared is %d." % (n, squared)
    return squared


# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

my_number_squared = square(10)

# Parameters and Arguments
def power(base,exponent):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!

# Functions Calling Functions
def one_good_turn(n):
    return n + 1


def deserves_another(n):
    return one_good_turn(n) + 2

# Few more functions
def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

# Generic Imports
import math
print(math.sqrt(25))

# Function Imports
# Import *just* the sqrt function from math on
from math import sqrt

# Universal Imports
from math import *

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!

# On Beyond Strings
def biggest_number(*args):
    print()
    max(args)
    return max(args)


def smallest_number(*args):
    print
    min(args)
    return min(args)


def distance_from_zero(arg):
    print
    abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# max
# Set maximum to the max value of any set of numbers

maximum = max(4,5,6.0)

print(maximum)

# min
# Set minimum to the min value of any set of numbers

minimum = min(9,7,4)

print(minimum)

# abs()
absolute = abs(-42)

print(absolute)

# type ()
# Print out the types of an integer, a float,
# and a string on separate lines below.

print(type(89))
print(type(8.9))
print(type('spam'))

# Review Functions
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

# Review Modules
import math
print(math.sqrt(13689))

# Review Built-In Functions
def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"