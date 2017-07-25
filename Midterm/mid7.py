def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersection = d1.keys() & d2.keys()
    merge = {**d1, **d2}
    dict1 = {}
    dict2 = {}

    for i in intersection:
        dict1[i] = f(d1[i], d2[i])

    for i in merge:
        if i in intersection:
            pass
        else:
            dict2[i] = merge[i]

    result = (dict1, dict2)

    return result
