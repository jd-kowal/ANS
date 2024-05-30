import math

class uABS:
    def __init__(self, file_path):
        self.p = 0
        self.alfabet = []
        self.text = ""
        self.file_path = file_path
        self.encoded = ""
        self.decoded = ""
        self.is_text = False

    def probability_setter(self, p):
        self.p = p

    def prepare(self):
        # funkcja zliczająca alfabet i prawdopodobieństwo
        import collections

        # Odczytanie pliku
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        binary_list = []
        if text.isnumeric() == 0:
            self.is_text = True
            # Iterate through each character in the string
            for char in text:
                # Convert character to binary, pad with leading zeroes and append to list
                binary_list.append(bin(ord(char))[2:].zfill(8))
            text = ''.join(map(str, binary_list))
        else:
            for char in text:
                if char not in {'0', '1'}:
                    raise ValueError()

        self.text = text

        # Tworzenie licznika dla wszystkich znaków w pliku
        counter = collections.Counter(text)

        # Całkowita liczba znaków w pliku
        total_characters = sum(counter.values())

        # Informacje o alfabecie i prawdopodobieństwie występowania
        alphabet = list(counter.keys())
        probabilities = {char: count / total_characters for char, count in counter.items()}

        self.alfabet = alphabet

        # Sprawdzanie ilości różnych znaków -> maksymalnie dwa
        if len(probabilities) > 2:
            raise ValueError()

        # Ustawianie dobrego prawdopodobieństwa do algorytmu
        if len(probabilities) == 1:
            try:
                self.p = probabilities['0']
            except:
                self.p = probabilities['1']
            #self.p = 9.99999
        elif probabilities["0"] < probabilities["1"]:
            self.p = probabilities["0"]
        else:
            self.p = probabilities["1"]
        return alphabet, probabilities

    def bin_to_string(self):
        binary_str = self.decoded
        # Podziel ciąg binarny na segmenty 8-bitowe
        n = 8
        binary_segments = [binary_str[i:i + n] for i in range(0, len(binary_str), n)]

        # Zamień każdy segment na znak ASCII i połącz w słowo
        word = ''.join([chr(int(segment, 2)) for segment in binary_segments])

        return word

    def encode(self, text=None):
        if text is None:
            text = self.text
        x = 1
        for sign in text:
            if sign == '0':
                x = math.ceil((x + 1) / (1 - self.p)) - 1
            elif sign == '1':
                x = math.floor(x / self.p)
            else:
                raise ValueError('Encoding error')
        self.encoded = x
        return x

    def decode(self, x=None):
        if x is None:
            x = self.encoded
        y = ""
        while x > 1:
            s = math.ceil((x + 1) * self.p) - math.ceil(x * self.p)
            y = y + str(s)
            if s == 0:
                x = x - math.ceil(x * self.p)
            elif s == 1:
                x = math.ceil(x * self.p)
            else:
                raise ValueError('Decoding error')
        decoded_text = y[::-1]
        self.decoded = decoded_text

        # Checking if we need to transform bits into a text (text was encoded)
        if self.is_text:
            decoded_text = self.bin_to_string()
        return decoded_text
