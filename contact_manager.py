###
### Author: Simran Sall
### Course: CSc 110
### Description: This program allows a user to save, add, and
###              access contacts. The user can input commands
###              such as adding or showing a contact and the
###              the program will act upon the command.
###

def open_file(contacts_set):
    '''This function opens the text file that has all of the
    contacts and adds each person's contact info into a set of
    tuples.
    contacts_set: this is the empty set in which all of the
        contacts will be added to.
    '''
    #open the contacts file and read through it
    open_file = open('contacts.txt', 'r')
    for info in open_file:
        #strip file to isolate the strings
        info = info.strip('\n').split(' | ')
        #add all values to a set of tuples
        contacts_set.add((info[0], info[1], info[2]))
    return contacts_set

def add_contacts(contacts_set):
    '''This function is for one of the commands that the
    user can input. If the user wants to add a contact, this
    function will run. It will add the name, email, and
    phone number of the new contact. If the contact already
    exists, the program will notify the user.
    contacts_set: the set of contact information in which the
        new contacts will be added to.
    '''
    #user can input contact information
    name = input('name: \n')
    email = input('email: \n')
    phone = input('phone: \n')
    #check to see if contact already exists
    check_tuple = (name, email, phone)
    if check_tuple in contacts_set:
        print('Contact already exists!')
    else:
        #add contact if doesn't already exist
        contacts_set.add((name, email, phone))
        print('Contact added!')
    contacts_set.add((name, email, phone))

def show_contacts(contacts_set, split_command):
    '''This function is for one of the commands that the
    user can input. If the user wants to show a contact, this
    function will run. It will show the name, email, and phone
    number of the contact the user wants shown. If there are
    no matching contacts, the program will notify the user by
    displaying "none".
    contacts_set: the set of contact information that will
        be used to compare all of the matches
    split_command: this splits the string that the user inputs
        in order to isolate the last strings that are the name.
        This is used to ultimately check if the user inputs
        a first name or both a first and last name.
    '''
    #split the command string that the user inputs to isolate the name
    names_split = split_command[4:]
    #create a new set that consists of all of the matches found
    matches = set()
    #iterate through the set of contacts
    for i in contacts_set:
        #check if the user inputs only the first name or both first and last.
        if len(names_split) == 1:
            for j in names_split:
                #add the info of the name, email, or phone number.
                #depends on what the user inputs.
                if j == i[0]:
                    matches.add(i)
                elif j == i[1]:
                    matches.add(i)
                elif j == i[2]:
                    matches.add(i)
        #if user inputs first and last names, rejoin the strings together
        else:
            join_names = ' '.join(names_split)
            if join_names == i[0]:
                matches.add(i)
    #display the matching contact information
    for contact in sorted(matches):
        print(contact[0] + "'s " + 'contact info:')
        print('  email: ' + contact[1])
        print('  phone: ' + contact[2])
    #print none if no matches
    if len(matches) == 0:
        print('None')

def main():
    contacts_set = set()
    open_file(contacts_set)
    add_contact = 'add contact'
    show_input = 'show contacts with'
    print('Welcome to the contacts app!')
    command = ''
    while command != 'exit':
        command = input('> \n')
        if command == add_contact:
            add_contacts(contacts_set)
        elif show_input in command:
            split_command = command.split(' ')
            show_contacts(contacts_set, split_command)
        elif command == 'exit':
            print('Goodbye!')
        elif command != add_contact and show_input not in command and command != 'exit':
            print('Huh?')
    save_file = open('contacts.txt', 'w')
    for contacts in sorted(contacts_set):
        save_file.write(contacts[0] + ' | ' + contacts[1] + ' | ' + contacts[2] + '\n')
    save_file.close()

main()