f = open('../../../Studies/Lab5/student.txt', 'r')

for line in f: #pick lines from file f
    words = line.split()
    fName = words[0]
    sName = words[1]
    fee = float(words[3])
    advance = float(words[4])
    #calculate fees due
    due = fee - advance
    print(f'{fName+" "+sName:<20}{due:>20.2f}')



