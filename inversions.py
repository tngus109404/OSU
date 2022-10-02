def num_inversions(list):
    inversion = 0
    print(merge(list,inversion))

def merge(list,inversion):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        inversion=merge(left,inversion)
        inversion+=merge(right,inversion)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
                lele=len(left)-i
                inversion+=lele
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        return inversion
    else:
        return 0
