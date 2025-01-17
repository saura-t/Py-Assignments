def alphaNumericTest(s):
    alphaCtr, numCtr = 0, 0
    for char in s:
        if char.isalpha():
            alphaCtr += 1
        elif char.isnumeric():
            numCtr += 1

    return (alphaCtr, numCtr)


if __name__ == "__main__":
    try:
        # assuming we accept special charaters as well
        s = str(input("Enter a string of charaters: "))
        counts = alphaNumericTest(s)
        print(f"Alphabets: {counts[0]} & Numbers: {counts[1]}")
    except Exception as e:
        print(e)
