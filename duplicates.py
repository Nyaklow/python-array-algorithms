# A program in which the user can enter a list of values and these values are then printed in the same order but without duplicates. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 26 March 2025

num = str(input("Enter an array of numbers (separated by spaces):\n"))
user_arr = [int(num) for num in num.split()] # This puts input into an array and converts from strings to intergers

unique_arr = []    # Empty array
for x in user_arr:
    if x not in unique_arr: #This expression tells the computer to put the items that are 
        unique_arr += [x]   #not in unique_arr, in unique_arr, and those that are in 
print("Unique element array:", unique_arr,)        # unique_arr, out of unique_arr. Thus getting rid of duplicates.
        



