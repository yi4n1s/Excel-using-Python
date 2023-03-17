import pandas as pd

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

df['Tax%'] = df['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)

df['Taxes Owed'] = df['Income'] * df['Tax%']

to_drop = ['Area Code', 'First', 'Address']
df.drop(columns=to_drop, inplace=True)

df['Test Col'] = False
df.loc[df['Income'] < 60000, 'Test Col'] = True
print(df.groupby(['Test Col']).mean().sort_values('Income'))

#print(df.loc[(df['City'] == 'Riverside') & (df['First'] == 'John')])
#print(df['Taxes Owed'])