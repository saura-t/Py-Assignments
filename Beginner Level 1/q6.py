def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def perfectNumber(num):
    divisors = get_divisors(num)
    if num == sum(divisors)-num:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        perfectNumber(n)
    except ValueError as err:
        print("Only integers are allowed")