###
### Author: Simran Sall
### Course: CSc 110
### Description: This program takes a text file and spellchecks it.
###              If a word is spelled wrong in the file, the program
###              will recognize it and do one of two options: replace
###              or suggest. In replace mode, the program will automatically
###              replace the wrongly spelled word with the correctly spelled
###              version. In suggest mode, the program will identify the
###              wrongly spelled words in a list and suggest what the correct
###              version is.
###

def read_misspelling(misspelling):
    ''' This function reads the misspelling file that contains all the
    incorrectly spelled words with the correct spellings. It then takes
    those words and adds them to a dictionary.
    misspelling: this is the empty dictionary in which the words will be added to.
    '''
    misspelling_txt = open('misspellings.txt', 'r')
    for words in misspelling_txt:
        #take away the extra characters to evaluate the words
        words = words.strip('\n').split(':')
        i = 1
        for i in range (1, len(words)):
            # the keys are the words to the right of the colon,
            # the correctly-spelled word is to the left of the colon,
            # or at index 0.
            misspelling[words[i]] = words[0] # add values to dictionary
    return misspelling

def replace(misspelling, words_text):
    ''' This function defines the replace mode, and will be called
    if the user wants to replace the wrong words with the correct ones
    rather than suggest replacements.
    misspelling: the dictionary that will be referenced to determine
    if the word in the text file is incorrectly spelled or not.
    words_text: the text file that the user inputs; this is referenced
    and is the text that will be spellchecked.
    '''
    print('\n' + '--- OUTPUT ---')
    # initialize boolean value
    boolean = True
    for i in words_text:
        # take away extra characters to evaluate word
        for word in i.strip('\n').split(' '):
            for key in misspelling:
                # save the original misspelled word as variable
                original_word = word
                if word.lower() in key.split(","):
                    # evaluate if first letter of word is uppercase
                    if original_word[0].isupper():
                        print(misspelling[key].capitalize() + ' ', end='')
                    else:
                        print(misspelling[key] + ' ', end='')
                    boolean = False
            if(boolean):
                print(word + ' ', end='')
            boolean = True
        print()

def suggest(misspelling, words_text):
    ''' This function defines the suggest mode, and will be called
    if the user wants to suggest what the wrong words are rather than
    automatically replace the words with the correctly spelled words.
    misspelling: the dictionary that will be referenced to determine
    if the word in the text file is incorrectly spelled or not.
    words_text: the text file that the user inputs; this is referenced
    and is the text that will be spellchecked.
    '''
    print('\n' + '--- OUTPUT ---')
    boolean = True
    j = 1
    correct_words = []
    for i in words_text:
        # take away extra characters to evaluate word
        for word in i.strip('\n').split(' '):
            for key in misspelling:
                # save the original misspelled word as a variable
                original_word = word
                if word.lower() in key.split(","):
                    # evaluate if first letter of word is uppercase
                    if original_word[0].isupper():
                        print(original_word + ' (' + str(j) + ') ', end='')
                        j += 1
                        # append the capitalized version to the list so it
                        # will print correctly in the legend
                        correct_words.append(misspelling[key].capitalize())
                    elif original_word[0].islower():
                        print(word + ' (' + str(j) + ') ', end='')
                        j += 1
                        # append the correct version of the word to the list
                        # so it can print in the legend
                        correct_words.append(misspelling[key])
                    else:
                        print(word + ' ', end='')
                    boolean = False
            if(boolean):
                print(word + ' ', end='')
            boolean = True
        print()
    print('\n'+ '--- LEGEND ---')
    j = 1
    i = 0
    for word in correct_words:
        original_word = word
        if original_word[0].islower():
            print('(' + str(j) + ') '+ correct_words[i])
            j += 1
            i += 1
        elif original_word[0].isupper():
            # must capitalize the first letter
            print('(' + str(j) + ') '+ correct_words[i].capitalize())
            j += 1
            i += 1

def main():
    input_file = input('Enter input file: \n')
    spellcheck = input('Enter spellcheck mode (replace or suggest): \n')
    misspelling = {}
    words_text = open(input_file, 'r')
    read_misspelling(misspelling)
    if spellcheck == 'replace':
        replace(misspelling, words_text)
    else:
        suggest(misspelling, words_text)

main()