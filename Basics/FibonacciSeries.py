#program is to print Fibonacci series.
#if enter number is n then
#0 1 1 2 3 5 8 13 21 34 ........n

n = int(input("Enter a number to print Fibaonacci : "));
a = 0;
b = 1;

if(n == 0):
    print(a);
elif(n == 1):
    print(a);
    print(b);
elif(n>1):
    print(a, end=" ");
    print(b, end=" ");
    i = 1;
    while(i<=n):
        c = a+b;
        print(c,end=" ");
        a = b;
        b = c;
        i += 1;