class tANS:
    def __init__(self, symbol_probs):
        self.R = 2
        self.L = 1 << self.R
        self.symbol_probs = symbol_probs
        self.symbol_to_count = {s: int(self.L * p) for s, p in symbol_probs.items()}
        self.maxX = {s: self.L // self.symbol_to_count[s] for s in self.symbol_probs}
        self.encoding_table = self.generate_encoding_table()
        self.decoding_table = self.generate_decoding_table()

    def generate_encoding_table(self):
        start = {}
        next_symbol = {}
        encoding_table = [0] * (2 * self.L)
        total_count = 0

        for s in sorted(self.symbol_probs):
            start[s] = total_count
            next_symbol[s] = 0
            total_count += self.symbol_to_count[s]

        for x in range(self.L, 2 * self.L):
            s = self.symbol_from_state(x)
            encoding_table[start[s] + next_symbol[s]] = x
            next_symbol[s] += 1

        return encoding_table

    def generate_decoding_table(self):
        next_symbol = {s: 0 for s in self.symbol_probs}
        decoding_table = []

        for X in range(self.L):
            s = self.symbol_from_state(X + self.L)
            x = next_symbol[s]
            next_symbol[s] += 1
            nb_bits = self.R - x.bit_length()
            new_x = (x << nb_bits) - self.L
            decoding_table.append((s, new_x, nb_bits))

        return decoding_table

    def symbol_from_state(self, x):
        total_count = 0
        for s in sorted(self.symbol_probs):
            total_count += self.symbol_to_count[s]
            if x < total_count:
                return s
        raise ValueError(f"Invalid state: {x}")

    def encode_symbol(self, x, s):
        while x >= self.maxX[s]:
            self.write_bit(x % 2)
            x //= 2

        return self.encoding_table[x - self.L]

    def decode_symbol(self, x):
        s, new_x, nb_bits = self.decoding_table[x - self.L]
        for _ in range(nb_bits):
            new_x = (new_x << 1) | self.read_bit()

        return s, new_x

    def write_bit(self, bit):
        # Placeholder function to simulate writing a bit to a stream
        pass

    def read_bit(self):
        # Placeholder function to simulate reading a bit from a stream
        return 0  # Replace with actual bit reading logic

# Example usage:
symbol_probs = {'a': 0.75, 'b': 0.25}
encoder = tANS(symbol_probs)

# Encoding process
x = 4  # Example initial state
x = encoder.encode_symbol(x, 'a')

# Decoding process
s, x = encoder.decode_symbol(x)
