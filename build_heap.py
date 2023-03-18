# python3

def check(arr, i, n, swaps):
    while True:
        l = 2*i + 1
        r = 2*i + 2
        min = i

        if l < n and arr[l] < arr[min]:
            min = l
        if r < n and arr[r] < arr[min]:
            min = r

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            swaps.append((i, min))
            i = min
        else:
            break


def build_heap(arr):
    n = len(arr)
    swaps = []

    for i in range(n//2 - 1, -1, -1):
        check(arr, i, n, swaps)

    return swaps


def read_data_from_keyboard():
    n = int(input())
    data = list(map(int, input().split()))
    return n, data


def read_data_from_file():
    file_name = input("Enter file name: ").strip()
    try:
        with open("./tests/" + file_name, mode="r") as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().split()))
    except OSError as e:
        return None, None
    return n, data


def main():

    input_type = input("Enter 'I' for keyboard input or 'F' for file input: ").strip()

    if input_type.lower() == 'i':
        n, data = read_data_from_keyboard()
    elif input_type.lower() == 'f':
        n, data = read_data_from_file()
    else:
        print("Invalid input type")
        return

    # Checks if length of data is the same as the said length
    assert len(data) == n
    assert len(data) == len(set(data))

    swaps = build_heap(data)

    # Outputs how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n
    print(len(swaps))

    
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()







