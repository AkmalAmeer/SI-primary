"""
Spiral Traversal of Matrix

Given a 2D square matrix, print the matrix in a spiral order. Refer to examples for more details. From an interview's point of view, after you scan the matrix in a 2D array, try to print the matrix in a spiral order without using any extra space.



Input Format

The first line of input contains T - the number of test cases. The first line of each test case contains N - the size of the matrix [NxN]. It is followed by N lines each containing N integers - matrix elements.



Output Format

For each test case, print the matrix in a spiral order, separated by newline.



Constraints

1 <= T <= 100

1 <= N <= 100

-100 <= ar[i][j] <= 100



Example

Input

4

1

1

2

1 2

4 3

3

1 2 3

8 9 4

7 6 5

5

-44 25 -52 69 -5

17 22 51 27 -44

-79 28 -78 1 -47

65 -77 -14 -21 -6

-96 43 -21 -20 90



Output

1

1 2 3 4

1 2 3 4 5 6 7 8 9

-44 25 -52 69 -5 -44 -47 -6 90 -20 -21 43 -96 65 -79 17 22 51 27 1 -21 -14 -77 28 -78



Explanation



Self Explanatory
"""
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l1 = list(map(int,input().split()))
        l.append(l1)
    up = left = 0
    down = right = n-1
    while up <= down and left <= right:
        for i in range(left, right+1):
            print(l[up][i],end=" ")
        up += 1
        for i in range(up, down+1):
            print(l[i][right],end=" ")
        right -= 1
        if up <= down:
            for i in range(right, left-1, -1):
                print(l[down][i],end=" ")
            down -= 1 
        if left <= right:
            for i in range(down, up-1, -1):
                print(l[i][left],end=" ")
            left += 1
    print()