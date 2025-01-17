from collections import Counter


def anagram_check(s1, s2):
    hmap1, hmap2 = Counter(s1), Counter(s2)

    if hmap1 == hmap2:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        inp1 = input("Enter first string: ")
        inp2 = input("Enter second string: ")
        res = anagram_check(inp1, inp2)
        print(res)

    except Exception as e:
        print(e)
