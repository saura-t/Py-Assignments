def get_vowels_count(s):
    ctr = 0
    for char in s:
        if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            ctr += 1
    return ctr

if __name__ == "__main__":
    try:
        s = input("Enter input string: ")
        print(f"Number of vowels: {get_vowels_count(s)}")
    except Exception as e:
        print(e)