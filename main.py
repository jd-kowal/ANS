import src.rANS as r_ans
import src.tANS as t_ans
import src.uANS as u_ans


class Main:
    @staticmethod
    def main() -> None:
        """An example of using tANS API. As an argument please input path to file in which you have message to compress"""
        t_ans.TableANSEncodingAPI("sample_data").useTableANSEncDec()


if __name__ == "__main__":
    Main.main()
