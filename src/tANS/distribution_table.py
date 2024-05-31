from collections import defaultdict
import random


class DistributionTable:
    def __init__(self, message: str) -> None:
        self._message: str = message
        self._symbol_distribution = self._extract_symbol_distribution()
        self._frequencies_sum: int = 0
        self._table: dict[str: list[str | int]] = {}
        self._L = self._sum_symbols()
        self._I = self._enumerate_appearances()

        self._initialize()

    def __str__(self) -> str:
        max_len = max(len(str(item)) for key in self._table for item in self._table[key])
        x = " | ".join(f"{str(item):<{max_len}}" for item in self._table['x_'])
        symbol = " | ".join(f"{str(item):<{max_len}}" for item in self._table['symbol'])
        x_tmp = " | ".join(f"{str(item):<{max_len}}" for item in self._table['x_tmp'])
        nBits = " | ".join(f"{str(item):<{max_len}}" for item in self._table['nBits'])

        return f"""
        DISTRIBUTION TABLE
        | x      | {x} |
        | symbol | {symbol} |
        | x_tmp  | {x_tmp} |
        | nBits  | {nBits} |
        """

    def get_frequencies_sum(self) -> int:
        return self._frequencies_sum

    def get_L(self) -> int:
        return self._L

    def get_I(self) -> list[int]:
        return self._I

    def get_table(self) -> dict[str, list[int]]:
        return self._table

    def get_symbol_distribution(self) -> dict[str, int]:
        return dict(self._symbol_distribution)

    def _extract_symbol_distribution(self) -> dict[str, int]:
        symbol_distribution = defaultdict(lambda: 0)
        for symbol in self._message:
            symbol_distribution[symbol] += 1
        return dict(symbol_distribution)

    def _sum_symbols(self) -> int:
        return len(self._message)

    def _enumerate_appearances(self) -> list[int]:
        return [Ls for Ls in range(self._L, 2 * self._L)]

    def _redistribute_symbols(self) -> list[int | str]:
        symbols = []
        for symbol, freq in self._symbol_distribution.items():
            symbols.extend([symbol] * freq)
        # random.shuffle(symbols)
        return symbols

    def _set_x_tmp(self, symbols: list[int | str]) -> list[int]:
        x_tmp = []
        symbol_distribution = self._symbol_distribution.copy()
        for symbol in symbols:
            x_tmp.append(symbol_distribution[symbol])
            symbol_distribution[symbol] += 1
        return x_tmp

    def _set_nbits(self, x_tmp: list[int]) -> list[int]:
        nbits = []
        for symbol in x_tmp:
            counter, tmp_symbol = 0, symbol
            while tmp_symbol < self._L:
                counter += 1
                tmp_symbol *= 2
            nbits.append(counter)
        return nbits

    def _initialize_table(self) -> None:
        self._table['x_'] = self._I
        self._table['symbol'] = self._redistribute_symbols()
        self._table['x_tmp'] = self._set_x_tmp(self._table['symbol'])
        self._table['nBits'] = self._set_nbits(self._table['x_tmp'])

    def _initialize(self) -> None:
        self._initialize_table()