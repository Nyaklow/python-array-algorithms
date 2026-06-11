# A program that allows a user to input integer values and query a 2-dimensional array of size 9 X 9.  Your program should then ask the user for a pair of coordinates, (x, y), separated by a space and return the value at the position specified by the given coordinates. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 26 March 2025

arr_dd = []
print("Enter an array:")

for x in range(9):
    row = list(map(int, input().split()))
    arr_dd.append(row)
    
while True:
    coords = input("Enter coordinates:\n").split()
    x, y = int(coords[0]), int(coords[1])
    
    if x ==-1 or y == -1:
        break
    
    if 0 <= x < 9 and 0 <= y < 9:   
        print(f"Value = {arr_dd[x][y]}")
    
    
        