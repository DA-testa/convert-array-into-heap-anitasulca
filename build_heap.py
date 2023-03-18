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
    # Get input from the user
    mode = input("Enter 'F' to read from a file or 'I' to input manually: ").lower().strip()
    n = int(input(" "))
    data = list(map(int, input(" ").split()))

    # If the mode is file, get the file name and read data from the file
    if mode == "f":
        file_name = input("Enter the file name: ").strip()
        try:
            with open(file_name, "r") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().split()))
        except OSError as e:
            print(e)
            return

    # Check the length of the input data
    assert len(data) == n

    # Call the function to assess the data and get all swaps
    swaps = build_heap(data)

    # Output the number of swaps made, which should be less than 4n
    print(f"Number of swaps: {len(swaps)}")

    # Output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()



