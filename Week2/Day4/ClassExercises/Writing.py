#Open a text file myText.txt on the same folder as your python file
f = open("myText.txt", "w")

#Write text to file
f.write(f'\nLine number 1\nLine number 2\n')

#Close file after writing
f.close()
