def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    return sum(([i] if not isinstance(i, list) else flatten(i) for i in aList), [])
