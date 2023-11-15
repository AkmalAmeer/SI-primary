"""
First Repeating Character - 2

Given a string of characters, find the first repeating character.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a single string of characters.



Output Format

For each test case, print the first repeating character, separated by a new line. If there are none, print '.'.



Constraints

1 <= T <= 1000

'a' <= str[i] <= 'z'

1 <= len(str) <= 104



Example

Input

4

datastructures

algorithms

smartinterviews

hackerrank



Output

a

.

t

r



Explanation



Self Explanatory
"""


for _ in range(int(input())):
    st = input()
    d = {}
    val = '.'
    for i in st:
        if i in d:
            d[i] += 1
            val = i
            break
        else:
            d[i] = 1
    print(val)