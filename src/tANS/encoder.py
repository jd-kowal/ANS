from src.tANS.distribution_table import DistributionTable


class Encoder:
    def __init__(self, distribution_table: DistributionTable) -> None:
        self._dt = distribution_table

    def __str__(self) -> str:
        return "tANS Encoder"

    def encode(self, message: str) -> tuple[str, int]:
        table = self._prepare_table()
        initial_state_idx = table['x_'].index(table['x_'][table['symbol'].index(message[-1])])
        output = ""
        next_symbol = table['x_'][initial_state_idx]

        for symbol in reversed(message[:-1]):
            curr_idx = table['x_'].index(next_symbol)
            next_symbol, curr_val = table[symbol][curr_idx]
            output += bin(curr_val)[2:]

        return output, next_symbol

    def _prepare_table(self):
        table = self._dt.get_table()

        for symbol in self._dt.get_symbol_distribution().keys():
            table[symbol] = []
        for idx, symbol in enumerate(table['symbol']):
            n_bits = table['nBits'][idx]
            for i in range(2**n_bits):
                try:
                    table[symbol].append((table['x_'][idx], i))
                except KeyError:
                    table[symbol] = []
                    table[symbol].append((table['x_'][idx], i))

        return table

