import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 73, 63, 65, 55, 77]}

df = pd.DataFrame(web_stats)

# # printing df
# print(df)
# print(df.head(3))
# print(df.tail(2))
#
# # setting 'Day' as 'index'
# print(df.set_index('Day'))
# print(df.head())
#
# # Imp fmt of setting 'Day' as 'index'
# df = df.set_index('Day')
# print(df.head())
#
# # Another fmt of setting 'Day' as 'index'
# df.set_index('Day', inplace=True)
# print(df.head())

# referencing a specific set
print(df['Visitors'])
# or
print (df.Visitors)
