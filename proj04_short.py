def compare_front(param1,param2):
    assert type(param1) == type(param2)
    similarities = 0
    i = 0
    if len(param1) < len(param2):
        while i < len(param1):
            if param1[i] == param2[i]:
                similarities += 1
            else:
                break
            i += 1
        return similarities
    else:
        while i < len(param2):
            if param1[i] == param2[i]:
                similarities += 1
            else:
                break
            i += 1
        return similarities

def compare_back(param1,param2):
    assert type(param1) == type(param2)
    similarities = 0
    i = -1
    j = 0
    if len(param1) < len(param2):
        while j < len(param1):
            if param1[i] == param2[i]:
                similarities += 1
            i -= 1
            j += 1
    else:
        while j < len(param2):
            if param2[i] == param1[i]:
                similarities += 1
            i -= 1
            j += 1

    return similarities

def primary_stress(phenome):
    assert type(phenome) == list
    assert len(phenome) != 0
    for i in phenome:
        assert i != ''
    index_count = 0
    for stress in phenome:
        index_count += 1
        if '1' in stress:
            return index_count-1
    return None