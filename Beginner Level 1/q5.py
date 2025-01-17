def factorial(num):
    res = 1
    for i in range(2, num+1):
        res *= i
    
    return res

if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
        fact = factorial(n)
        print(f"factorial of {n} is {fact}")
    except ValueError as err:
        print("Only integers are allowed")