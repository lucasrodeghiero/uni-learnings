from student import Student

myName = input("Enter your name: ")
myId = input("Enter your ID: ")
myAge = int(input("Enter your age: "))

s = Student(myId,myName,myAge)

print(s)
