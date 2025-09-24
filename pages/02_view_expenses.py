import streamlit as st
import pandas as pd
#import os
import matplotlib.pyplot as plt

csv_path = "data/expenses.csv"




def execution():
    df=pd.read_csv(csv_path)
    total=df['Amount'].max()
    st.markdown(f"### Gold coins: {int(total)//200} 🪙")

    date_from=st.date_input('From Date :date:')
    date_to=st.date_input('To Date :date:')

    st.write('Amount :money_with_wings:')
    amount_min = st.slider('Minimum Value',min_value=0,max_value=20000,value=0,step=10)
    amount_max = st.slider('Maximum Value',min_value=0,max_value=20000,value=0,step=10)

    category=st.multiselect('Categories',["Housing", "Utilities", "Transportation", "Food", "Healthcare","Insurance", "Debt Payments", "Entertainment", "Personal Care","Education", "Savings", "Taxes", "Miscellaneous"],placeholder="You can choose multiple option(s)")

    df['Date']= pd.to_datetime(df['Date'])
    date_from,date_to = pd.to_datetime(date_from),pd.to_datetime(date_to)

    if len(category)==0:
        condtion=((df['Date']>=date_from) &
                  (df['Date']<=date_to) &
                  (df['Amount']>=amount_min) &
                  (df['Amount']<=amount_max))
    else:
        condtion=((df['Date']>=date_from) &
                  (df['Date']<=date_to) &
                  (df['Amount']>=amount_min) &
                  (df['Amount']<=amount_max) &
                  (df['Category'].isin(category)))
    df=df[condtion]
    st.title("Expenses 💸💸")
    st.dataframe(df.reset_index(drop=True))
    
    
    st.title("Amount")
    st.line_chart(df["Amount"])
                

    st.title('Categories :card_index_dividers:')
    category_df=df.groupby('Category')['Amount'].sum()
    fig,ax=plt.subplots()
    ax.pie(category_df,labels=category_df.index,autopct='%.2f')
    st.pyplot(fig)


execution()


