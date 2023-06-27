"""
Author: Lucas
File Name: Ex18.py
Date: 25/02/2022

This program reads two integer numbers.
Then calculates the sum and product of the two numbers
Finally it prints the sum and the product values
"""
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
#Lets sum the inputs
sum = num1+num2
#lets multiply the inputs
prod = num1*num2
#Use the f string format to embed the variables within the string message
#This technique is known as interpolation. Evalation of variables to values.
print(f'Addition of the two numbers: {sum:.2f}.\nProduct of the two numbers: {prod:.2f}.')
