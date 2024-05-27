# 2.Merge Sort

def sort(lst, low, high):
    if low >= high:
        return
    mid = (low+high)//2
    sort(lst, low, mid)
    sort(lst, mid+1, high)
    merge(lst, low, high, mid)
    return lst


def merge(lst, low, high, mid):
    li, ri = 0, 0
    ll, rl = lst[low:mid+1], lst[mid+1:high+1]
    k = low
    while (li < len(ll)) and (ri < len(rl)):
        if ll[li] < rl[ri]:
            lst[k] = ll[li]
            li += 1
        elif ll[li] > rl[ri]:
            lst[k] = rl[ri]
            ri += 1
        k += 1
    while li < len(ll):
        lst[k] = ll[li]
        li += 1
        k += 1
    while ri < len(rl):
        lst[k] = rl[ri]
        ri += 1
        k += 1
    return


lst1 = [15, 20, 5, 30, 45, 17, 40, 25, 31]
l = [15, 18, 25, 32, 8, 16, 48, 35]
l = sort(lst1, 0, 8)
print(l)
