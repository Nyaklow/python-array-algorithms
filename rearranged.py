# A program that rearranges a sorted array such that the largest element is at index 0, the smallest at 1, the second largest at index 2, and so on.
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 26 March 2025

num = str(input("Enter sorted numbers separated by spaces:\n"))
arr = [int(num) for num in num.split()] # Putting the input into the array

high = len(arr) - 1
low = 0
copy = [0] *len(arr) # A temporary array which stores the rearrangemnet of the elements
alt = True    # A statement that can act as a 'fact checker' for the program, this is purely because I did not have an equation or pattern of sorts that could rearrange the elements.
for i in range(len(arr)):
    if alt:
        copy[i] = arr[high]
        high -= 1
    else:
        copy[i] = arr[low]
        low += 1
    alt = not alt
    
for i in range(len(arr)):   # this updates the original list with the rearranged items
    arr[i] = copy[i]
print("Rearranged array:", arr,)



    
        
        
        
        
