###
### Author: Simran Sall
### Course: CSc 110
### Description: This program displays an image of a tie-fighter,
###              which is a type of spacecraft from Star Wars.
###              Users can input how wide they want their tie-fighter
###              to be, and the width of the tie-fighter will be adjusted
###              accordingly. The numbers that users input will only
###              affect the width of the tie-fighter.
###

width = int(input("Enter TIE width: : "))  #this allows the user to input a number that will be the width of the spacecraft.

print("|" + "[" + " " * width + "         " + " " * width + "]" + "|")
print("|" + "[" + " " * width + "         " + " " * width + "]" + "|")
print("|" + "[" + " " * width + " " + "/" + "=" + "---" + "=" + "\\" + " " + " " * width + "]" + "|")
print("|" + "[" + " " * width + "/" + "==" + "---" + "==" + "\\" + " " * width + "]" + "|")
print("|" + "[" + "/" * width + "|" + "==" + " " + "X" + " " + "==" + "|" + "\\" * width + "]" + "|")
print("|" + "[" + " " * width + "\\" + "==" + "---" + "==" + "/" + " " * width + "]" + "|")
print("|" + "[" + " " * width + " " + "\\" + "=" + "---" + "=" + "/" + " " * width + " " + "]" + "|")
print("|" + "[" + " " * width + "         " + " " * width + "]" + "|")
print("|" + "[" + " " * width + "         " + " " * width + "]" + "|")

