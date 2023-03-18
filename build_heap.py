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
    # input from keyboard or file
    data_input = input("Enter data (separated by space): ")
    input_type = input("Enter input type (I for keyboard, F for file): ")

    # input validation
    if input_type == "F":
        try:
            with open(data_input, "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
        except:
            print("Invalid file or file format")
            return
    elif input_type == "I":
        try:
            n = int(data_input.split()[0])
            data = list(map(int, data_input.split()[1:]))
            assert len(data) == n
        except:
            print("Invalid input format")
            return
    else:
        print("Invalid input type")
        return

    # calls function to assess the data and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4*len(data)
    print("Number of swaps: ", len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()






