import pandas as pd
df = pd.read_excel("test.xlsx")
df['sum']=df['Python']+df['Math']
df.to_excel('test1.xlsx')