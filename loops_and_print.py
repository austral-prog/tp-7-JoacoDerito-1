def enumerate_list(list):
    result = []
    for a in list:
        if not a: continue
        result += [f'{len(result)}. {a}']
    
    return result


def enumerate_backwards(list):
    result = []
    for a in list:
        if not a: continue
        result += [f'{len(result)}. {a[::-1]}']
    
    return result
