def IsTrialDivision(num):
    if(num <= 1):
        return "Not Prime";
        
    for i in range(2, int(num**0.5) + 1):
        
        if(num % i == 0):
            return "Not Prime";
            
    return "Prime number";

num = (int(input("Enter No to check prime no")));
print(IsTrialDivision(num));    
    