import pandas as pd
import numpy as np
from datetime import datetime
import sys

from pandas.conftest import axis

df_all = pd.read_csv(r'D:\hansol_db\all_all.csv')
df_err = pd.read_csv(r'D:\hansol_db\Error Lot list.csv')
i = 1
j = 1
def is_same_lot(lot_all, lot_err):
    global i, j
    if str(lot_err).lower() == "nan":
        return '0'

    lot_err = int(lot_err)

    print(f'=========== {j}: compare : {lot_all} < ----- > {lot_err}')
    if str(lot_all).strip() == str(lot_err).strip():
        print(f'{i}::{str(lot_all)} is same with {str(lot_err)}')
        return '1'
    else:
        return '0'

    i += 1
    j += 1


print(df_all.columns)
print(df_err.columns)
print('--------')
print(str(df_all['Date'][0]))

# 1. 데이터 수정
df_all['Date'] = df_all['Date'].apply(lambda x: x.split()[0])

df_merge = pd.merge(df_all, df_err, how='left', on='Date')
df_merge['result'] = 0
print(df_merge.iloc[0])
print(len(df_merge.index))
print(df_merge.columns)

df_merge['result'] = df_merge.apply(lambda x: is_same_lot(x['Lot'], x['LoT']), axis=1)

df_merge.to_csv(r'D:\hansol_db\result.csv')
