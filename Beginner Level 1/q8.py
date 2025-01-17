from math import gcd


def get_lcm(n1, n2):
    return (n1 * n2) // gcd(n1, n2)


if __name__ == "__main__":
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        print(f"LCM of {n1} and {n2} is {get_lcm(n1, n2)}")
    except ValueError as err:
        print("Only integers are allowed")
