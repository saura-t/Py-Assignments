def unhappy_customers(n, s):
    ctr = 0
    comps = set()
    i = 0
    while i < len(s):
        if s[i] in comps:
            comps.remove(s[i])
        elif len(comps) < n:
            comps.add(s[i])
        else:
            ctr += 1
            i += 1
        i += 1
    return ctr


if __name__ == "__main__":
    try:
        n = int(input("Enter number of computers: "))
        s = input("Customers string: ")
        print(f"Number of unhappy customers: {unhappy_customers(n, s)}")
    except Exception as e:
        print(e)
