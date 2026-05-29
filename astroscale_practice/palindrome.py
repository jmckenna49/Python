
def palindrome(string_word):
    left = 0
    right = len(string_word) - 1
    while left < right:
        if string_word[left] == string_word[right]:
            left += 1
            right -= 1
        else:
            print("Not a palindrome")
            return
    print("Its a palindrome")

def palindrome2(string_cheese):
    if string_cheese == string_cheese[::-1]:
        print("Its a boy!")
    else:
        print("It's not a boy....or a grill...")
        
def palindrome3(string_cheese):       
    reversey_str = ""
    for c in range(len(string_cheese)-1,-1,-1):
        reversey_str += string_cheese[c]
    if string_cheese == reversey_str:
        print("Its a grill!")
    else:
        print("Its disgusting, its a child.")

if __name__ == "__main__":
    string_word = "cheese"
    string_word2 = "racecar"
    palindrome(string_word)
    palindrome(string_word2)

    palindrome2(string_word2)
    palindrome2(string_word)
    
    palindrome3(string_word2)
    palindrome3(string_word)