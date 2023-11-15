"""
Print Hollow Diamond Pattern

Print a hollow diamond pattern using '*'. See examples for more details.



Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single odd integer N - the size of the diamond.



Output Format

For each test case, print the test case number as shown, followed by the diamond pattern, separated by a new line.



Constraints

1 <= T <= 100

3 <= N <= 201



Example

Input

4
3
7
5
15


Output

Case #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *

"""
def diamond_pattern(n):
    for i in range(n//2+1):
        print(" "*(n//2-i)+"*"+" "*(2*i)+"*"*(i!=n//2))
    for j in range(n//2,-1,-1):
        print(" "*(n//2-j)+"*"+" "*(2*j)+"*"*(j!=n//2))
t = int(input())
for i in range(1,t+1):
    n = int(input())
    print(f'Case #{i}:')
    diamond_pattern(n)