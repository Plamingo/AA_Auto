# streamlit 웹페이지 구현 (pip install streamlit)
# 실행 : streamlit run *.py
# 중지 : Ctrl + C
# pip install scikit-learn : 설치
# pip install matplotlib : 설치

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris #사이킷런의 아이리스 데이터 가져옴
import matplotlib.pyplot as plt

iris_dataset = load_iris()

df = pd.DataFrame(data=iris_dataset.data,columns=iris_dataset.feature_names)
df.columns = [col_name.split(' (cm)')[0] for col_name in df.columns]
df['species'] = iris_dataset.target

species_dict = {0 : 'setosa', 1 : 'versicolor', 2 : 'virginica'}

def mapp_species(x):
    return species_dict[x]

df['species'] = df['species'].apply(mapp_species)
print(df)

st.subheader('this is table')
st.table(df.head())
#st.title('Hello This is example')
#st.header('this is header')

# 사이드바 구현, 체크박스/버튼 등을 추가
#st.sidebar.title('Test side-bar')
#st.sidebar.checkbox('Checkbox')

