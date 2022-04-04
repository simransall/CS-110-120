###
### Author: Simran Sall
### Course: CSc 110
### Description: This program takes an inputted text file and reads it. It
###              then produces an infographic based on the words of the text.
###              This infographic includes information about the words of the
###              text, like how many unique words there are, what proportion
###              of words are capitalized vs non-capitalized, and the proportion
###              of small words to medium and large words.
###

from graphics import graphics

def organize_file_contents(file_contents, file_reading):
    '''This function takes the file that the user inputs and
    it reads its lines and creates a list of all of the words
    in that file (including repeated words).
    file_contents: this is what opens the inputted file to read it

    file_reading: this is an empty list in which all of the words
        in the text file will be added to it.
    '''
    read_file = file_contents.readlines()
    for line in read_file:
        word = line.strip('\n').split()
        for individual_word in word:
            file_reading.append(individual_word)

def counting_words(count, file_reading, small, medium, large,\
max_small_val, max_med_val, max_large_val):
    '''This function keeps track of all of the words, including
    the length of each word in the file. It adds all of the words to
    a dictionary as a key, and the value is the amount of times that
    word occurs in the text file.
    count: the empty dictionary in which all of the words and the amount
        of times that word occurs will be added.

    file_reading: the list created in the organize_file_contents function
        that the for loop will be referencing to add the words to the dictionary.

    small: empty dictionary to keep track of how many unique small words
        are in the text file and how many times they occur.

    medium: empty dictionary to keep track of how many unique medium words
        are in the text file and how many times they occur.

    large: empty dictionary to keep track of how many unique large words
        are in the text file and how many times they occur.

    max_small_val: this is to keep track of the unique small word that appears
        the most in the text file (how many times that word occurs).

    max_med_val: this is to keep track of the unique medium word that appears
        the most in the text file (how many times that word occurs).

    max_large_val: this is to keep track of the unique large word that appears
        the most in the text file (how many times that word occurs).
    '''
    for word in file_reading:
        #if the word is in the dictionary, increase the count it occurs by 1
        if word in count:
            count[word] += 1
            #consider if the word is small, medium, or large
            if len(word) >= 0 and len(word) <= 4 and word not in small:
                small[word] = 2
            elif word in small:
                small[word] += 1
            elif len(word) >= 5 and len(word) <= 7 and word not in medium:
                medium[word] = 2
            elif word in medium:
                medium[word] += 1
            elif len(word) >= 8 and word not in large:
                large[word] = 2
            else:
                large[word] += 1
        #if the word is not in the dictionary, add it
        else:
            count[word] = 1
    #find the word with the maximum amount of occurences for small, medium, and large
    for word in small:
        if small[word] > max_small_val:
            max_small_val = small[word]
            max_small_key = word
    for word in medium:
        if medium[word] > max_med_val:
            max_med_val = medium[word]
            max_med_key = word
    for word in large:
        if large[word] > max_large_val:
            max_large_val = large[word]
            max_large_key = word
    max_values=[max_small_val,max_small_key,max_med_val,max_med_key,max_large_val,max_large_key]
    return max_values

def word_length(count, small_word, med_word, large_word, total_word_count):
    '''This function determines the total amount of unique small, medium,
    and large words and then gathers the total amount of unique words. These
    values also help determine the proportions on the bar chart in the bar_charts
    function.
    count: the dictionary that is used to isolate all the keys into a list
        so the keys (the words of the text file) can be evaluated.

    small_word: the variable that be added to depending on if the word in the
        for loop is considered to be a small word.

    med_word: the variable that be added to depending on if the word in the
        for loop is considered to be a medium word.

    large_word: the variable that be added to depending on if the word in the
        for loop is considered to be a large word.

    total_word_count: the total amount of unique small, medium, and large words.
    '''
    isolate all the keys (the words) from the dictionary)
    key_words = []
    for key in count.keys():
        key_words.append(key)
     get each unique small/medium/large word from the count dictionary
    for word in key_words:
        if len(word) >= 0 and len(word) <= 4:
            small_word +=1
        elif len(word) >= 5 and len(word) <= 7:
            med_word += 1
        elif len(word) >= 8:
            large_word += 1
    #find how many total unique words there are
    total_word_count = small_word + med_word + large_word
    list = [small_word, med_word, large_word, total_word_count]
    return list

def capitalization(count, capitalized_words, non_cap_words):
    ''' This function determines how many words in the text
    file are capitalized and how many words in the text file
    are non-capitalized.

    count: the dictionary that is used to isolate all the keys into a list
        so the keys (the words of the text file) can be evaluated.

    capitalized_words: the variable that will be added to depending on
        if the first letter of the word is capitalized.

    non_cap_words: the variable that will be added to if the first letter
        of the word is not capitalized.
    '''
    #isolate the keys from the dictionary that contains all the unique words and
    #their counts.
    key_words = []
    for key in count.keys():
        key_words.append(key)
    for word in key_words:
        #evaluate if the first letter of the word is upper case or not
        if word[0].isupper():
            capitalized_words += 1
        else:
            non_cap_words += 1
    caps_list = [capitalized_words, non_cap_words]
    return caps_list

