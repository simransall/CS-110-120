def create_dict(rhym_words, openfile):
    for word in openfile:
        word = word.upper()
        word = word.split()
        phonemes = word[1:]
        if word[0] in rhym_words:
            for key, value in rhym_words.items():
                rhym_words[word[0]].append(phonemes)
        else:
            rhym_words[word[0]] = [word[1:]]
    return rhym_words

def identical_phoneme(ident_words, rhym_words):
    for key, value in rhym_words.items():
        index_count = 0
        if len(value) >= 2:
            for i in value:
                for j in i:
                    if '1' in j:
                        if '1' in (rhym_words[key])[0]:
                            ident_words[key]=(rhym_words[key])[index_count-1:]
                        else:
                            ident_words[key] = (rhym_words[key])[index_count-2:]
        else:
            for values in rhym_words[key]:
                index_count += 1
                for i in values:
                    if '1' in i:
                        if '1' in (rhym_words[key])[0]:
                            ident_words[key] = (rhym_words[key])[index_count-1:]
                        else:
                            ident_words[key] = (rhym_words[key])[index_count-2:]
    return ident_words

def findrhyme_1(word1, ident_words, rhymes_1):
    for key in ident_words:
        for value in ident_words[key]:
            if (ident_words[word1])[0][0] != (ident_words[key])[0][0]:
                if '1' in (ident_words[word1])[0][0] and (ident_words[key])[0][0]:
                    if (ident_words[word1])[0:] == (ident_words[key])[0:]:
                        rhymes_1.append(key)
                else:
                    if (ident_words[word1])[1:] == (ident_words[key])[1:]:
                        rhymes_1.append(key)
            else:
                continue
    print(rhymes_1)
    return rhymes_1

def findrhyme_2(word2, ident_words, rhymes_2):
    for key in ident_words:
        if (ident_words[word2])[0] != (ident_words[key])[0]:
            if '1' in (ident_words[word2])[0] and (ident_words[key])[0]:
                if (ident_words[word2])[0:] == (ident_words[key])[0:]:
                    rhymes_2.append(key)
            else:
                if (ident_words[word2])[1:] == (ident_words[key])[1:]:
                    rhymes_2.append(key)
        else:
            continue
    return rhymes_2

def findrhyme_3(word3, ident_words, rhymes_3):
    for key in ident_words:
        if (ident_words[word3])[0] != (ident_words[key])[0]:
            if '1' in (ident_words[word3])[0] and (ident_words[key])[0]:
                if (ident_words[word3])[0:] == (ident_words[key])[0:]:
                    rhymes_3.append(key)
            else:
                if (ident_words[word3])[1:] == (ident_words[key])[1:]:
                    rhymes_3.append(key)
        else:
            continue
    return rhymes_3

def print_rhymes(rhymes_1, rhymes_2, rhymes_3, word1, word2, word3):
    print('Rhymes for: ' + word1)
    if len(rhymes_1) == 0:
            print('--none found--')
    else:
        for word in rhymes_1:
            print(word)
    print()

    print('Rhymes for: ' + word2)
    if len(rhymes_2) == 0:
            print('--none found--')
    else:
        for word in rhymes_2:
            print(word)
    print()

    print('Rhymes for: ' + word3)
    if len(rhymes_3) == 0:
            print('--none found--')
    else:
        for word in rhymes_3:
            print(word)
    print()

def main():
    filename = 'testcasenotworking.txt'#input()
    openfile = open(filename, 'r')
    rhym_words = {}
    ident_words = {}
    rhymes_1 = []
    rhymes_2 = []
    rhymes_3 = []
    create_dict(rhym_words, openfile)
    identical_phoneme(ident_words, rhym_words)
    word1 = 'HOWEVER'#input().upper()
    word2 = 'PURSE'#input().upper()
    word3 = 'WORSE'#input().upper()
    findrhyme_1(word1, ident_words, rhymes_1)
    findrhyme_2(word2, ident_words, rhymes_2)
    findrhyme_3(word3, ident_words, rhymes_3)
    print_rhymes(rhymes_1, rhymes_2, rhymes_3, word1, word2, word3)

if __name__ == "__main__":
    main()