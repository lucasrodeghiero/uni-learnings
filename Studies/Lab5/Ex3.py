file = open("student.txt", 'r')

for line in file: # pick lines from file
    words = line.split()
    givenName = words[0] #first index
    lastName = words[1] #second index
    fee = float(words[3]) #fourth index
    advance = float(words[4]) #fifth index
    #calculate fees due
    due = fee - advance
    print(f'{givenName+ " " +lastName:<20}{due:>10.2f}')
