import streamlit as st 
import pandas as pd
import os 
folder_path='data'
excel_file_path=r'data/feedback.csv'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
if not os.path.exists(excel_file_path):
    fd=pd.DataFrame(columns=['Name','Feedback','Rating'])
    fd.to_csv(excel_file_path,index=False)

def clear():
    st.session_state.name=''
    st.session_state.feed=0

name=st.text_input('Enter your Name: ',key='name')
feedback=st.text_input('Please enter your valuable feedback: ',key='feed')
rating=st.slider('Please provide us from 1 to 5: ',min_value=1,max_value=5,key='rating')

emoji_holder=st.empty()
if rating==1:
    emoji_holder.subheader(" We will definitely improve"+":weary:")
if rating==2:
    emoji_holder.subheader(" We will definitely improve your experience"+":disappointed_relieved:")
if rating==3:
    emoji_holder.subheader(" Thanks !!"+":persevere:")
if rating==4:
    emoji_holder.subheader(" Oh you are loving it!!!"+":smiley_cat:")
if rating==5:
    emoji_holder.subheader(" Thank you so much for your love"+":heart_eyes_cat:")



def insert(Name, Feedback, Rating):
    df=pd.read_csv(excel_file_path)
    lenght=len(df)
    df.loc[lenght]=[Name, Feedback, Rating]
    df.to_csv(excel_file_path, index=False)
    st.balloons()

col1,col2=st.columns([0.2,0.8])
with col1:
    submit=st.button('Submit',key='submit')
    if submit and name and feedback:
        insert(name, feedback, rating)
        st.success('Thank you for your feedback :smiley:', icon="✅")
        emoji_holder.empty()
with col2:
    clear=st.button('Clear :scissors:',on_click=clear)

st.subheader('Past Feedbacks')
df=pd.read_csv(excel_file_path)
st.dataframe(df)