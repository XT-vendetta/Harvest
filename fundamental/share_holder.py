import requests
from datetime import date, datetime
from typing import List
from pandas import DataFrame

from core.equity import Equity
from bs4 import BeautifulSoup


class ShareHolderItem(dict):
    def __init__(self, name: str, quantity: int, pct: float, share_holder_type: str):
        super().__init__({
            'name': name,
            'quantity': quantity,
            'pct': pct,
            'share_holder_type': share_holder_type
        })

    @classmethod
    def from_tr_node(cls, tr_node):
        l: list = tr_node.find_all("td")

        if l[2].text[-1] in ['↑', '↓']:
            parsed_l2 = l[2].text[:-1]
        else:
            parsed_l2 = l[2].text

        if l[3].text[-1] in ['↑', '↓']:
            parsed_l3 = l[3].text[:-1]
        else:
            parsed_l3 = l[3].text

        return cls(
            l[1].text,
            int(parsed_l2),
            float(parsed_l3),
            l[4].text,
        )


class ShareHolder:
    def __init__(self,
                 equity: Equity = None,
                 due_date: date = None,
                 report_date: date = None,
                 share_holder_count: int = None,
                 share_holder_df: DataFrame = None):
        self.equity = equity
        self.due_date = due_date
        self.report_date = report_date
        self.share_holder_count = share_holder_count
        self.share_holder_df = share_holder_df

    @staticmethod
    def get_request_url(equity: Equity, is_circulate: bool = True, detailed: bool = False):
        circulate_str = 'vCI_CirculateStockHolder' if is_circulate else 'vCI_StockHolder'
        detailed_str = '' if detailed else '/displaytype/30'
        return f'https://vip.stock.finance.sina.com.cn/corp/go.php/{circulate_str}/stockid/{equity.id}{detailed_str}.phtml'

    @staticmethod
    def get_response_from_website(equity: Equity, is_circulate: bool = True, detailed: bool = False):
        url = ShareHolder.get_request_url(equity, is_circulate, detailed)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        if is_circulate:
            return soup.find("table", {"id": "CirculateShareholderTable"})
        else:
            return soup.find("table", {"id": "Table1"})

    @classmethod
    def from_website(
            cls,
            equity: Equity,
            due_date: date = None,
            is_circulate: bool = True,
            detailed: bool = False) -> List["ShareHolder"]:
        share_holder_table = ShareHolder.get_response_from_website(equity, is_circulate, detailed)
        all_tr = share_holder_table.find_all("tr")
        return_value = []
        for i in range(len(all_tr)):
            due_date_tr = all_tr[i]
            due_date_td = due_date_tr.find("td")
            if due_date_td is None:
                continue
            strong_node = due_date_td.find("strong")
            if strong_node is not None and len(strong_node) > 0:
                if (is_circulate and strong_node.text == "截止日期") or (not is_circulate and strong_node.text == "截至日期"):
                    actual_due_date = datetime.strptime(due_date_td.find_next("td").text, "%Y-%m-%d").date()
                    if due_date == actual_due_date or due_date is None:
                        report_date_tr = all_tr[i + 1]
                        report_date_td = report_date_tr.find("td")
                        assert report_date_td.text == "公告日期", "Current TR is not report date TR."
                        try:
                            report_date = datetime.strptime(report_date_td.find_next("td").text, "%Y-%m-%d").date()
                        except ValueError:
                            # old data does not have report date
                            report_date = None

                        if not is_circulate:
                            share_holder_count_tr = all_tr[i + 3]
                            share_holder_count_td = share_holder_count_tr.find("td")
                            assert share_holder_count_td.text == "股东总数", "Current TR is not share holder count TR."
                            share_holder_count_text = share_holder_count_td.find_next("td").text
                            try:
                                share_holder_count = int(share_holder_count_text)
                            except ValueError:
                                assert share_holder_count_text[-6:] == "查看变化趋势"
                                share_holder_count = int(share_holder_count_text[:-6])
                        else:
                            share_holder_count = None

                        if is_circulate:
                            share_holder_records = [ShareHolderItem.from_tr_node(all_tr[i + 3 + j]) for j in range(10)]
                        else:
                            share_holder_records = [ShareHolderItem.from_tr_node(all_tr[i + 6 + j]) for j in range(10)]

                        return_value.append(
                            cls(equity,
                                actual_due_date,
                                report_date,
                                share_holder_count,
                                DataFrame.from_records(share_holder_records)))
                        if due_date is not None:
                            break
        return return_value
