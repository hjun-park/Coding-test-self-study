import pandas as pd

df_all = pd.read_csv(r'D:\hansol_db\all_all.csv')
df_err = pd.read_csv(r'D:\hansol_db\Error Lot list.csv')


def is_same_lot(lot_all, lot_err):
    if str(lot_err).lower() == "nan":
        return '0'

    lot_err = int(lot_err)

    if str(lot_all).strip() == str(lot_err).strip():
        return '1'
    else:
        return '0'


# 1. 데이터 수정
df_all['Date'] = df_all['Date'].apply(lambda x: x.split()[0])

df_merge = pd.merge(df_all, df_err, how='left', on='Date')
df_merge['result'] = 0
df_merge['result'] = df_merge.apply(lambda x: is_same_lot(x['Lot'], x['LoT']), axis=1)

df_merge.to_csv(r'D:\hansol_db\result.csv')
