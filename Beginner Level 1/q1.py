def divTest(num):
    if num % 3 == 0 and num % 5 == 0:
         print("Consultadd - Python Training")
    elif num % 3 == 0:
        print("Consultadd")
    elif num % 5 == 0:
        print("Python Training")

if __name__ == "__main__":
    try:
        n = int(input("Enter a number for divisibility test: "))
        divTest(n)
    except ValueError as err:
        print("Only integers are allowed")