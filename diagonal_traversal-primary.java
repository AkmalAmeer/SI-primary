/*
Diagonal Traversal of Matrix

Given a 2D matrix of size NxN, print the sum of the elements of all its diagonals.



Input Format

The first line of input contains T - the number of test cases. The first line of each test case contains the N - the size of the matrix. Each of the next N lines contains N integers - the elements of the matrix.



Output Format

For each test case, print the sum of the elements of all the diagonals, separated by a new line. Refer to samples for more clarity.



Constraints

1 <= T <= 100

1 <= N <= 100

-100 <= ar[i][j] <= 100



Example

Input

4

3

-5 0 4

2 8 -6

3 7 1

1

-4

2

5 -2

-4 1

6

-2 -3 -6 -5 50 3

8 7 10 -5 -3 30

6 3 70 9 -20 -7

-9 9 -6 7 3 2

-1 7 7 6 -4 3

8 5 6 -9 40 8



Output

4 -6 4 9 3

-4

-2 6 -4

3 80 -15 -29 22 86 51 13 4 4 8



Explanation



Test Case 1

Sum of the elements of the 1st diagonal: 4

Sum of the elements of the 2nd diagonal: 0 + -6 = -6

Sum of the elements of the 3rd diagonal: -5 + 8 + 1 = 4

Sum of the elements of the 4th diagonal: 2 + 7 = 9

Sum of the elements of the 5th diagonal: 3



Test Case 2

Sum of the elements of the 1st and only diagonal: -4



Test Case 3

Sum of the elements of the 1st diagonal: -2

Sum of the elements of the 2nd diagonal: 5 + 1 = 6

Sum of the elements of the 3rd diagonal: -4
*/
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Main. */
        Scanner sc = new Scanner(System.in);
        int txt = sc.nextInt();
        while(txt!=0){
            txt--;
            int n = sc.nextInt();
            int A[][] = new int[n][n];
            for(int i = 0;i<n;i++){
                for(int j = 0;j<n;j++){
                    A[i][j] = sc.nextInt();
                }
            }
            for(int z=0;z<2*n-1;z++){
                int r = 0;
                int i = Math.max(0,z-n+1);
                int j = Math.max(0,n-z-1);
                for(;i<n&&j<n;i++,j++){
                    r += A[i][j];
                }
                System.out.print(r+" ");
            }
            System.out.println();
        }
    }
}