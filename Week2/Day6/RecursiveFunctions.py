def printInt(num):
    if num > 0:
        print(num)
        printInt(num - 1)

def main():
    num = int(input('Enter a number: '))
    print(printInt(num))

main()
