#Prime number is to check give number is prime or not in recursive way.
from math import sqrt;


def Prime(number, itr):
    #base conditpoin
    if(itr == 1 or itr == 2):
        return "Not Prime Number";
    if(number % itr == 0):
        return "Not Prime Number";
    
    if(Prime(number, itr - 1) == False):
        return "Not Prime Number";
        
    return "Number is Prime";

num = int(input("Enter number : "));

if num > 0:
    itr = int(sqrt(num)) + 1
    print(Prime(num, itr));
else:
    print("Number is negative not a prime Number");
    
        