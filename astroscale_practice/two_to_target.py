
# Return the indices of the first two numbers that make up the target
def two_to_target(arr,tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == tar:
                return[i,j]

def two_target(tar, arr):
    for x in arr:
        for y in arr:
            xidx = arr.index(x)
            yidx = arr.index(y)
            if x + y == tar and not xidx == yidx:
                return xidx, yidx
    print(f"No values in the array equals {tar}!")

if __name__ == "__main__":
    tar = 9
    arr = [1,2,3,4,5]
    
    print(two_to_target(arr,tar))
    print(two_target(tar,arr))