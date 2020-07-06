from valuation_service import valuation_service

import pandas as pd
import unittest

class TestValuationServiceMethod(unittest.TestCase):
    def setUp(self):
        self.currenciesDf = pd.read_csv('currencies.csv', delimiter=',')
        self.dataDf = pd.read_csv('data.csv', delimiter=',')
        self.matchingsDf = pd.read_csv('matchings.csv', delimiter=',')

        self.topProductsDf = pd.read_csv('top_products.csv', delimiter=',')

        self.currenciesColumns = ['currency', 'ratio']
        self.dataColumns = ['id', 'price', 'currency', 'quantity', 'matching_id']
        self.matchingsColumns = ['matching_id', 'top_priced_count']
        self.topProductsColumns = ['matching_id', 'total_price', 'avg_price', 'currency', 'ignored_products_count']

    def test_currencies(self):
        currenciesDfColumns = list(self.currenciesDf.columns.values)
        self.assertEqual(len(currenciesDfColumns), len(self.currenciesColumns))
        self.assertListEqual(currenciesDfColumns, self.currenciesColumns)

    def test_data(self):
        dataDfColumns = list(self.dataDf.columns.values)
        self.assertEqual(len(dataDfColumns), len(self.dataColumns))
        self.assertListEqual(dataDfColumns, self.dataColumns)

    def test_matchings(self):
        matchingsDfColumns = list(self.matchingsDf.columns.values)
        self.assertEqual(len(matchingsDfColumns), len(self.matchingsColumns))
        self.assertListEqual(matchingsDfColumns, self.matchingsColumns)

    def test_top_products(self):
        topProductsDfColumns = list(self.topProductsDf.columns.values)
        self.assertEqual(len(topProductsDfColumns), len(self.topProductsColumns))
        self.assertListEqual(topProductsDfColumns, self.topProductsColumns)

        for index, row in self.matchingsDf.iterrows():
            matchingId = row['matching_id']
            topPricedCount = row['top_priced_count']

            selectedDataDf = self.topProductsDf[self.topProductsDf['matching_id'] == matchingId]

            topPricedCount = len(selectedDataDf.index[:topPricedCount])
            ignoredProduct = len(selectedDataDf.index[topPricedCount:])

            self.assertEqual(topPricedCount, len(selectedDataDf.index))

if __name__ == '__main__':
    unittest.main()