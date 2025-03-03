#Program shows the reverse number.
n = int(input("Enter a number to reverse"));
s = 0
m = n;
while(n != 0):
    r = n % 10;
    s = s*10+r;
    n = n // 10;
    
print(f"N : {m} : Reverse : {s}");

#Now print indiviidual number;
print(f"Indivisiual number in the given number : {m}");
while(s != 0):
    r = s % 10;
    print(r);
    s = s//10;
