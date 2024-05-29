from src.uANS.uABS import uABS

if __name__ == '__main__':
    # KiK - Projekt - ANS

    # TEST uABS
    string = "10011"
    x = uABS(p=3/10)
    encoded = x.encode(string)
    decoded = x.decode(encoded)
    print("Encoded: ", encoded)
    print("Decoded: ", decoded)

