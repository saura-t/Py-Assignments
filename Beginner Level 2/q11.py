def get_split_list(s):
    s = s.split(',')
    s = (list(map(lambda word: list(map(lambda x: x, word)), s)))

    return s


if __name__ == "__main__":
    try:
        s = input("Enter value(',' seperated): ")
        print(get_split_list(s))
    except Exception as e:
        print(e)