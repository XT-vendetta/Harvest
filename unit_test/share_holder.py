import unittest
from datetime import date
from core.equity import Equity
from fundamental.share_holder import ShareHolder


class MyTestCase(unittest.TestCase):
    def test_from_website_1(self):
        equity = Equity(603290, "斯达半导")
        share_holder = ShareHolder.from_website(equity, date(2020, 9, 30))
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
        self.assertEqual(target_share_holders, [x.__dict__ for x in share_holder.info.values()])

    def test_from_website_2(self):
        equity = Equity(603290, "斯达半导")
        share_holder = ShareHolder.from_website(equity, date(2020, 6, 30))
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
        self.assertEqual(target_share_holders, [x.__dict__ for x in share_holder.info.values()])


if __name__ == '__main__':
    unittest.main()
