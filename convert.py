###
### Author: Simran Sall
### Course: CSc 110
### Description: This program evaluates a text file to
###              take a word that is not in the English
###              language and convert it to English. The
###              user will input both a text file that has
###              the English word and its different translations,
###              as well as the word that the user wants
###              translated into English.
###

def get_word_conversions(words_file_name):
    ''' This function takes the text file that the user inputs
    as a parameter and evaluates it. It iterates through the text
    file and will add the translations to a dictionary so that it
    can be referenced in the print_conversion function.
    words_file_name: the text file that is inputted by the user.
    '''
    conversions = {}
    conversion_file = open(words_file_name, 'r')
    for definitions in conversion_file:
        definitions = definitions.strip('\n').split(',')
        i = 1
        for i in range (1, len(definitions)):
            conversions[definitions[i]] = definitions[0]
    return conversions

def print_conversion(word, conversions):
    ''' This function prints out the English definition of
    the word that the user inputs. The parameters are word
    and conversions.
    word: the inputted string by the user that is the term
    in another language.
    conversions: the dictionary that the program will reference
    when printing out the English definition of the word.
    '''
    if word in conversions:
        print('\n' + 'English version is: ' + conversions[word])
    else:
        print('\n' + 'Not sure.')

def main():
    file_name = input('Enter name of words file:\n')
    conversions = get_word_conversions(file_name)

    word = input('Enter word to convert to English:\n')
    print_conversion(word, conversions)

main()