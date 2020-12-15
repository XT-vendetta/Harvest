import requests
from datetime import date, datetime
from core.equity import Equity
from bs4 import BeautifulSoup


class ShareHolderItem:
    def __init__(self, name: str, quantity: int, pct: float, share_holder_type: str):
        self.name = name
        self.quantity = quantity
        self.pct = pct
        self.share_holder_type = share_holder_type

    @classmethod
    def from_tr_node(cls, tr_node):
        l: list = tr_node.find_all("td")
        return cls(
            l[1].text,
            int(l[2].text),
            float(l[3].text),
            l[4].text,
        )


class ShareHolder:
    def __init__(self,
                 equity: Equity = None,
                 due_date: date = None,
                 report_date: date = None,
                 info: dict = None):
        self.equity = equity
        self.due_date = due_date
        self.report_date = report_date
        self.info = info

    @classmethod
    def from_website(cls, equity, due_date: date):
        url = 'https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/' \
              + f'{equity.id}/displaytype/30.phtml'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        share_holder_table = soup.find("table", {"id": "CirculateShareholderTable"})
        all_tr = share_holder_table.find_all("tr")
        for i in range(len(all_tr)):
            tr = all_tr[i]
            first_td = tr.find("td")
            if first_td is None:
                continue
            strong_node = first_td.find("strong")
            if strong_node is not None and len(strong_node) > 0:
                if strong_node.text == "截止日期":
                    due_date_test = datetime.strptime(
                        tr.find("td", {"class": "tdr", "colspan": "5"}).text,
                        "%Y-%m-%d").date()
                    if due_date == due_date_test:
                        report_date = datetime.strptime(
                            all_tr[i+1].find("td", {"class": "tdr", "colspan": "5"}).text,
                            "%Y-%m-%d").date()
                        info = dict()
                        for j in range(10):
                            info[j+1] = ShareHolderItem.from_tr_node(all_tr[i+3+j])

                        return cls(
                            equity,
                            due_date,
                            report_date,
                            info)

        return cls()
