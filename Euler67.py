"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in 
triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, 
as there are 2**99 altogether! 
If you could check one trillion (1012) 
routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
"""

filename = "p067_triangle.txt"
with open(filename, "r") as f:
    array = []
    for line in f:
        array.append(line)
triangle = []
for i in array:
    j = i.split(" ")
    k = [int(n) for n in j]
    triangle.append(k)

for i in range(len(triangle) - 1, -1, -1):
    for j in range(0, i):
        triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])
print(triangle[0][0])
