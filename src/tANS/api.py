from src.tANS.distribution_table import DistributionTable
from src.tANS.encoder import Encoder
from src.tANS.decoder import Decoder
import time


class TableANSEncodingAPI:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.file_content = self._load_file()
        self.distribution_table = self._prepare_distribution_table()

    def _load_file(self) -> str:
        with open(self.filepath, 'r') as file:
            file_contents = file.read()
        return file_contents

    @staticmethod
    def align_to_largest_power_of_2_less_than_length(s):
        length = len(s)
        power_of_2 = 1
        while power_of_2 * 2 < length:
            power_of_2 *= 2

        aligned_string = s[:power_of_2]
        return aligned_string

    def _prepare_distribution_table(self) -> DistributionTable:
        file_contents = self.file_content
        aligned_string = TableANSEncodingAPI.align_to_largest_power_of_2_less_than_length(file_contents)
        distribution_table = DistributionTable(aligned_string)
        return distribution_table

    def _prepare_encoder(self) -> tuple[str, int]:
        message = self.file_content
        distribution_table = self.distribution_table
        encoder = Encoder(distribution_table)
        return encoder.encode(message)

    def _prepare_decoder(self, encoded_message: str, initial_state: int) -> str:
        distribution_table = self.distribution_table
        decoder = Decoder(distribution_table)
        return decoder.decode(encoded_message,  initial_state)

    def useTableANSEncDec(self):
        print(self.distribution_table)
        print(f'Origin message: {self.file_content}')
        start = time.time()
        encoded_message, initial_state = self._prepare_encoder()
        end = time.time()
        print(f'Encoding time: {end - start} ms')
        print(f'Encoded message: {encoded_message}')
        print(f'Number of compressed message bits: {len(encoded_message)}')
        print(f'Number of original message bits: {len(self.file_content) * self._next_power_of_2_greater_than_length()}')
        print(50*'-')
        start = time.time()
        self._prepare_decoder(encoded_message, initial_state)
        end = time.time()
        print(f'Decoding time: {end - start} ms')
        print(f'Decoded message: {self.file_content}')

    def _next_power_of_2_greater_than_length(self):
        length = len(self.distribution_table.get_symbol_distribution().keys())
        power_of_2 = 1
        while power_of_2 <= length:
            power_of_2 *= 2
        return power_of_2




