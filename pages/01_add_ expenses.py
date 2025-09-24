import streamlit as st 
import pandas as pd
import os 
folder_path='data'
excel_file_path=r'data/expenses.csv'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
if not os.path.exists(excel_file_path):
    expenses=pd.DataFrame(columns=['Date','Category','Description','Currency Type','Amount'])
    expenses.to_csv(excel_file_path,index=False)

def clear():
    st.session_state.desc=''
    st.session_state.am=0

def insert(date, category, description, curency_type, amount):
    df=pd.read_csv(excel_file_path)
    lenght=len(df)
    if description!='' and amount>0:
        df.loc[lenght]=[date, category, description, curency_type, amount]
        df.to_csv(excel_file_path, index=False)
        st.balloons()
    else:
        st.error('Please provide a description and a valid amount value greater than zero.', icon="🚨")
date=st.date_input('Date :calendar:', key='date')
category=st.selectbox('Category :card_index_dividers:',("Housing","Utilities","Transportation","Food","Healthcare","Insurance","Debt Payments","Entertainment","Personal Care","Education","Savings","Taxes","Miscellaneous"))
description=st.text_input('Description :flashlight:', key='desc')
curency_type = st.selectbox('Currency type: :heavy_dollar_sign:', ('Dollar','Rupee','Euros','Pound','Australian Dollar','Yen','Yuan','Canadian Dollar','Swiss Franc','Other'))
amount = st.number_input('Amount :money_mouth_face:', key='am', min_value=0, step=1, max_value=10000000000)

col1,col2=st.columns(2)
with col1:
   add_bt = st.button('Add Expense :money_with_wings:')
with col2:
    st.button('Clear :scissors:',on_click=clear)

if add_bt:
    insert(date, category, description, curency_type, amount)