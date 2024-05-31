from src.tANS.distribution_table import DistributionTable


class Decoder:
    def __init__(self, distribution_table: DistributionTable) -> None:
        self._dt = distribution_table

    def __str__(self) -> str:
        return "tANS Decoder"

    def decode(self, encoded_message: str, state_x: int) -> str:
        table = self._dt.get_table()
        output = ""
        rest_of_bits = encoded_message
        while rest_of_bits:
            symbol_idx = table['x_'].index(state_x)
            output += table['symbol'][symbol_idx]
            state_x = table['newX'][symbol_idx] + int(Decoder.read_bits(rest_of_bits, table['nBits'][symbol_idx]), 2)
            rest_of_bits = rest_of_bits[:(-table['nBits'][symbol_idx])]
        return output

    @staticmethod
    def read_bits(buffer: str, nb_bits: int) -> str:
        return buffer[-nb_bits:]


