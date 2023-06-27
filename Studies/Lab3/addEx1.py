currentValue = float(input("What is the current cost of the property? "))
distFromCity = float(input("How far the property is from the city? "))
valueCalc = int(input("Value calculation after how many years? "))

print(f'{"Years":>4}{"Value":>10}')
appValue = 0

if distFromCity <= 20:
    appRate = 0.02
else:
    appRate = 0.01
for count in range(1,valueCalc+1):
    if appRate == 0.02:
        appValue = currentValue*appRate + currentValue
        print(f'{count:>4} {appValue:>10.2f}')
        currentValue = appValue
    else:
        if appRate == 0.01:
            appValue = currentValue*appRate + currentValue
            print(f'{count:>4} {appValue:>10.2f}')
            currentValue = appValue
print(f'Value of the property after {valueCalc} years: ${appValue:.2f}')



