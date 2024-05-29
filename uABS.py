import math

class uABS:
    def __init__(self, p):
        self.p = p

    def prepare(self):
        # funkcja zliczająca alfabet i prawdopodobieństwo
        pass


    def encode(self, text):
        x = 1
        for sign in text:
            if sign == '0':
                x = math.ceil((x + 1) / (1 - self.p)) - 1
            elif sign == '1':
                x = math.floor(x / self.p)
            else:
                raise ValueError('Encoding error')
        return x

    def decode(self, x):
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
        return decoded_text
