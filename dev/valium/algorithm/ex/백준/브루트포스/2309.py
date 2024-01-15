'''
https://www.acmicpc.net/submit/2309/71793614
'''

def get_target_index(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if sum(arr) - arr[i] - arr[j] == 100:
                return i, j

    return -1, -1

if __name__ == '__main__':
    arr = sorted([int(input()) for _ in range(9)])

    target_index = get_target_index(arr)

    for k in range(0, len(arr)):
        if k in target_index:
            continue

        print(arr[k])
