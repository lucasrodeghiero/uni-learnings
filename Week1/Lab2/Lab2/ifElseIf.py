""" Ordering a pizza that Verne can eat """

#things that Verne does not eat
diet_restrictions = set(['meat','cheese'])

#decide which pizza to order

#The more restrictive options should go near the top
#EVALUTE THE HIGHEST PRIORITY

#if 'meat' in diet_restrictions: FIRST TO BE DONE BUT WASNT THE MOST RESTRICTIVE

if 'meat' and 'cheese' in diet_restrictions:
    print('Get a vegan pizza.')

#elif 'meat' and 'cheese' in diet_restrictions: SECOND TO BE DONE
elif 'meat' in diet_restrictions:
    print('Get a cheese pizza.')

else:
    print('Get something else.')
