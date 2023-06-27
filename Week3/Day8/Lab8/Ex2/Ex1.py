from student import Student

#myName = input("Enter your name: ")
#myId = input("Enter your ID: ")
#myAge = int(input("Enter your age: "))
#myMarks = int(input("Enter your marks: "))



s = Student('s4676442', 'Lucas',24,3)

s.setMark(1,85)
s.setMark(2,69)
s.setMark(3,90)
print(s.getMark(2))
print(s)
