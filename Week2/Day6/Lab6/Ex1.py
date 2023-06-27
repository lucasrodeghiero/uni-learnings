def sum(x, y):
    return x+y

def multiply(x, y):
    return x*y

def subtraction(x,y):
    return x-y

def division(x,y):
    if y >= 1:
        return x/y
    else:
        return print("Denominator can't be zero")
def main():
    x = float(input('Enter a number: '))
    y = float(input('Enter a number: '))
    print(f'Addition = {sum(x, y):.2f}')
    print(f'Multiplication = {multiply(x, y):.2f}')
    print(f'Subtraction = {subtraction(x,y):.2f}')
    print(f'Division = {division(x,y):.2f}')

main()
