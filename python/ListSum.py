#sort with merge of sublists with a base number

#split to sublists first then sort each then merge

def listSum(L):
    """Returns a sum of integers for a list containing
    integers.
    input: list of integers
    output: listSum returns a sum of all the integers
    in L.
    """
    if L == []:
        return []
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + listSum(L[1:])
print (listSum([1, 3, 4, 5, 6]))
print (listSum([]))
print (listSum([8]))
