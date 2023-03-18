# python3

def sift_down(arr, i, n, swaps):
    while True:
        left_child = 2*i + 1
        right_child = 2*i + 2
        min_index = i

        if left_child < n and arr[left_child] < arr[min_index]:
            min_index = left_child
        if right_child < n and arr[right_child] < arr[min_index]:
            min_index = right_child

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append((i, min_index))
            i = min_index
        else:
            break


def build_heap(arr):
    n = len(arr)
    swaps = []

    for i in range(n//2 - 1, -1, -1):
        sift_down(arr, i, n, swaps)

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
        print(f"Error: {e}")
        return None, None
    return n, data


def main():
    # Prompt user to choose input type
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

    # Output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()







