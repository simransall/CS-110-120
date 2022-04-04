###
### Author: Simran Sall
### Course: CSc 110
### Description: This program creates a version of the Eiffel Tower.
###              By programming a user_input function, users can
###              type in an integer to set the size of the Eiffel Tower,
###              and the tower will adjust to reflect that size. Set
###              formulas are also used so that the structure of the
###              tower remains the same despite changes in size.

size = int(input("Enter Eiffel tower size: \n"))
#set formulas that define the spacing and sizing
upper_height = int(size*1.5)
upper_width = int(3)
middle_width = int(size*2 + 1)
middle_height = int(size/2 + 3)
lower_width = int(size*4 + 1)
lower_height = int(size/1.5)

#formula based on lower width and middle width:
lower_middle = int(size-1)
#formula based on lower width and upper width:
lower_upper = int((3+lower_middle+(middle_width/2)))

print()
print(" " + " " * lower_upper + "$")
print((" " * lower_upper + "|Z|\n") * upper_height, end="")
print("   " + " " * lower_middle + "/" + "Z" * middle_width + "\\" + " " * lower_middle)
print(("   " + " " * lower_middle + "H"+ " " * middle_width+"H\n")* middle_height, end="")
print("  " + "/" +  "%" * lower_width + "\\")
print((" " + "##"+ " " * lower_width + "##\n")* lower_height, end="")
print(("##" + " " + " " * lower_width + " " + "##\n") * lower_height, end="")