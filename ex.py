# streamlit 웹페이지 구현 (pip install streamlit)
# 실행 : streamlit run *.py
# 중지 : Ctrl + C
# pip install scikit-learn : 설치
# pip install matplotlib : 설치
# streamlit run *.py --server.port 8888

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris #사이킷런의 아이리스 데이터 가져옴
import matplotlib.pyplot as plt
import time
import datetime
import io
from pathlib import Path

#iris_dataset = load_iris()
#df = pd.DataFrame(data=iris_dataset.data,columns=iris_dataset.feature_names)
#df.columns = [col_name.split(' (cm)')[0] for col_name in df.columns]
#df['species'] = iris_dataset.target
#species_dict = {0 : 'setosa', 1 : 'versicolor', 2 : 'virginica'}

# emojis : https://www.webfx.com/tools/emoji-cheat-sheet
# streamlit emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(
    page_title='Test Result Share Dashboard',
    page_icon=':bar_chart:',
    layout='wide',
    )

# File uploading module
#@st.cache_data # 캐시를 이용하여 큰 데이터를 빠르게 읽어오기  cache_data 차이?

#fl = st.file_uploader(":file_folder: upload a file",type=(["csv","xlsx"]))
#if fl is not None :
#    filename = fl.name
#    st.success(filename)
#    df = pd.read_excel(filename)
#else :
#    current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
#    EXCEL_FILE = current_dir / 'Data_Entry.xlsx'
#    df = pd.read_excel(io=EXCEL_FILE,engine='openpyxl',sheet_name='Test1')

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Data_Entry.xlsx'

@st.cache_data # 캐시를 이용하여 큰 데이터를 빠르게 읽어오기  cache_data 차이?
def get_data_from_excel():
    df = pd.read_excel(
        io = EXCEL_FILE,
        engine='openpyxl',
        sheet_name='Test1',
        #usecols='B:D',
        #header=3,
        #skiprows=3,
        #nrows=1000,
        )
    df['Date'] = pd.to_datetime(df['Date'], format="YYYY-MM-DD").dt.date    #dt 속성을 사용하여 date정보만 추출
    return df

df = get_data_from_excel()
#st.echo()
#with st.echo():
#     st.write('Code will be executed and printed')

st.sidebar.header('프로젝트 선택 :')
    
project_select = st.sidebar.multiselect(
    'Select the project :',
    options = df['Project'].unique(),
    default = df['Project'].unique(),
)

row_select = st.sidebar.multiselect(
    "Select the rows :",
    options = df['Row'].unique(),
    default = df['Row'].unique(),
)

option_select = st.sidebar.multiselect(
    "Select the options :",
    options = df['Seat_option'].unique(),
    default = df['Seat_option'].unique(),
)
    #"[Naver](https://www.naver.com)"  
    # format: 2016-05-26 0:00:00
    #df['Date'] = pd.to_datetime()
    #start_dt = st.date_input("시작일자",datetime.datetime(2023,1,1))
    #end_dt = st.date_input("종료일자",datetime.datetime.now())
    #"[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    #"[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)

#filter_button = st.sidebar.button("filter apply")

#if filter_button :
#    st.sidebar.success("Filter applied!")

df_selection = df.query(
        "Project == @project_select & Row == @row_select & Seat_option == @option_select "
    )

master_key = st.sidebar.text_input("Master Key", key="chatbot_api_key", type="password")
#filtered_df = df[df['Project'].isin(project_select)]

def save_xls(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine = 'xlsxwriter')
    df.to_excel(writer,sheet_name='sheet1',index=False)
    writer.close()
    processed_data = output.getvalue()
    return processed_data

st.download_button(
    label="Download data as excel",
    data=save_xls(df_selection),
    file_name="export_data.xlsx",
    mime='application/vnd.ms-excel',
    key='excel_download'
)

if master_key == "1":
    st.sidebar.success('welcome master')
    st.title(":bar_chart: H-PT, SLD Test Result")
    st.dataframe(df_selection,width=1400,height=700)


#st.markdown("---")
st.title(":bar_chart: H-PT, SLD Test Result")
#st.markdown("##") #한칸 띄우는 기능
st.dataframe(df_selection,width=1400,height=700)


st.markdown("---")

button1 = st.button('Example')
st.link_button("Go to gallery", "https://streamlit.io/gallery")

#if button1 ==True :
#    st.write('gogogo')
# 
#with st.spinner(text='In progress'):
#    time.sleep(5)
#    st.success('Done')22

#bar = st.progress(50)
#time.sleep(3)
#bar.progress(100)

#st.table(df.iloc[0:10])
#st.title('Hello This is example')
#st.header('this is header')

# 사이드바 구현, 체크박스/버튼 등을 추가
#st.sidebar.title('Test side-bar')
#st.sidebar.checkbox('Checkbox')

#if st.user.email == 'jane@email.com':
#    st.write("1")#display_jane_content()
#elif st.user.email == 'adam@foocorp.io':
#    st.write("2")#display_adam_content()
#else:
#    st.write("Please contact us to get access!")

#color = st.color_picker('Pick A Color', '#00f900')
#st.write('The current color is', color)

#st.experimental_user.email

#with st.form(key='my_foam'):
#    username=st.text_input('Username')
#    password=st.text_input('Password')
#    st.form_submit_button('Login')

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")