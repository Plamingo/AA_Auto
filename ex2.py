import streamlit as st
import pandas as pd

#Data = pd.read_excel('Data_Entry.xlsx',
#                     sheet_name='Test1') # Index 사용가능 sheet_name=1 0부터 시작 

# sheet_name=None 으로 설정하면 모든 시트데이터 불러옴
# usecols=[1,2] 원하는 열의 데이터만 저장
# usecols=['Direction','Region'] 원하는 열의 label 사용

# print(Data)

#def life_game():
#    name = input("Enter your name: ")
#    age = int(input("Enter your age: "))
#    money = 100
#    print(f"Welcome, {name}! You start your life with ${money}")
import openpyxl

workbook = openpyxl.load_workbook("Data_Entry.xlsx")
sheet = workbook.active

data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, address, phone_number, email = row[0], row[1], row[2], row[3]
    data.append({"이름":name, "이메일":email})

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False, encoding = "utf-8")

st.table(df.head())