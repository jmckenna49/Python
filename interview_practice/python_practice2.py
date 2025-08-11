def two_to_target(arr, target):
    seen = {}
    for i,num in enumerate(arr):
        compliment = target - num
        if compliment in seen:
            # return compliment, num
            return [seen[compliment],i]
        seen[num] = i
    return None

print(two_to_target(arr=[1,2,4,5],target=6))

def dup_arr_compare(arr1,arr2):
    dups = []
    for num in arr1:
        if num in arr2 and ( num not in dups):
            dups.append(num)
    return dups
arr1 = [1,2,3,4,5,1]
arr2 = [1,1,4,5,2]
print(dup_arr_compare(arr1,arr2))

def remove_dup_element(arr=[1,1,2,3,4],val=1):
    k = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k+=1
    return k,arr[:k]
print(remove_dup_element())

def remove_duplicates_sorted_array(nums=[1,1,2,3,4]):
    l = 1
    for r in range(1,len(nums)):
        if nums[r] != nums[l-1]:
            nums[l]=nums[r]
            l+=1
    return l, nums[:l]
print(remove_duplicates_sorted_array())


def roman_numerals(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for x in reversed(s):
        cur_value = roman_map[x]
        if cur_value < prev_value:
            total -= cur_value
        else:
            total += cur_value
        prev_value = cur_value
    return total
chee=roman_numerals("MCXIV")
print(chee)


def reverse_arr(arr):
    rev_arr = []
    for x in arr:
        rev_arr = [x] + rev_arr
    return rev_arr
print(reverse_arr(arr=[1,2,3,4,5]))    



def reverse_str(s="Hello"):
    rev_str = ""
    for c in s:
        rev_str = c + rev_str
    return rev_str
print(reverse_str())


def isValid(s="([{}])"):
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    return s == ''      
print(isValid())


def isPalindrome(s):
    rev_str = ""
    lower_str = s.lower()
    for c in lower_str:
        rev_str = c + rev_str
    if lower_str == rev_str:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
isPalindrome(s="racecar")
isPalindrome(s="Hello")
isPalindrome(s="Racecar")


def iterative_factorial(n=5):
    result = 1
    for i in range(2,n+1):
        result*=i
    return result
print(iterative_factorial(n=5))

def recursive_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n*recursive_factorial(n-1)
print(recursive_factorial(6))


def reverse_list(arr=[1,2,3,4,5]):
    rev_stack = []
    while len(arr) > 0:
        # pop removes and returns the top of the stack, LIFO
        rev_stack.append(arr.pop())
    return rev_stack
print(reverse_list())

