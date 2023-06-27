# Declare constance

CITY_CLOSE_RATE = 2
CITT_DIST_RATE = 1
BNDRY_DIST = 20

def getrate(propDist):
    #Select the right rate based on distance
    if propDist <= BNDRY_DIST:
        rate = CITY_CLOSE_RATE
    else:
        rate = CITT_DIST_RATE
    return rate/100 #Calculate percentage and return

def print_output(year, rate, propVal):
    #Print header of the table
    print(f'{"Year":>5}{"Value":>15}')
    #Calculate property value for each year
    count = 0
    for count in range(1, year+1):
        increment = propVal *rate
        endVal = propVal + increment
        print(f'{count:>5}{endVal:15.2f}')
        propVal = endVal
    #Print final property value after appreciation
    print(f'Value of the property after {count} years: ${propVal:.2f}')

def main():
    #Read inputs
    propVal = float(input("What is the current cost of the property? "))
    propDist = float(input("How far property is from the city? "))
    year = int(input('Value calculation after how many years? '))
    rate = getrate(propDist)
    print_output(year, rate, propVal)
main()
