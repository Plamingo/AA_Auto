
import pandas as pd

dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
#dict key가 열이름, value가 프레임의 열을 구성
df = pd.DataFrame(dict_data)

df2 = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                   index=['준서','예은'],
                   columns=['나이','성별','학교'])

print(df)
print('\n')
#print(type(df))
print('\n')
print(df.index)
print(df.columns)