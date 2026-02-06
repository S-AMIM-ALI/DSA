def bs(arr):
    n=len(arr)
    for i in range(n-1):
        swap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
    return arr
num=[22,12,31,222,45]
print(bs(num))