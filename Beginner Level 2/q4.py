def rotate_arr(arr, d):
    arr = arr.split(',')
    arr = list(map(int, arr))
    rotation = len(arr) - d
    for i in range(rotation):
        arr.append(arr[i])
    return arr[rotation:]

if __name__ == "__main__":
    try:
        l1 = input("Enter values(',' seperated): ")
        d = int(input("D: "))
        print(f"arr after rotation by {d}: {rotate_arr(l1, d)}")
    except Exception as e:
        print(e)