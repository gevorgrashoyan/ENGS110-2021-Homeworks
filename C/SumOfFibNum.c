#include<stdio.h>
#include <string.h>
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

void printBinary(char *msg, int n) {
        char binaryBuf[33];
        int i, d, j = 0;

        for (i = 31; (i >= 0) && ! (n >> i); i--);
        while (i >= 0) {        
            d = n >> i--;
            binaryBuf[j++] = ((d & 1) ? 1 : 0) + '0';
        }
        binaryBuf[j] = '\0';
        printf("%s %s\n", msg, (j ==0) ? "0" : binaryBuf);
}


int main ()
{
   int n, sum;

   printf("Enter the integer: ");
   scanf("%d", &n);
   sum = calculateSum(n);
   printf("Sum of Fibonacci numbers is %d\n", sum);
   printBinary("Binary sum of Fibonacci numbers is", sum);
   getchar();
   return 0;
}
