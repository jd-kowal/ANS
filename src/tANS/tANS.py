from collections import defaultdict
import random


class EncodertANS:
    def __init__(self, message: str) -> None:
        self.message: str = message
        self.symbols: list[str] = []
        self.frequencies: list[int] = []
        self.symbols_to_freq: defaultdict[str, int] = defaultdict(lambda: 0) # default factory -> funkcja zwracająca wartosć domyślną
        self.frequencies_sum: int = 0

        self.tANS_table: dict[str: list[str | int]] = {'x': [], 'S': [], 'y': [], 'k': [], 'y_prim': []}

    def fill_tans_table(self) -> None:
        self.tANS_table['x'] = [i for i in range(self.frequencies_sum, self.frequencies_sum * 2)]
        symbols = []
        for symbol, freq in self.symbols_to_freq.items():
            for _ in range(freq):
                symbols.append(symbol)
        random.shuffle(symbols)
        self.tANS_table['S'] = symbols
        y_symbols = self.symbols_to_freq
        for symbol in self.tANS_table['S']:
            self.tANS_table['y'].append(y_symbols[symbol])
            y_symbols[symbol] += 1

        for y in self.tANS_table['y']:
            counter = 0
            temp_y = y
            while temp_y < self.frequencies_sum:
                counter += 1
                temp_y *= 2
            self.tANS_table['k'].append(counter)

        for symbol in self.symbols:
            self.tANS_table[symbol] = []
        for idx, symbol in enumerate(self.tANS_table['S']):
            k = self.tANS_table['k'][idx]
            for i in range(2**k):
                try:
                    self.tANS_table[symbol].append((self.tANS_table['x'][idx], i))
                except KeyError:
                    self.tANS_table[symbol] = []
                    self.tANS_table[symbol].append((self.tANS_table['x'][idx], i))



    def encode(self):
        output = ""
        desired_number = max(self.tANS_table['k'])
        initial_state_idx = self.tANS_table['S'].index(self.message[0])
        next_symbol = self.tANS_table['x'][initial_state_idx]
        for symbol in self.message[1:]:
            curr_idx = self.tANS_table['x'].index(next_symbol)
            next_symbol, curr_val = self.tANS_table[symbol][curr_idx]
            print(f"next_symbol: {next_symbol}, curr_val: {curr_val}, cr_bin: {bin(curr_val)[2:].zfill(desired_number)}")
            output += bin(curr_val)[2:].zfill(desired_number)

        print(output)
        print(len(output))

    def get_symbols_to_freq(self) -> dict[str, int]:
        return dict(self.symbols_to_freq)

    def print_tANS_table(self) -> None:
        print(f'x: {self.tANS_table['x']}')
        print(f'S: {self.tANS_table['S']}')
        print(f'y: {self.tANS_table['y']}')
        print(f'k: {self.tANS_table['k']}')
        for letter in self.symbols:
            print(f"{letter}: {self.tANS_table[letter]}")

    def extrac_symbols(self):
        for element in self.message:
            self.symbols_to_freq[element] += 1
        # self.symbols_to_freq['A'] = 3
        # self.symbols_to_freq['B'] = 3
        # self.symbols_to_freq['C'] = 2

    def sum_frequencies(self):
        self.frequencies_sum = sum([val for val in self.symbols_to_freq.values()])


tans = EncodertANS("ABACCACBC")
print(type(tans.symbols_to_freq))
print(tans.symbols_to_freq['A'])
print(tans.extrac_symbols())
print(tans.get_symbols_to_freq())
print(tans.sum_frequencies())
print(tans.frequencies_sum)
print(tans.fill_tans_table())
print(tans.tANS_table['x'][0])
tans.print_tANS_table()

tans.encode()

print(tans.tANS_table)
print(bin(1)[2:].zfill(2))

