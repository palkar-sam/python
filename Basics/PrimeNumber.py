def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def printDivisors(n):
    """Print all divisors of a number up to its square root.
    
    Args:
        n (int): The number to find divisors of.
    """
    limit = int(n**0.5) + 1
    print("Limit is ",limit)
    for i in range(2, limit):
            print(i)

def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    #number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    printDivisors(number)

if __name__ == "__main__":
    main()