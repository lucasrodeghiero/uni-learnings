"""
input  = 2 integers 1 float

output = 4 decimals
print the numbers with format :.4f
"""

int1 = int(input("Enter an integer value: "))
int2 = int(input("Enter an integer value: "))
float1 = float(input("Enter a float value: "))
print(f'The first integer value is {int1+int2+float1 : .4f}')
