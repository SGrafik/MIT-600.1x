def longest_run(L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    def mCount(L):
    count=1

    maxCount=0
    for i in range(len(L)-1):
        if L[i+1] >= L[i]:
            count +=1
        else:

            count =1
        if maxCount<count:
            maxCount=count
    return maxCount
longest_run()
