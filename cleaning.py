import pandas as pd
import numpy as np
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

df.drop(columns='Address', inplace=True)

df = df.set_index('Area Code')

#df.First = df.First.str.split(expand=True)
#print(df)

df = df.replace(np.nan, 'N/A', regex=True)
to_excel = df.to_excel('modified.xlsx')

#print(df.loc[8074])
#print(df.iloc[0])
#print(df.loc[8074:, 'First'])
#print(df.First.str.split(expand=True))

