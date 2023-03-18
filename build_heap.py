# python3


def heapify(data, n, i, swaps):
    """
    A function to heapify a subtree rooted with node i
    """
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is smaller than root
    if l < n and data[l] < data[smallest]:
        smallest = l

    # See if right child of root exists and is smaller than root
    if r < n and data[r] < data[smallest]:
        smallest = r

    # Change root, if needed
    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]  # swap

        # Heapify the root.
        heapify(data, n, smallest, swaps)

def build_heap(data):
    swaps = []
    n = len(data)
    # Build a heap from the last non-leaf node by performing heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps

def main():
    # Input from keyboard
    n = int(input())
    data = list(map(int, input().split()))
    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # Output how many swaps were made
    print(len(swaps))
    # Output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
