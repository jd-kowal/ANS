from src.tANS.distribution_table import DistributionTable


class Decoder:
    def __init__(self, distribution_table: DistributionTable) -> None:
        self._distribution_table = distribution_table