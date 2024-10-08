def index_of_by_index(word, list, index):
    if not word in list[index:]: return -1
    for i, e in enumerate(list[index:]):
        if e == word:
            break
    return len(list[:index]) + i

def index_of_empty(list):
    if not '' in list: return -1
    for i, e in enumerate(list):
        if e == '':
            break
    return i


def index_of(word, list):
    if not word in list: return -1
    for i, e in enumerate(list):
        if e == word:
            break
    return i


def put(word, list):
    if not '' in list: return -1
    for i, e in enumerate(list):
        if e == '':
            break
    list[i] = word
    return i


def remove(word, list):
    if not word in list: return 0
    count = 0
    for i, e in enumerate(list):
        if e == word:
            list[i], count = "", count +1
    return count
