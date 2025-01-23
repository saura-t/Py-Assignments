if __name__ == "__main__":
    try:
        s = input("Enter string: ")
        c = input("Enter character: ")
        res = lambda x: True if x[0].lower() == c.lower() else False
        print(f"{res(s)}")
    except Exception as e:
        print(e)