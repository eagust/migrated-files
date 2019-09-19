# @lst : the lst that needs to be sorted
# @start: the index of each recursion
# @length: the size of the lst

def selectionSort(lst, start, length):
    if start == length - 1:
        return lst


    min = lst[start]
    index = start

    for i in range(start, length):
        if lst[i] < min:
            min = lst[i]
            index = i

    popVal = lst.pop(index)
    lst.insert(start, popVal)
    selectionSort(lst, start + 1, length)

A = [4,5,90,8,1]
selectionSort(A,0,len(A))

print(A)