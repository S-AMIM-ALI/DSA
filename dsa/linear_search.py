def linear(item,list1):
    for e in list1:
        if e==item:
            return{f"elements {e} is found at location{list1.index(e)}"}
    return IndexError("element not found")
list1=[12,22,33,123,112,11,66]
item=11
print(linear(item,list1))
