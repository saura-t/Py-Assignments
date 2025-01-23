from statistics import median


def get_median(arr):
    arr = arr.split(',')
    arr = list(map(int, arr))
    arr.sort()
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
        med = (arr[mid-1] + arr[mid]) / 2
    else:
        mid = (len(arr) // 2)
        med = arr[mid]
    return med


if __name__ == "__main__":
    try:
        l1 = input("Enter values (',' seperated): ")
        arr = l1.split(',')
        arr = list(map(int, arr))
        print(f"Median(using 'statistics' library): {median(arr)}")
        print(f"Median: {get_median(l1)}")
    except Exception as e:
        print(e)
