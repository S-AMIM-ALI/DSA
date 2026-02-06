def binary(item,list1):
    n=len(list1)
    ln=sorted(list1)
    return binary_search(item,ln,0,n-1)
def binary_search(item,ln,lower,upper):
    if lower>upper:
        return {f"messgaes":"elements {item} not found"}
    mid=(lower+upper)//2
    if item==ln[mid]:
        return {"messgaes":f"elements {item}  found at position {mid}"}
    elif item<ln[mid]:
        return binary_search(item,ln,lower,mid-1)
    else:
        return binary_search(item,ln,mid+1,upper)

lst = [10, 4, 7, 1, 9, 3]
print(binary(7, lst))
