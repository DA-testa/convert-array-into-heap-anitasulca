# python3

def small(data, i, swaps):
    n = len(data)
    l = 2*i + 1
    r = 2*i + 2
    sm = i
    if l < n and data[l] < data[sm]:
        sm = l
    if r < n and data[r] < data[sm]:
        sm = r
    if sm != i:
        swaps.append((i, sm))
        data[i], data[sm] = data[sm], data[i]
        small(data, sm, swaps)

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        small(data, i, swaps)
    return swaps

def main():
    # Prompt user for input method
    method = input("Enter 'F' to input data from file or 'I' to input data from keyboard: ").strip().lower()

    if method == 'f':
        # Prompt user for file name
        file_name = input("Enter file name: ").strip()

        try:
            with open(file_name, "r") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
                swaps = build_heap(data)
                print(len(swaps))
                for i, j in swaps:
                    print(i, j)
        except OSError as e:
            print(e)

    elif method == 'i':
        # Prompt user for n and data
        n = int(input("Enter n: "))
        data = list(map(int, input("Enter data: ").split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()



