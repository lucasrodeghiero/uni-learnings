vegMeal = int(input("Please enter the amount of vegetarian meals: "))
meatMeal = int(input("Please enter the amount of meat meals: "))
seaMeal = int(input("Please enter the amount of seafood meals: "))
print(f'Order Details\n**************\nVegeratian: {vegMeal}\nMeat: {meatMeal}\nSeafood: {seaMeal}')
print(f'Your total expense is: ${vegMeal*11.80+meatMeal*12.80+seaMeal*14.00:.2f}')

