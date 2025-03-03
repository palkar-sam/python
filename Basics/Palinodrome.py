#this program is for to determin Palinodrome number.
n = int(input("Enter a Number to deterimine Palindrome."));
m = n;
s = 0;
while(n!=0):
    r = n % 10;
    s = s * 10 + r;
    n = n // 10;
 
if(s == m):
    print("Numeber is Palindorme");
else:
    print("Number is not palindrome");