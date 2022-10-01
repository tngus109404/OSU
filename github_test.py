from random import randint


def qselect(i, array):
    if len(array) > 0:
        index = randint(0, len(array) - 1)
        print(index)
        array[0], array[index] = array[index], array[0]
        pivot = array[0]
        left = [x for x in array if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        array = left + [pivot] + right
        print(array)
        k = len(left) + 1
        if i == k:
            return pivot
        elif i < k:
            return qselect(i, left)
        else:
            return qselect(i - k, right)


a=qselect(3,[6,1,8,2])
print(a)
