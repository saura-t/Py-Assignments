if __name__ == "__main__":
    try:
        l1 = input("Enter value for first list(',' seperated): ")
        l2 = input("Enter value for second list(',' seperated): ")
        all_elements = set(l1.split(',')) & set(l2.split(','))
        print(all_elements)
    except Exception as e:
        print(e)
