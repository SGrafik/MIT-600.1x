def dotProduct(listA, listB):
    '''
    Returns the sum of listA[0] * listB[0] + listA[1] * listB[1] etc...
    ** Lists must both be of the same length **
    '''
    result = 0

    for i, item in enumerate(listA):
        result += listA[i] * listB[i]

    return result
