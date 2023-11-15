"""
Product of 2 Matrices

Given 2 matrices, find their product.



Input Format

The first line of input contains T - the number of test cases. The first line of each test case contains N1, M1 - the size of the 1st matrix. It is followed by N1 lines each containing M1 integers - elements of the 1st matrix. The next line contains N2, M2 - the size of the 2nd matrix. It is followed by N2 lines each containing M2 integers - elements of the 2nd matrix. Note that M1 = N2.



Output Format

For each test case, print the resultant product matrix, separated by a new line.



Constraints

1 <= T <= 100

1 <= N1,M1,N2,M2 <= 50

-100 <= mat[i][j] <= 100



Example

Input

2

2 2

1 2

3 -1

2 3

1 -2 3

2 3 -1

2 3

27 29 53

-28 49 -24

3 4

23 52 -38 72

-64 15 -59 -10

-75 43 10 25



Output

5 4 1

1 -9 10

-5210 4118 -2207 2979

-1980 -1753 -2067 -3106



Explanation



Self Explanatory
"""
def prod(a,b):
    n1,m1 = len(a), len(a[0])
    n2,m2 = len(b), len(b[0])

    res = [[0 for _ in range(m2)] for _ in range(n1)]

    if m1!=n2:
        return ("Multiplication not possible")

    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                res[i][j] += a[i][k]*b[k][j]
    return res

for _ in range(int(input())):

    n1,m1 = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(n1)]

    n2,m2 = map(int,input().split())
    mat1 = [list(map(int,input().split())) for _ in range(n2)]

    res = prod(mat,mat1)

    for i in res:
        print(" ".join(map(str,i)))
