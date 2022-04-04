'''File: music_compare.py
   Author: Simran Sall
   Purpose: to give a summary of the input file as to what
   songs are the most similar
'''

from utils import *

def main():
    filename = input('file: ')
    song_length = input('n: ')
    openfile = open(filename, 'r')
    tuple_list = read_file(openfile)
    print('--- SONG LIST ---')
    for i in tuple_list:
        print('id='+str(i[0])+' info="'+i[1]+'" notes='+str(i[2]))
    print()
    print('--- COMPARISONS ---')
    most_similar = 0
    for i in tuple_list:
        for j in tuple_list:
            song1 = i[1]
            song2 = j[1]
            song1_notes = i[2]
            song2_notes = j[2]
            if song1 == song2:
                break
            else:
                j_index = compare_sets(song1_notes, song2_notes)
            if most_similar < j_index:
                if song1 == song2:
                    break
                else:
                    most_similar = j_index
                    song1 = i[1]
                    song2 = j[1]
            else:
                most_similar = most_similar
                song1 = song1
                song2 = song2
            print('id_a='+str(i[0])+' id_b='+str(j[0])+' similarity='+str(j_index))
    print()
    print('--- RESULT ---')
    print('Most similar songs:' + '\n' + song1 + '\n' + song2)
    print('ids: ' + str(i[0]) + '\n' + 'ids: ' + str(j[0]) + '\n')
    print('Melodies:')
    for i in song1_notes:
        print(i + ' ', end='')
    print()
    for i in song2_notes:
        print(i + ' ', end='')
    print()
    print('Set 1:')
    print(str(song1_notes))
    print('Set 2:')
    print(str(song2_notes))

main()