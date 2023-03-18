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
    inputs = input("Enter 'F' for file input or 'I' for keyboard input: ").strip().lower()

    if inputs == 'f':
        file = input("Enter the filename: ").strip()
        try:
            with open(file, "r") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
                swaps = build_heap(data)
                print(len(swaps))
                for i, j in swaps:
                    print(i, j)
        except OSError as e:
            print(e)
    elif inputs == 'i':
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements: ").split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()



