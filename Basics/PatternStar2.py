#print following out put
#*
#**
#***
#****
#*****

n = int(input("Enter number of stars to print"));

for i in range(n+1):
    for j in range(n, i - 1, -1):
        print(f"*", end=" ");
    print();