"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая 
состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
"""
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI': lst})
df.head()

new_df = pd.DataFrame(0, index=df.index, columns=['human', 'robot'])

for i in range(len(df)):
    new_df.at[i, df.at[i, 'whoAmI']] = 1

print(new_df)

"""
    human  robot
0       1      0
1       1      0
2       1      0
3       0      1
4       0      1
5       0      1
6       0      1
7       1      0
8       0      1
9       1      0
10      0      1
11      1      0
12      1      0
13      0      1
14      0      1
15      1      0
16      1      0
17      0      1
18      1      0
19      0      1
"""
print()

print(pd.get_dummies(df['whoAmI'], dtype='int'))

"""
    human  robot
0       1      0
1       1      0
2       1      0
3       0      1
4       0      1
5       0      1
6       0      1
7       1      0
8       0      1
9       1      0
10      0      1
11      1      0
12      1      0
13      0      1
14      0      1
15      1      0
16      1      0
17      0      1
18      1      0
19      0      1
"""