# Write a function fizzbuzz(n) that returns a list of strings from 1 to n where:
# Multiples of 3 print fizz, multiples of 5 print buzz, multiples of both print fizzbuzz, and otherwise the number prints out as a string

def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
if __name__ == "__main__":
    fizz_buzz(15)
