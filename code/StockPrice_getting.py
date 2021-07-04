import pandas as pd
from pandas_datareader import data

#path 
data_path = '../data/'
result_path = '../result/'

# 株価データを取得
def get_StockPrice(df_tosho):
    #dfの作成
    df_stockprice = pd.DataFrame(index=[], columns=[
        'JP_Code',
        'JP_Company',
        'Market',
        'Category',
        'Date',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume'
    ])

    #株価の取得
    for i in range(len(df_tosho)):
        df = data.DataReader('{}.JP'.format(df_tosho['コード'][i]), 'stooq')
        df.sort_index(inplace=True)
        df.reset_index(inplace=True)

        #dfの整備・結合
        df[['JP_Code','JP_Company','Market', 'Category']] = df_tosho['コード'][i], df_tosho['銘柄名'][i], df_tosho['市場・商品区分'][i], df_tosho['規模区分'][i]
        df_stockprice = pd.concat([df_stockprice,df])
    return df_stockprice

#企業コード辞書の読み込み
df_tosho = pd.read_csv(data_path + 'Tosho_med.csv')

#実行
df_stockprice = get_StockPrice(df_tosho)

#export
df_stockprice.to_excel(result_path + 'Stockprice_Med.xlsx',index=False)
df_stockprice.to_csv(result_path + 'Stockprice_Med.csv',index=False)