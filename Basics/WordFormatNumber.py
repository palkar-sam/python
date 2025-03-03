#this program is to print each word in the number;
n = int(input("Enter a Number to print each number in word format"));
s = 0;
m = n;
while(n != 0):
    r = n % 10;
    s = s * 10 + r;
    n = n // 10;

print("Reverse Number is %d", s);
print("Word Format : ");
while(s != 0):
    r = s % 10;
    s = s//10;
    if( r == 0):
        print("Zero");
    elif(r == 1):
        print("One");
    elif(r == 2):
        print("Two");
    elif(r == 3):
        print("Three");
    elif(r == 4):
        print("Four");
    elif(r == 5):
        print("Five");
    elif(r == 6):
        print("Six");
    elif(r == 7):
        print("Seven");
    elif(r == 8):
        print("Eight");
    elif(r == 9):
        print("Nine");
     