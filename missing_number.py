# A program that takes in a list of arbitrary numbers and outputs a missing number in the sequence.
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 26 March 2025

num = input("Enter an array of numbers (separated by spaces):\n")

arr = list(map(int, num.split())) #Putting input into a list and converting from string to integer


mini_num = min(arr)
max_num = max(arr)

expected = 0        # this ismthe variable for the sum of array with the missing number
actual = sum(arr)   # The sum of the array before the missing value

for x in range(mini_num, max_num + 1):
   expected += x
    
missing_num = expected - actual

if missing_num == 0:
   print("There is no missing number.")
else:
   print(f"Missing number: {missing_num}")
