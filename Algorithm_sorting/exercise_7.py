n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

def merge_sort(array):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        arr = []
        l, h = low, mid

        while l < mid and h < high:
            if array[l] < array[h]:
                arr.append(array[l])
                l += 1
            else:
                arr.append(array[h])
                h += 1
        while l < mid:
            arr.append(array[l])
            l += 1
        while h < high:
            arr.append(array[h])
            h += 1
        for i in range(low, high):
            array[i] = arr[i-low]
    return sort(0, len(array))


merge_sort(array)
for i in range(n):
    print(array[i])

