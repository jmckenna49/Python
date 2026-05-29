
# HELP ME CODE I AM STUPID STELLA, PEAS AND THANK YOU :)

def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def reverse2(arr):
    reversey_arr = []
    for num in range(len(arr),0,-1):
        reversey_arr.append(num)
    return reversey_arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(reverse(arr))
    
    arr2=[1,2,3,4,5]
    print(reverse2(arr2))
    
    arr3= [1,2,3,4,5]
    arr3.sort(key=None, reverse=True)
    print(arr3)