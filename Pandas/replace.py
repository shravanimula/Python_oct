import pandas as pd
data=pd.DataFrame({'city':['knr','hyd','AP','wgl','srl'],
                    'event':['IT','music','poetry','theatre','comedy'],
                    'cost':[10000,5000,15000,12000,8000]})
#creting index
index1=[pd.Period('02-2023'),pd.Period('04-2023'),pd.Period('06-2023'),
        pd.Period('08-2023'),pd.Period('10-2023')]

#set the index
data.index=index1
print(data)
