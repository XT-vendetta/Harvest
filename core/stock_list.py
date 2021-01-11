from pandas import read_excel


class TushareAPI:
    def __init__(self):
        pass

    @staticmethod
    def get_index_components(index_id: str, detailed_return: bool = False):
        try:
            wt = read_excel(f"http://www.csindex.com.cn/uploads/file/autofile/cons/{index_id}cons.xls", usecols=[0, 4, 5, 8])
            wt["成分券代码Constituent Code"] = wt["成分券代码Constituent Code"].map(lambda x: str(x).zfill(6))
            if detailed_return:
                return wt
            else:
                return list(wt["成分券代码Constituent Code"])
        except Exception as er:
            print(str(er))


