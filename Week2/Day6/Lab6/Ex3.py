def convertCtoF(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
def convertFtoC(fahrenheit):
    celsius = (fahrenheit - 32) *5/9
    return celsius
def main():
    temp = float(input('Please enter a temperature to convert: '))
    convert = input("Convert to Celsius or Fahrenheit? (C or F)? ").upper()
    if convert == 'C':
        print(f'{convertFtoC(temp):.2f}C')
    elif convert == 'F':
        print(f'{convertCtoF(temp):.2f}F')
    else:
        print('Please enter a valid unit Fahrenheit (F) or Celsius (C)!!!!!!')

main()
