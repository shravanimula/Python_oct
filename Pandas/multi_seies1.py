import pandas as pd
author=['Jitender', 'Purnima',
                'Arpit', 'Jyoti']
article=[210, 211, 114, 178]


auth_series = pd.Series(author)
article_series = pd.Series(article)
frame = {'Author': auth_series,
                'Article': article_series}
result = pd.DataFrame(frame)
print(result)
