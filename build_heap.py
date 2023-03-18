# python3

def build_heap(data):
    swaps = []
    # Starting from the middle and going backwards,
    # we move down the tree and sift down each node
    # to turn the array into a min-heap
    for i in range(len(data)//2, -1, -1):
        swaps = sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    # Initialize index i as the minimum element
    min_index = i
    # Get the index of the left child of node i
    left_child = 2*i + 1
    # If left child is smaller than the parent node i, 
    # update the index of the minimum element to be the left child
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    # Get the index of the right child of node i
    right_child = 2*i + 2
    # If right child is smaller than the minimum element so far,
    # update the index of the minimum element to be the right child
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child
    # If the index of the minimum element has changed,
    # swap the parent node i with the minimum element
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        # Continue sifting down the swapped element to maintain the heap property
        swaps = sift_down(data, min_index, swaps)
    return swaps

def main():
    # Input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # Checks if length of data is the same as the said length
    assert len(data) == n

    # Calls function to assess the data 
    # and give back all swaps
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
