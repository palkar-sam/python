#this program is to find factorial of number using while loop.
#e.g 5! = 5 * 4 * 3 * 2 * 1

n = int(input("Enter a number for Factorial : "));
i = 1;
b = n;
while(n != 0):
    i = i * n;
    n = n - 1;
    
print(f"Factorial of Number {b} is : {i}");
