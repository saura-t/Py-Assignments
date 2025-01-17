def sumOfOdds(nums):
    n = nums.split(',')
    n = list(map(int, n))
    if len(n) != 2:
        print("invalid number of values entered!")
        return
    start, end = n[0], n[1]
    if n[0] % 2 == 0:
        start += 1

    total = 0
    for i in range(start, end, 2):
        total += i
    return total


if __name__ == "__main__":
    try:
        n = input("Enter value for start and end (seperate using ','): ")
        total = sumOfOdds(n)
        print(f"sum of odd numbers is {total}")
    except ValueError as err:
        print("Only integers are allowed")
