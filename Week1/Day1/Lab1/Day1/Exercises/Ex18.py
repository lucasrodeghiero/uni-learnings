"""
Author: Lucas
File Name; Ex18.py
Date: 21/02/2022

This program reads two integer numbers.
Then calculates the sum and product of the two numbers.
Finally it prints the sum and the product values.
"""
#Started with INTEGERS and moved to FLOAT to allow user to input DECIMALS
#num1 = int(input("Please enter the first number: "))
#num2 = int(input("Please enter the second number: "))
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
sum = num1 + num2
prod = num1 * num2
#Use the f string format to embed the variables within the string message
#This technique is known as interpolation. Evalation of variables to values.
print(f'Addition of the two number = {sum : .2f}.\n Product of the two numbers = {prod : .2f}.')
