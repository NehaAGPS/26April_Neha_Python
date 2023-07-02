# Write a Python program to returns sum of all divisors of a number.

def sum_div():
    divisors = [1]
    number=int(input("Enther Number:-"))
    for i in range(2,number):
        if (number % i) == 0:
            divisors.append(i)
            print(sum(divisors))
sum_div()