""" Which gives best readability? """


def qsort(l):
    return qsort([x for x in l[:int(len(l)/2)]+l[int(len(l)/2)+1:] if x <= l[int(len(l)/2)]]) + [l[int(len(l)/2)]] + qsort([x for x in l[:int(len(l)/2)]+l[int(len(l)/2)+1:] if x > l[int(len(l)/2)]]) if len(l) not in [0, 1] else l


def qsort2(l):
    if len(l) in [0, 1]:
        return l

    mid_index = int(len(l)/2)
    mid_elem = l[mid_index]
    exluding_list = l[:mid_index]+l[mid_index + 1:]

    left_list = qsort2([elem for elem in exluding_list if elem <= mid_elem])
    right_list = qsort2([elem for elem in exluding_list if elem > mid_elem])

    return left_list + [mid_elem] + right_list


print(qsort2([1, 5, 3, 4, 1, 2]))
