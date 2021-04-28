#include<stdio.h>
int calculateSum(int n)
{
        int iM2 = 0, iM1 = 1, fib, sum;
        if( n <= 0)
           return iM2;

        fib = iM2 + iM1;
        sum = fib;

        while (fib < n) {
                iM2 = iM1;
                iM1 = fib;
                sum = sum + fib;
                fib = iM2 + iM1;
        }
        return sum;
}


int main ()
{
   int n;

   printf("Enter the integer: ");
   scanf("%d", &n);
   printf("Sum of Fibonacci numbers is %d", calculateSum(n));
   getchar();
   return 0;
}