def bar_charts(input_file,small_word,med_word,large_word,total_word_count,\
capitalized_words,non_cap_words,max_small_val, max_small_key, max_med_val, \
max_med_key, max_large_val, max_large_key):
    '''This function utilizes graphics to create the infographic as an output.
    It will display 2 bar charts about the capitalization and the length of the
    words, how many unique words there are, as well as the most occurring small/
    medium/large word.
    input_file: the name of the input file; used to display the name of the file
        in the infographic.

    small_word: the value calculated from the word_length() function that is used
        to calculate the portion of the bar chart the small words will cover.

    med_word: the value calculated from the word_length() function that is used
        to calculate the portion of the bar chart the medium words will cover.

    large_word: the value calculated from the word_length() function that is used
        to calculate the portion of the bar chart the large words will cover.

    total_word_count: the value calculated from the word_length() function that is used
        in the calculations of the portions of the different word lengths.

    capitalized_words: the value calculated from the capitalization() function that
        is used in the calculations of the portions of the capitalized words.

    non_cap_words: the value calculated from the capitalization() function that
        is used in the calculations of the portions of the non-capitalized words.

    max_small_val: how many times the small word that appears the most in the
        text file occurs.

    max_small_key: the small word that occurs the most in the text file.

    max_med_val: how many times the medium word that appears the most in the
        text file occurs.

    max_med_key: the medium word that occurs the most in the text file.

    max_large_val: how many times the large word that appears the most in the
        text file occurs.

    max_large_key: the large word that occurs the most in the text file.
    '''
    #create the canvas
    gui = graphics(650, 700, 'infographic')
    #display the name of the canvas
    gui.text(30, 30, input_file, 'sea green', 20)
    #display how many total unique words there are
    gui.text(30, 70, 'Total Unique Words:', 'dark slate gray', 15)
    gui.text(215, 70, total_word_count, 'tomato', 15)
    gui.text(30, 100, 'Most used words(s/m/l):', 'dark slate gray', 10)
    #print out most used s/m/l words
    gui.text(190, 100, max_small_key + ' (' + str(max_small_val) + 'x)\t'+\
    max_med_key + ' (' + str(max_med_val) + 'x)  '+\
    max_large_key + ' (' + str(max_large_val) + 'x)', 'sea green', 10)
    #print out titles for the bar graphs
    gui.text(95, 130, 'Word lengths', 'tomato', 15)
    gui.text(350, 130, 'Cap/Non-Cap', 'tomato', 15)
    #calculate the proportions of each type of word
    length_small = (450/total_word_count) * small_word
    length_medium = (450/total_word_count) * med_word
    length_large = (450/total_word_count) * large_word
    capital_proportion = (450/total_word_count) * capitalized_words
    non_cap_proportion = (450/total_word_count) * non_cap_words
    offset = 160
    #print proportion of small, medium, and large words (bar chart)
    length_medium = length_small + length_medium
    length_large = length_medium + length_large
    gui.rectangle(95, offset, 130, length_small, 'pale turquoise')
    gui.rectangle(95, offset + length_small, 130, length_medium, 'medium turquoise')
    gui.rectangle(95, offset + length_medium, 130, length_large, 'dark turquoise')
    #print proportion of capitalized and non-capitalized words (bar chart)
    gui.rectangle(350, offset, 130, capital_proportion, 'pale turquoise')
    gui.rectangle(350, offset + capital_proportion, 130, non_cap_proportion, 'dark turquoise')
    #print labels for each portion of the chart:
    gui.text(95, offset, 'small words', 'white', 10)
    gui.text(95, offset + length_small, 'medium words', 'white', 10)
    gui.text(95, offset + length_medium, 'large words', 'white', 10)
    gui.text(350, offset, 'Capitalized', 'white', 10)
    gui.text(350, offset + capital_proportion, 'Non Capitalized', 'white', 10)
    gui.update_frame(40)

def main():
    input_file = input('Enter file name: ')
    file_contents = open(input_file, 'r')
    file_reading = []
    count = {}
    small = {}
    medium = {}
    large = {}
    small_word = 0
    med_word = 0
    large_word = 0
    max_small_val = 0
    max_med_val = 0
    max_large_val = 0
    total_word_count = 0
    capitalized_words = 0
    non_cap_words = 0
    organize_file_contents(file_contents, file_reading)
    max_value = counting_words(count, file_reading, small, medium, large, \
    max_small_val, max_med_val, max_large_val)
    info = word_length(count, small_word, med_word, large_word, total_word_count)
    cap_info = capitalization(count, capitalized_words, non_cap_words)
    bar_charts(input_file, info[0], info[1], info[2], info[3], cap_info[0], cap_info[1],\
    max_value[0],max_value[1], max_value[2], max_value[3], max_value[4], max_value[5])

main()