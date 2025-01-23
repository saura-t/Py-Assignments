if __name__ == "__main__":
    try:
        a = [1, 2, 3]
        for i in range(len(a) + 1):
            print(a[i])
    except IndexError as err:
        print(f"Index out of bound: {err}")
    except Exception as e:
        print(e)