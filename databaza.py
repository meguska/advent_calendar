import csv
import pandas
 
pernicky1= pandas.read_csv('pernicky_data.csv', encoding='utf-8')
colu= pernicky1.columns

neviem= pernicky1[['ID', 'Aktivita']]
data = pernicky1.values.tolist()
print(data)