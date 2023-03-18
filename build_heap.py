# python3

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_idx = i
    l = 2*i+1
    if l < n and data[l] < data[min_idx]:
        min_idx = l
    r = 2*i+2
    if r < n and data[r] < data[min_idx]:
        min_idx = r
    if i != min_idx:
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps.append((i, min_idx))
        sift_down(min_idx, data, swaps)

def main():
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
