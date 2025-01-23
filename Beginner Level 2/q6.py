def is_power_of_two(n):
    n = n/2.0
    if n == 2:
        return True
    elif n > 2:
        return is_power_of_two(n)
    else:
        return False
    
if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(f"{is_power_of_two(n)}")
    except ValueError as err:
        print("Only integer values accepted.")
    except Exception as e:
        print(e)