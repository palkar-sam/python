#thi program is to determin whether number is Arm strong number or no.
n = int(input("Enter Number to determin Armstrong Number"));
m = n;
s = 0;
while(n!=0):
    r = n % 10;
    s = s + (r * r * r);
    n = n // 10;
    
if(m == s):
    print("The number is Armstrong Number");
else:
    print("The Number is not Armstrong Number.");