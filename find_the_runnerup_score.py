if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr_ = list(arr)
    arr_1 = [val for val in arr_ if val != max(arr_)]

    print(max(arr_1))
