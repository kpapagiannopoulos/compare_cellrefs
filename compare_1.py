import pandas as pd
col_list = ["SECTOR_ID"]
df1 = pd.read_csv('file1', low_memory=False, usecols=col_list )
df2 = pd.read_csv('file2', low_memory=False, usecols=col_list)

result = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
print(result)
result.to_csv ('compare_export.csv')
