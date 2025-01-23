if __name__ == "__main__":
    try:
        l1 = input("Enter values(',' seperated): ")
        print(set(l1.split(',')))
    except Exception as e:
        print(e)