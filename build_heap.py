# python3

def sift_down(arr, i, n, swaps):
    while 2*i + 1 < n:
        j = i  # parent
        l = 2*i + 1  # left child
        r = 2*i + 2  # right child
        
        if arr[l] < arr[j]:
            j = l
        if r < n and arr[r] < arr[j]:
            j = r
        
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]
            swaps.append((i, j))
            i = j
        else:
            break


def build_heap(arr):
    n = len(arr)
    swaps = []
    
    for i in range(n//2, -1, -1):
        sift_down(arr, i, n, swaps)
        
    return swaps


def main():
    input_type = input("Enter I for keyboard input or F for file input: ").strip()

    if input_type.lower() == 'i':
        n = int(input())
        arr = list(map(int, input().split()))

    elif input_type.lower() == 'f':
        file_name = input("Enter file name: ").strip()
        try:
                file_name = open("./tests/" + file_name, mode = "r")
                n = int(file_name.readline().strip())
                arr = list(map(int, file_name.readline().split()))

        except OSError as e:
            print(f"Error: {e}")
            return
        
    else:
        print("Invalid input type")
        return

    assert len(arr) == n
    assert len(arr) == len(set(arr))

    swaps = build_heap(arr)

    print(len(swaps))
    assert len(swaps) <= 4 * n

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
