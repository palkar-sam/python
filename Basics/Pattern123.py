#print patter like below
#1 1 1 1 1
#2 2 2 2 2
#3 3 3 3 3
#4 4 4 4 4

#using nested for loop
print("Using Nested For Loop");
for i in range(1,5):
    for j in range(1,6):
        print(i,end=" ")
    print()
    
#using while loop
print("using while loop")
n = int(input("Enter a number"))
i = 1
while (i < n):
    j = 1
    while(j < n):
        print(i, end=" ")
        j = j + 1
    i = i + 1
    print()



