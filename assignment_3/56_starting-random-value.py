# How will you set the starting value in generating random numbers?

"""
 The Random number generator needs a number to start with (a seed value),to be able to generate
 a random number.
 By  default the random number generator uses the currunt system time Use the seed() method
 to customize the start number of the random number generator. 

"""

import random

y = "y"
while y!="n":
    random.seed(10)
    print(random.random())
    y=input("Do You Wan't to Countinue 'y' for 'yes' 'n' for 'no' :-")
    