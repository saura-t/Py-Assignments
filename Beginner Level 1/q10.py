def flip_string(s):
    words = s.split()
    return " ".join(words[::-1])

if __name__ == "__main__":
    try:
        s = input("Enter a string to reverse: ")
        print(f"Reversed string: {flip_string(s)}")
    except Exception as e:
        print(e)