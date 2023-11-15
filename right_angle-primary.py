"""
Print Right Angled Triangle Pattern

Print a mirror image of a right-angled triangle using '*'. See examples for more details.



Input Format

The First line of input contains T - the number of test cases. It's followed by T lines, each line contains a single integer N - the size of the pattern.



Output Format

For each test case, print the test case number as shown, followed by the pattern, separated by a new line.



Constraints

1 <= T <= 100

1 <= N <= 100



Example

Input

4
2
1
5
10


Output

Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********


Explanation



Self Explanatory
"""

t=int(input())
for j in range(1,t+1):
    n=int(input())
    print("Case #{}:".format(j))
    for i in range(1,n+1):
        space = " "*(n-i)
        star = "*"*(i)
        print(space+star)
