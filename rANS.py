class rANS:
    def __init__(self):
        self.literki = []
        self.proba = []
        self.bagno = {}
        self.proba_d = {}
        self.count = 1

        self.encoded = 1
        self.decoded = ""

    def set_proba(self, probablilities):
        self.proba = probablilities

    def set_alfabet(self, alfabet):
        self.literki = alfabet

    def function(self):
        tmp = 0
        bagno = 1
        self.count = 0
        for i in range(len(self.literki)):
            self.bagno[self.literki[i]] = [tmp + bagno, bagno]
            tmp = tmp + self.proba[i]
            self.proba_d[self.literki[i]] = self.proba[i]
            bagno = bagno % 1

        self.count = tmp

    def code(self, message):
        val = 1
        print(message, "------------")
        for symbol in message:
            tmp = (val - 1 + self.bagno[symbol][1]) // self.proba_d[symbol]
            print(tmp)
            r = (val - 1 + self.bagno[symbol][1]) % self.proba_d[symbol] + 1 - self.bagno[symbol][1]
            print(r)
            tmp = tmp * self.count + r + self.bagno[symbol][0]
            print(tmp)
            val = tmp
        self.encoded = val
        return val

    def unode(self):
        pass

    def show_bagno(self):
        print("offset ", self.bagno)
        print("proba", self.proba_d)
        print("range_len", self.count)
        print(self.bagno["A"])


l = ["A", "B", "C"]
p = [4, 3, 1]

rans = rANS()
rans.set_alfabet(l)
rans.set_proba(p)
rans.function()
rans.show_bagno()
print('|', rans.code(""))
