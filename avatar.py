###
### Author: Simran Sall
### Course: CSc 110
### Description: This program allows a user to create an avatar.
###              Users can either create a custom avatar, or choose
###              one of the existing avatars (Jeff, Adam, or Chris).
###              Users can input a hat style, torso length, leg length,
###              eyes, arms, and a hair style to create a custom avatar.
###              If an existing avatar is chosen, the program will print
###              out either Jeff, Adam, or Chris (depending on which one
###              was chosen).
###

def hat(hat_style):
    '''Gets a string from the user, and will print a
    certain hat style depending on the input. Hat styles can either
    be left, right, both left and right-facing, or front-facing.
        hat_style: string that indicates if the hat style will be
        left-facing, right-facing, both ways, or just front-facing.
    '''
    print('       ~-~ ')
    print('     /-~-~-\\')
    if hat_style == 'left':
        print(' ___/_______\\')
    if hat_style == 'right':
        print('    /_______\\___')
    if hat_style == 'both':
        print(' ___/_______\\___')
    if hat_style == 'front':
        print('    /_______\\')

def face(hair_style, eyes_style):
    '''Gets a string from the user and creates a face depending on the
    custom characters the user inputs. The face is customized by the
    hair and the eye character.
        hair_style: "True" will cause the hair to be shaggy while "False" will
        cause the avatar to have non-shaggy hair.
        eyes_style: the user will input the character that they want their
        avatar's eyes to be.
    '''
    if hair_style == "True":
        print('    |"""""""|')
    else:
        print("    |'''''''|")
    print('    | ' + eyes_style + '   ' + eyes_style + ' |')
    print('    |   V   |')
    print('    |  ~~~  |')
    print('     \_____/ ')

def arms(arm_style):
    '''This gets a string from the user and creates the arms that consist
    of the character that the user inputs.
        arm_style: a string that allows the user to input a character for the arms.
    '''
    print(' 0' + arm_style + arm_style + arm_style + arm_style + '|---|' \
    + arm_style + arm_style + arm_style + arm_style + '0')

def torso(torso_style):
    '''Builds the torso with the length depending on the torso_style. The
    appearance of the torso will always remain the same, but the length is
    altered depending on the integer that the user inputs.
        torso_style: integer that a user inputs to indicate how long
        they want the avatar's torso to be.
    '''
    i=0
    while i < int(torso_style):
        print('      |-X-|\n', end='')
        i+=1

def legs(leg_style, shoe_style):
    '''Prints the bottom-half of the avatar, including the legs and shoes, based
    on the leg_style and shoe_style parameters. The appearance of the legs will always
    be consistent, only the length will change. The shoes are customized to the
    string that the user inputs.
        leg_style: integer that a user inputs to indicate how long they want
        the avatar's legs to be. Number can be any integer between 1 and 4.
        shoe_style: string that user inputs to determine the style of the
        avatar's shoe. Can be up to 5 characters.
    '''
    print('      HHHHH')
    i = 0
    middle = 1
    string = ' '
    left = 5
    while i < int(leg_style):
        j = 0
        while j < left:
            print(' ',end='')
            j+=1
        print('///', end='')
        j=0
        while j < middle:
            print(' ',end='')
            j+=1
        print('\\\\\\\n',end='')
        i +=1
        middle+=2
        left-=1
    print(shoe_style + '       ' + shoe_style)

def jeff():
    '''This function is for one of the pre-made avatars, and will
    print out an avatar based on pre-determined parameters.
    '''
    print()
    hat('both')
    face('True', '0')
    arms('=')
    torso('2')
    legs('2', '#HHH#')

def adam():
    '''This function is for one of the pre-made avatars, and will
    print out an avatar based on pre-determined parameters.
    '''
    print()
    hat('right')
    face('False', '*')
    torso('1')
    arms('T')
    torso('3')
    legs('3', '<|||>')

def chris():
    '''This function is for one of the pre-made avatars, and will
    print out an avatar based on pre-determined parameters.
    '''
    print()
    hat('front')
    face('True', 'U')
    torso('1')
    arms('W')
    torso('1')
    legs('4', '<>-<>')

def main():
    print('----- AVATAR -----')
    choice = input("Select an Avatar or create your own: \n")
    while choice != "Jeff" and choice != "Adam" and choice != "Chris"\
    and choice != "custom" and choice!= "exit":
        choice = input("Select an Avatar or create your own: \n")
    if choice == "exit":
        print()
    if choice == "Jeff":
        jeff() #the way jeff is printed is defined in this function
    if choice == "Adam":
        adam() #the way adam is printed is defined in this function
    if choice == "Chris":
        chris() #the way chris is printed is defined in this function
    if choice == "custom":
        print("Answer the following questions to create a custom avatar")
        hat_style = input("Hat style ? \n")
        eyes_style = input("Character for eyes ? \n")
        hair_style = input("Shaggy hair (True/False) ? \n")
        arm_style = input("Arm style ? \n")
        torso_style = int(input("Torso length ? \n"))
        leg_style = int(input("Leg length (1-4) ? \n"))
        shoe_style = input("Shoe look ? \n")
        print()
        hat(hat_style)
        face(hair_style, eyes_style)
        arms(arm_style)
        torso(torso_style)
        legs(leg_style, shoe_style)

#call the main function
main()