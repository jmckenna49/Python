import random

my_dict = {"name" : "Stelly",
 "age" : 28}

my_dict["employment"] = "FTE"
name = my_dict["name"]
age = my_dict["age"]
my_dict["age"] =  29

print(my_dict)

new_dict = {"fruit" : "apple",
 "remove_me" : "please",
 "yummy" : True}

new_dict.pop("remove_me")
print(new_dict)
dic_dic = new_dict
dic_dic["color of apple"] = "red"
print(dic_dic)

school = {
    "Grade 1": {
        "Alice": {"Math": 85, "English": 90},
        "Bob": {"Math": 78, "English": 82}
    },
    "Grade 2": {
        "Charlie": {"Math": 92, "English": 88},
        "Dana": {"Math": 87, "English": 91}
    },
    "Grade 3": {
        "Eve": {"Math": 93, "English": 95},
        "Frank": {"Math": 80, "English": 84}
    }
}

print(school["Grade 1"]["Alice"]["English"])

students = []
scores = []
for grade in school.values():
    for student,score in grade.items():
        students.append(student)
        scores.append(score)
print(students)

def calc_avg_score(school):
    avg_score={}
    for grade in school:
        for student, subjects in school[grade].items():
            average = sum(subjects.values())/len(subjects.values())
            avg_score[student] = average
    return avg_score
average = calc_avg_score(school)
print(average)


def add_subject_score(school, grade, student, subject, score):
    if grade not in school:
        school[grade] = {}
    if student not in school[grade]:
        school[grade][student] = {}
    if subject not in school[grade][student]:
        school[grade][student][subject] = {}
    school[grade][student][subject] = score
    return school
    
y = add_subject_score(school, "Grade 3", "Steve", "Math", 90)
print(y)
y = add_subject_score(school, "Grade 4", "Sally", "Science", 70)
print(y)

def guessing_game():
    correct_num = random.randint(1, 10)
    num = int(input("Pick a number between 1 and 10: "))
    guesses = 0
    while correct_num != num:
        
        if num > correct_num:
            print("Value is above the correct number.")
        else:
            print("Value is below the correct number.")
        if correct_num == num:
            break
        guesses+=1
        print(f"You're on {guesses} guesses so far.")
        num = int(input("Pick a new number between 1 and 10: "))

    print("Congrats you guessed the right number!")
    
    
    
pali_arr = ["wee", "James", "racecar", "no on"]

def is_palindrome(pali_arr=pali_arr):
    for x in pali_arr:
        print(f"Checking: {x}")
        i = 0
        j = len(x) - 1
        is_pal = True
        while i < j:
            if x[i] != x[j]:
                print(f"{x} is NOT a palindrome")
                is_pal = False
                break
            i += 1
            j -= 1
        if is_pal:
            print(f"{x} IS a palindrome")
is_palindrome()


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

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value: # do a check to see if the previous value is lower than the current, if so we subtract i.e IX, IV, XL
            total -= value  # Subtract if smaller (like IV = 5 - 1)
        else:
            total += value  # Otherwise add it
        prev_value = value

    return total
chee=roman_numerals("MCXIV")
print(chee)

arr = [1,11,6,3,9,2]

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Temporarily store the next node, if 1->2->3->4->None, and we're on 1, next_node saves 2
        current.next = prev       # Reverse the current node's pointer, 1->None, breaks link to 2
        prev = current            # Move `prev` to the current node, last none in the reversed list
        current = next_node       # Move to the next node in the list, this now points at 2

    return prev  # `prev` becomes the new head of the reversed list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original linked list:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed linked list:")
print_linked_list(reversed_head)




def rev_char(string_var):
    rev_s = ""
    for c in string_var:
        rev_s = c + rev_s
    return rev_s
x = rev_char("Hello")
print(x)


def arr_compare(arr1, arr2):
    dups = []
    for x in arr1:
        for y in arr2:
            if ((y in arr1) and (y not in dups)):
                dups.append(y)
    return dups
arr1=[1,2,3,4,5,8]
arr2=[1,3,1,5,4,6,7,8,9]

dips = arr_compare(arr1, arr2)
print(dips)


def palindrome(stringy):
    rev_stringy = ""
    
    for s in stringy:
        rev_stringy = s + rev_stringy    
    if(rev_stringy != stringy):
        print(f"{stringy} is not a palindrome")
    else:
        print(f"{stringy} is a palindrome")
stringy = "racecar"
e = palindrome(stringy)

def two_to_target(arr, target):
    seen = {}
    for i,num in enumerate(arr):
        compliment = target - num
        
        if compliment in seen:
            return compliment,num
            # return [seen[compliment],i]
        seen[num]=i
        print(seen)
    return None
arr = [1,2,3,4,5]
target = 9
yus = two_to_target(arr, target)
print(yus)            

def roman_nums_to_int(stronk):
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
    cur = 0
    
    for s in reversed(stronk):
        value = roman_map[s]
        if value < cur: # if cur value less than cur
            total -= value
        else:
            total += value  # Otherwise add it
        cur = value
    return total

chee=roman_nums_to_int("MCXIV")
print(chee)