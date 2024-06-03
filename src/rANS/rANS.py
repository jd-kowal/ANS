import math


class rANS_old:
    def __init__(self):
        self.literki = []
        self.proba = []
        self.bagno = {}
        self.proba_d = {}
        self.range = 1

        self.file_string = ""
        self.encoded = 1
        self.decoded = ""

        self.file_path = ""

        self.char_occurrences = {}

    def set_proba(self, probablilities):
        self.proba = probablilities

    def set_alfabet(self, alfabet):
        self.literki = alfabet

    def read_file(self, file_path):
        self.file_path = file_path
        file_content = ""
        with open(self.file_path, 'r') as file:
            file_content = file.read()
        self.file_string = file_content
        for char in self.file_string:
            self.char_occurrences[char] = self.char_occurrences.get(char, 0) + 1

    def function(self):
        tmp = 0
        bagno = 1
        self.range = 0
        for i in range(len(self.literki)):
            self.bagno[self.literki[i]] = [tmp + bagno, bagno]
            tmp = tmp + self.proba[i]
            self.proba_d[self.literki[i]] = self.proba[i]
            bagno = bagno % 1

        self.range = tmp

    def code(self, message):
        val = 1
        print(message, "------------")
        for symbol in message:
            tmp = (val - 1 + self.bagno[symbol][1]) // self.proba_d[symbol]
            print(tmp)
            r = (val - 1 + self.bagno[symbol][1]) % self.proba_d[symbol] + 1 - self.bagno[symbol][1]
            print(r)
            tmp = tmp * self.range + r + self.bagno[symbol][0]
            print(tmp)
            val = tmp
        self.encoded = val
        return val

    def unode(self):
        pass

    def show_bagno(self):
        print("offset ", self.bagno)
        print("proba", self.proba_d)
        print("range_len", self.range)


###################
class rANS:
    def __init__(self):
        self.literki = []
        self.proba = []
        self.offset = {}
        self.proba_d = {}
        self.decode_d = {}
        self.range = 1
        self.char_occurrences = {}
        self.file_path = ""

        self.encoded = 1
        self.decoded = ""

    def set_proba(self, probablilities):
        self.proba = probablilities

    def set_alfabet(self, alfabet):
        self.literki = alfabet

    def scale_probabilities(self):
        self.range = 2 ** len(self.proba)
        original_sum = sum(self.proba)
        scaling_factor = self.range / original_sum
        scaled_table = [num * scaling_factor for num in self.proba]
        self.proba = [max(round(num), 1) for num in scaled_table]
        rounded_sum = sum(self.proba)
        diff = self.range - rounded_sum
        while diff != 0:
            for i in range(len(self.proba)):
                if diff == 0:
                    break
                if diff > 0:
                    self.proba[i] += 1
                    diff -= 1
                elif diff < 0 and self.proba[i] > 1:
                    self.proba[i] -= 1
                    diff += 1
        return self.proba

    def read_file(self, file_path):
        self.file_path = file_path
        file_content = ""
        with open(self.file_path, 'r') as file:
            file_content = file.read()
        self.decoded = file_content
        for char in file_content:
            self.char_occurrences[char] = self.char_occurrences.get(char, 0) + 1
        print("char_occurances ", self.char_occurrences)
        tmp = 0
        self.literki = []
        self.proba = []
        for key in self.char_occurrences:
            tmp = tmp + self.char_occurrences[key]
            self.literki.append(key)
            self.proba.append(self.char_occurrences[key])
        self.range = tmp
        self.scale_probabilities()
        self.function()

    def function(self):
        tmp = 0

        self.range = 0
        for i in range(len(self.literki)):
            self.offset[self.literki[i]] = tmp
            tmp = tmp + self.proba[i]
            self.proba_d[self.literki[i]] = self.proba[i]

        self.range = tmp
        tmpi = 0
        for l in self.literki:
            for _ in range(self.proba_d[l]):
                self.decode_d[tmpi] = l
                tmpi = (tmpi + 1)

    def encode(self):
        val = self.range
        print(self.decoded, "------------")
        for symbol in self.decoded:
            tmp = val // self.proba_d[symbol]
            r = val % self.proba_d[symbol]
            tmp = tmp * self.range + self.offset[symbol] + r
            val = tmp
        self.encoded = val
        self.decoded = ""
        return val

    def decode(self):
        decoded = ""
        while self.encoded > self.range:
            symbol = self.decode_d[self.encoded % self.range]
            decoded = symbol + decoded

            completedevision = self.encoded // self.range
            wholesteps = completedevision * self.proba_d[symbol]
            fractionalsteps = self.encoded % self.range - self.offset[symbol]
            self.encoded = wholesteps + fractionalsteps
        self.decoded = decoded
        self.encoded = 1
        return decoded

    def show_bagno(self):
        print("offset ", self.offset)
        print("proba", self.proba_d)
        print("range_len", self.range)
        #print("decode_d", self.decode_d)


rans = rANS()

rans.read_file("test.txt")
rans.show_bagno()
print('encoded |', rans.encode())
print('decoded |', rans.decode())
