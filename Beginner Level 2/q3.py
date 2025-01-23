from collections import defaultdict

def get_pair_count(arr, k):
    ctr = 0
    arr = arr.split(',')
    hmap = defaultdict(list)
    for i in range(len(arr)):
        '''Assuming there can be duplicates in arr, since we cant use one element twice'''
        if int(arr[i]) in hmap:
            hmap[int(arr[i])].append(i)
        else:
            hmap[int(arr[i])] = [i]
    for key in hmap:
        if len(hmap[key]) > 0:
            target = k - key
            hmap[key].pop()
            if target in hmap and len(hmap[target]) > 0:
                ctr += 1
                hmap[target].pop()
    return ctr


if __name__ == "__main__":
    try:
        l1 = input("Enter values(',' seperated): ")
        k = int(input("K: "))
        print(f"Pair Count: {get_pair_count(l1, k)}")
    except Exception as e:
        print(e)
