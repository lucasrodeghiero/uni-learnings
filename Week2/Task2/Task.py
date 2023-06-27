"""
Lucas do Amaral
03/03/2022
"""

file = open('studMarks.txt', 'r')

#Table Header
print(f"{'Student Name':<5} {'Average Mark':>30}\n-------------------------------------------")
for line in file:
    words = line.split() #Splits all the strings
    givenName = words[0]
    lastName = words[1]
    marks = words[2:7]
    marksList = [] #Empty list to add value
    for grade in marks:
        marksList.append(int(grade)) #Adds value to my empty list
    totalMarks = sum(marksList)
    average = totalMarks/len(marks)
    print(f'{lastName+ "," +givenName:<20} {average:>22.2f}')

file.close()
