from src.uANS.uABS import uABS

if __name__ == '__main__':
    # KiK - Projekt - ANS

    # TEST uABS
    # czyta do 6 znaków =>> 6 znaków * 8 bitów = 48 bitów
    path = "../../../ANS/tests/uANS/document.txt"

    x = uABS(path)
    alfabet, probabilities = x.prepare()

    print("uABS - Testing Algorithms")
    encoded = x.encode()
    print("Encoded: ", encoded)
    decoded = x.decode()
    print("Decoded: ", decoded)
