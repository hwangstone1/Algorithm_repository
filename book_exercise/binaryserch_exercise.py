
def bi(array, target, low, high):
    mid = (low + high) // 2
    if low > high :
        return 0
    if array[mid] > target:
        return bi(array, target, low, mid-1)
    elif array[mid] < target:
        return bi(array, target, mid + 1, high)
    else:
        return mid + 1





if __name__ == "__main__":
    array = list(map(int, input().split()))
    target = int(input())
    array.sort()

    answer = bi(array, target, 0, len(array)-1)

    print(answer)