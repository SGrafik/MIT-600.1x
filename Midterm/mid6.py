def deep_reverse(L):
    """
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    """
    for i in L:
        i = i.reverse()

    L = L.reverse()
