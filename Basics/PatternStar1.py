#print following out put
#*
#**
#***
#****
#*****

n = int(input("Enter number of stars to print"));

for i in range(n):
    for j in range(0, i+1):
        print("*", end=" ");
    print();