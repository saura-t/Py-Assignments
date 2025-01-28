def get_encoded(s):
    res = ''
    ctr = 1
    for i in range(len(s)):
        if i+1 < len(s) and s[i] == s[i+1]:
            ctr += 1
        else:
            res = res + s[i] + str(ctr)
            ctr = 1
    return res

if __name__ == "__main__":
    try:
        s = input("Enter str: ")
        print(f"{get_encoded(s)}")
    except Exception as e:
        print(e)