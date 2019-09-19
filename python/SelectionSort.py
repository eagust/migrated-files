#Selection sort

def find_min(list, x,length):
    i = 0
    n = 0

    while i < length - (1):
        min = i
        while i+1 < length:
            if list[i] < list[i+1]:
                min = list[i]
                print(min, "is smaller")
            else:
                min = list[i+1]
                print(min, "is smaller2")
            i += 1

    a, b = x, list.index(min)
    list[a], list[b] = list[b], list[a]
    n += 1

    print("iteration", n ,A)

    find_min(A[1:],1,len(A[1:]))

    return list


A = [75, 30, 9, 14, 1, 18]
min_list = find_min(A,0,len(A))
print("The sorted list is:", min_list)

""" i = list[0]
    for j in list[1:]:
        if j < i:
            n += 1
            a,b = list.index(i), list.index(j)
            list[a],list[b] = list[b],list[a]
            print("iteration", n, list)
        else:
            n += 1
            print("iteration", n, list)

    Selection_sort(A)"""