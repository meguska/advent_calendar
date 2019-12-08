import csv
import pandas
 
pernicky= pandas.read_csv('pernicky_data.csv', index_col='ID', encoding='utf-8')
 
print(pernicky)