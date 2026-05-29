

def remove_dups(arr1,arr2):
    arr3=[]
    for x in arr1:
        if x not in arr2:
            arr3.append(x)

    for y in arr2:
        if y not in arr3:
            arr3.append(y)
    arr3.sort()
    return arr3

if __name__ == "__main__":
    arr1=[1,2,3,4,5]
    arr2=[3,6,7,5,8,9]
    print(remove_dups(arr1,arr2))
