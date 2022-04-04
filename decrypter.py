###
### Author: Simran Sall
### Course: CSc 110
### Description: This program takes the file's encrypted contents
###              and puts it in the correct order again, so it can
###              be understood. It does this by using the index file
###              to place the contents back in the correct order.
###

def decryption_algorithm(encrypted_file, index_file, decrypted_file):
    '''This function defines the algorithm that rearranges the
    encrypted file back to the original order. This function takes
    3 parameters.
    encrypted_file: the file with the encrypted contents.
    index_file: the file that shows the line number of the encrypted contents.
    decrypted_file: text file that the original contents will be added to
    once the decryption algorithm is run.
    '''
    decrypted_list = []
    list_encrypted = encrypted_file.readlines()
    line_count = len(list_encrypted)
    list_file = index_file.readlines()
    #initializing the decrypted list so that the correct contents can be added to it.
    i = 0
    while i < (line_count+1):
        decrypted_list.append(' ')
        i += 1
    #add correct contents to decrypted list
    j = 0
    for index in list_file:
        decrypted_list[int(index)-1] = list_encrypted[j]
        j += 1
    i = 0
    #write contents to the decrypted file (should match the original contents)
    for i in decrypted_list:
        decrypted_file.write(i)
    decrypted_file.close()

def main():
    name_encrypted = input('Enter the name of an encrypted text file: ')
    print()
    name_file = input('Enter the name of the encryption index file: ')
    print()
    encrypted_file = open(name_encrypted, 'r')
    index_file = open(name_file, 'r')
    decrypted_file = open('decrypted.txt', 'w')
    decryption_algorithm(encrypted_file, index_file, decrypted_file)

main()