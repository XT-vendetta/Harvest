import unittest
from datetime import date
from core.equity import Equity
from fundamental.share_holder import ShareHolder


class MyTestCase(unittest.TestCase):
    def test_from_website_1(self):
        equity = Equity(603290, "斯达半导")
        share_holder = ShareHolder.from_website(equity, date(2020, 9, 30))[0]
        target_share_holders = [
            {'name': '中国工商银行股份有限公司－融通中国风1号灵活配置混合型证券投资基金', 'quantity': 1146295, 'pct': 2.866, 'share_holder_type': '境内法人股'},
            {'name': '招商银行股份有限公司－银河创新成长混合型证券投资基金', 'quantity': 900891, 'pct': 2.252, 'share_holder_type': '境内法人股'},
            {'name': 'MORGAN STANLEY&CO.INTERNATIONAL PLC.', 'quantity': 884864, 'pct': 2.212, 'share_holder_type': '境外法人股'},
            {'name': '王君', 'quantity': 830335, 'pct': 2.076, 'share_holder_type': '自然人股'},
            {'name': '中国农业银行股份有限公司－长城久嘉创新成长灵活配置混合型证券投资基金', 'quantity': 729434, 'pct': 1.824, 'share_holder_type': '境内法人股'},
            {'name': '中国建设银行股份有限公司－南方信息创新混合型证券投资基金', 'quantity': 700235, 'pct': 1.751, 'share_holder_type': '境内法人股'},
            {'name': '中国建设银行股份有限公司－银河行业优选混合型证券投资基金', 'quantity': 570992, 'pct': 1.427, 'share_holder_type': '境内法人股'},
            {'name': '泰康人寿保险有限责任公司－分红－个人分红－019L－FH002沪', 'quantity': 528500, 'pct': 1.321, 'share_holder_type': '境内法人股'},
            {'name': '中国银行股份有限公司－大成科技消费股票型证券投资基金', 'quantity': 497407, 'pct': 1.244, 'share_holder_type': '境内法人股'},
            {'name': '招商银行股份有限公司－泓德睿泽混合型证券投资基金', 'quantity': 446854, 'pct': 1.117, 'share_holder_type': '境内法人股'}
        ]
        self.assertEqual(date(2020, 9, 30), share_holder.due_date)
        self.assertEqual(date(2020, 10, 30), share_holder.report_date)
        self.assertEqual(target_share_holders, share_holder.share_holder_df.to_dict('records'))

    def test_from_website_2(self):
        equity = Equity(603290, "斯达半导")
        share_holder = ShareHolder.from_website(equity, date(2020, 6, 30))[0]
        target_share_holders = [
            {'name': 'MORGAN STANLEY&CO.INTERNATIONAL PLC.', 'quantity': 1193279, 'pct': 2.983, 'share_holder_type': '境外法人股'},
            {'name': '中国建设银行股份有限公司－易方达信息产业混合型证券投资基金', 'quantity': 874500, 'pct': 2.186, 'share_holder_type': '境内法人股'},
            {'name': '中国国际金融股份有限公司客户信用交易担保证券账户', 'quantity': 830335, 'pct': 2.076, 'share_holder_type': '境内法人股'},
            {'name': '中国工商银行股份有限公司－融通中国风1号灵活配置混合型证券投资基金', 'quantity': 827404, 'pct': 2.069, 'share_holder_type': '境内法人股'},
            {'name': '中信证券－中信银行－中信证券红利价值一年持有混合型集合资产管理计划', 'quantity': 630724, 'pct': 1.577, 'share_holder_type': '境内法人股'},
            {'name': '交通银行股份有限公司－汇丰晋信低碳先锋股票型证券投资基金', 'quantity': 596300, 'pct': 1.491, 'share_holder_type': '境内法人股'},
            {'name': '中国农业银行股份有限公司－长城久嘉创新成长灵活配置混合型证券投资基金', 'quantity': 575126, 'pct': 1.438, 'share_holder_type': '境内法人股'},
            {'name': '中国工商银行股份有限公司－易方达科翔股票型证券投资基金', 'quantity': 505447, 'pct': 1.264, 'share_holder_type': '境内法人股'},
            {'name': '方士雄', 'quantity': 407000, 'pct': 1.018, 'share_holder_type': '自然人股'},
            {'name': '兴业银行股份有限公司－兴全精选混合型证券投资基金', 'quantity': 370103, 'pct': 0.925, 'share_holder_type': '境内法人股'}
        ]

        self.assertEqual(date(2020, 6, 30), share_holder.due_date)
        self.assertEqual(date(2020, 8, 28), share_holder.report_date)
        self.assertEqual(target_share_holders, share_holder.share_holder_df.to_dict('records'))

    def test_from_website_3(self):
        equity = Equity(603290, "斯达半导")
        share_holder = ShareHolder.from_website(equity, date(2020, 9, 30), False)[0]
        target_share_holders = [
            {'name': '香港斯达控股有限公司', 'quantity': 71266800, 'pct': 44.54, 'share_holder_type': '限售流通股'},
            {'name': '浙江兴得利纺织有限公司', 'quantity': 29294388, 'pct': 18.31, 'share_holder_type': '限售流通股'},
            {'name': '嘉兴富瑞德投资合伙企业(有限合伙)', 'quantity': 8684964, 'pct': 5.43, 'share_holder_type': '限售流通股'},
            {'name': '嘉兴兴泽投资合伙企业(有限合伙)', 'quantity': 5899296, 'pct': 3.69, 'share_holder_type': '限售流通股'},
            {'name': '中国工商银行股份有限公司－融通中国风1号灵活配置混合型证券投资基金', 'quantity': 1146295, 'pct': 0.72, 'share_holder_type': '流通A股'},
            {'name': '宁波展兴投资有限公司', 'quantity': 1099644, 'pct': 0.69, 'share_holder_type': '限售流通股'},
            {'name': '招商银行股份有限公司－银河创新成长混合型证券投资基金', 'quantity': 900891, 'pct': 0.56, 'share_holder_type': '流通A股'},
            {'name': '深圳市鑫亮五金制品有限公司', 'quantity': 887856, 'pct': 0.55, 'share_holder_type': '限售流通股'},
            {'name': 'MORGAN STANLEY&CO.INTERNATIONAL PLC.', 'quantity': 884864, 'pct': 0.55, 'share_holder_type': '流通A股'},
            {'name': '王君', 'quantity': 830335, 'pct': 0.52, 'share_holder_type': '流通A股'}
        ]

        self.assertEqual(date(2020, 9, 30), share_holder.due_date)
        self.assertEqual(date(2020, 10, 30), share_holder.report_date)
        self.assertEqual(target_share_holders, share_holder.share_holder_df.to_dict('records'))

    def test_from_website_4(self):
        equity = Equity(600028, "中国石化")
        share_holder_1 = ShareHolder.from_website(equity, None, True, True)
        share_holder_2 = ShareHolder.from_website(equity, None, True, False)
        self.assertNotEqual(len(share_holder_1), len(share_holder_2))

    def test_get_request_url(self):
        equity = Equity(600028, "中国石化")
        url1 = ShareHolder.get_request_url(equity, True, True)
        url2 = ShareHolder.get_request_url(equity, False, True)
        url3 = ShareHolder.get_request_url(equity, True, False)
        url4 = ShareHolder.get_request_url(equity, False, False)
        self.assertEqual(url1, 'https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/600028.phtml')
        self.assertEqual(url2, 'https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/600028.phtml')
        self.assertEqual(url3, 'https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/600028/displaytype/30.phtml')
        self.assertEqual(url4, 'https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/600028/displaytype/30.phtml')

    def test_get_count_history(self):
        equity = Equity(600028, "中国石化")
        count_history = ShareHolder.get_count_history(equity)
        self.assertEqual(list(count_history.loc[count_history["截止日期"] == date(2020, 9, 30)]["股东户数"])[0], 571928)
        self.assertEqual(list(count_history.loc[count_history["截止日期"] == date(2020, 6, 30)]["股东户数"])[0], 563689)
        self.assertEqual(list(count_history.loc[count_history["截止日期"] == date(2020, 3, 31)]["股东户数"])[0], 553217)
        self.assertEqual(list(count_history.loc[count_history["截止日期"] == date(2019, 12, 31)]["股东户数"])[0], 478617)
        self.assertEqual(list(count_history.loc[count_history["截止日期"] == date(2019, 9, 30)]["股东户数"])[0], 502791)


if __name__ == '__main__':
    unittest.main()
