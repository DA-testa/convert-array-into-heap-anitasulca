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
    evade = input("Enter 'I' for input from keyboard or 'F' for input from file: ").strip().lower()
    if evade == "f":
        file = input("Enter file name: ").strip()
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
    elif evade == "i":
        n = int(input("Enter the length of the list: "))
        data = list(map(int, input("Enter the elements of the list separated by space: ").split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    else:
        print("Invalid input. Please enter 'I' or 'F'.")

if __name__ == "__main__":
    main()


