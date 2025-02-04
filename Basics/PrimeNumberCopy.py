num = int(input("Enter Number to check : "));
#negative numbers, 0 and 1 are not primes
if num > 1:
    #iterate from 2 to n // 2 (// is called floor division which returns floor value of result that is int
    for i in range(2, (num//2)+1):
        #if num is divisible by any number between 2 and n/2 then it is not prime number.
        if(num % i == 0):
            print("Number is not prime Number");
            break;
            
    else:
        print("Number is prime number");
else:
    print("Number is prime number"); 

num = 100;print("Num ", num)

         