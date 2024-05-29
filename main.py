from uABS import uABS

if __name__ == '__main__':
    # KiK - Projekt - ANS

    # TEST uABS
    #string = "10011"
    string = "00010101"
    x = uABS(p=3/10)
    encoded = x.encode(string)
    decoded = x.decode(encoded)
    print("Encoded: ", encoded)
    print("Decoded: ", decoded)

    char = 'A'
    ascii_value = ord(char)
    print(f'Wartość ASCII {char} to {ascii_value}')

    binary_list = []

    string = char
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))

    print(binary_list)