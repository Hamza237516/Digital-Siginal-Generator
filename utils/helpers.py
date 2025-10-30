def get_binary_input():
    data = input("Enter binary data stream (e.g. 1011001): ").strip()
    if not all(ch in '01' for ch in data):
        raise ValueError("Input must contain only 0s and 1s.")
    return data

def get_analog_input():
    print("Enter analog values separated by space:")
    values = list(map(float, input().split()))
    return values
