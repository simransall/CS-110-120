'''
'''
def build_map(filename):
    substitution_map = {}
    open_file = open(filename, 'r')
    for line in open_file.readlines():
        line = line.strip(' ').split()
        # assert the line only has two characters
        assert len(line) == 2
        # assert that each word is a single character
        assert len(line[0]) == 1
        assert len(line[1]) == 1
        substitution_map[line[0]] = line[1]
        duplicates_check = {}
        for key, value in substitution_map.items():
            if value not in duplicates_check:
                duplicates_check[key] = value
            else:
                assert value in substitution_map
        # assert that no key is used twice
    return substitution_map

def is_valid_map(substitution_map):
    # confirm that every thing in dictionary is a string
    for key, value in substitution_map.items():
        assert type(key), type(value) is str
    # confirm that every string is exactly one character long
        assert len(key), len(value) == 1
    # none of the strings should be space, tab or \n
        assert key, value != ' ' or '\t' or '\n'
    # no duplicate "from" characters - keys
