def get_reversed(n):
    total = 0
    while n != 0:
        total = (total*10) + (n % 10)
        n = n // 10
    return total


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(f"Reverse of {n} is {get_reversed(n)}")
    except ValueError as err:
        print("Only integers are allowed")
