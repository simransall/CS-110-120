###
### Author: Simran Sall
### Course: CSc 110
### Description: This program utilizes a user input function so that
###              users can plug in an integer for the width of the
###              castle. With using the print function, this will make
###              the castle wider or shorter depending on the number
###              that was inputted. The castle is a portrayal of the
###              Bodiam Castle.
###

width = int(input("castle width: "))
print("\n")
print(" " * width + "   " + ".-.-." + "  " + " " * width)
print("[-]" + " " * width + "|-.-|" + " " * width + "[-]")
print("| |" + "_" * width + "| H |" + "_" * width + "| |")
print("| |" + " " * width + "| H |" + " " * width + "| |")
print("| |" + " " * width + "| H |" + " " * width + "| |")
print("|_|" + "_" * width + "||^||" + "_" * width + "|_|")