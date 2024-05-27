# 1.Min & Max of an array using divide & conquer

def MaxMin(i, j, min, max):
    if i == j:
        min = max = arr[i]
        return max, min

    elif (i == j-1):
        if arr[i] < arr[j]:
            min = arr[i]
            max = arr[j]
        else:
            min = arr[j]
            max = arr[i]

    else:
        mid = (i+j)//2

        min1, max1 = MaxMin(i, mid, min, max)
        min2, max2 = MaxMin(mid+1, j, min, max)

        if min1 <= min2:
            min = min1
        else:
            min = min2

        if max1 <= max2:
            max = max2
        else:
            max = max1

    return min, max


# arr=list(map(int,input().split()))
arr = [4, 5, 2, 9, 1]
result = MaxMin(0, 4, 0, 0)
print(result)
