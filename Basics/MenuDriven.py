print("1. Max \n2. Min \n3. Swap")
a,b = map(int, input("Enter two numbers").split(","))
choice = int(input("Enter your choice"));
if(choice == 1):
    print("Maximum : ",max(a,b));
elif(choice == 2):
    print("Minimum : ",min(a,b));
elif(choice == 3):
    a,b = b,a
    print("After Swap %d %d"%(a,b));
else:
    print("Invalid Choice");