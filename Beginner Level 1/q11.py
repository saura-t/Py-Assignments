def convert_to_single_digit(n):
    if n > 9:
        total = 0
        while n % 10 != 0:
            total += n % 10
            n = n // 10
        return convert_to_single_digit(total)
    return n


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        res = convert_to_single_digit(n)
        print(f"Final Output: {res}")
    except ValueError as err:
        print("Only integers are allowed")
