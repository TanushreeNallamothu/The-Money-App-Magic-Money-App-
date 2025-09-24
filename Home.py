import streamlit as st

tab1,tab2,tab3=st.tabs(['🌟💫 About Me 🌟💫', '🥋🎼🎹🌸📚 Hobbies 🥋🎼🎹🌸📚', '📖 Contact 📖 '])

with tab1:
    col1,col2=st.columns([0.3,0.7])
    with col1:
        st.image('unicorngirl.png')
        st.subheader("Tanushree Nallamothu :sunglasses:")
    with col2:
        st.write(
            "Hello, I am Tanushree Nallamothu, a 5th grader and content developer :computer: . " \
            "My parents find it challenging to manage and track their expenses. " \
            "So, I created a website  to help them in tracking and managing their expenses. " \
            "You can use this website to manage and track your expenses as well. " \
            "I hope you all like it."
        )

with tab2:
    col1,col2=st.columns([0.3,0.7])
    with col1:
        st.markdown("""
            My hobbies are:
            - playing with my sister
            - playing piano 
            - drawing
            - coloring
            - haveing fun with my family
            - going to school
            - learning
                """)
    with col2:
        st.image('unicorngirl.png')

with tab3:
    st.markdown('''
            Contact
            - Harry Potter@gmail.com(Gmail)
            - 1234567890 (Phone Number)
            ''')
    
    
