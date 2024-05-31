from src.tANS.distribution_table import DistributionTable


class Encoder:
    def __init__(self, distribution_table: DistributionTable) -> None:
        self.distribution_table = distribution_table