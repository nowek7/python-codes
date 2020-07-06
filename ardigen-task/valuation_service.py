import sys
import pandas as pd

def help():
    print('Unexpected amount of arguments!')


def valuation_service(currencies: str, data: str, matchings: str) -> None:
    outputColumns = ['matching_id', 'total_price', 'avg_price', 'currency', 'ignored_products_count']

    # Read csv files.
    currenciesDf = pd.read_csv(currencies, delimiter = ',')
    dataDf = pd.read_csv(data, delimiter = ',')
    matchingsDf = pd.read_csv(matchings, delimiter = ',')

    # Add ratio two data dataframe.
    dataDf = pd.merge(left = dataDf, right = currenciesDf, how = 'left', left_on = 'currency', right_on = 'currency')

    # Compute total price and sort.
    dataDf['total_price'] = dataDf['price'] * dataDf['quantity'] * dataDf['ratio']
    dataDf = dataDf.sort_values(['matching_id', 'total_price'], ascending = False)

    # Extract top priced count of currencies.
    topProductsDf = pd.DataFrame()
    for index, row in matchingsDf.iterrows():
        matchingId = row['matching_id']
        topPricedCount = row['top_priced_count']

        selectedDataDf = dataDf[dataDf['matching_id'] == matchingId]

        selectedDataDf = selectedDataDf.assign(avg_price = selectedDataDf['total_price'].mean())
        selectedDataDf = selectedDataDf.assign(ignored_products_count = len(selectedDataDf.index[topPricedCount:]))

        selectedDataDf = selectedDataDf[outputColumns]
        selectedDataDf = selectedDataDf[:topPricedCount]

        topProductsDf = topProductsDf.append(selectedDataDf, ignore_index = True)

    # Save dataframe to csv file.
    topProductsDf.to_csv('top_products.csv', sep = ',', index=False)


if __name__ == "__main__":
    all_arguments = sys.argv
    arguments = all_arguments[1:]

    if len(arguments) != 3:
        help()
    else:
        valuation_service(*arguments)