import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

csv_path = "data/expenses.csv"

def execution():
    try:
        df = pd.read_csv(csv_path)

        if df.empty:
            st.header("Please add some expenses before analysing it")
            return

        # Normalize column names (strip spaces/case)
        df.columns = [c.strip() for c in df.columns]

        # ---- Max amount ----
        max_amt = df[df["Amount"] == df["Amount"].max()]
        st.subheader("You are spending the most here 😭")
        st.dataframe(max_amt.reset_index(drop=True))

        # ---- Min amount ----
        min_amt = df[df["Amount"] == df["Amount"].min()]
        st.subheader("You are spending the least here 😊")
        st.dataframe(min_amt.reset_index(drop=True))

        # ---- Most / least transactions by date ----
        tx_by_date = df.groupby("Date").size()
        most_transactions_date = tx_by_date.nlargest(1)
        
        st.subheader("You made the most number of transactions on 📅")
        st.dataframe(most_transactions_date.reset_index().rename(columns={0: "Count"}))

        least_transactions_date = tx_by_date.nsmallest(1)
        st.subheader("You made the least number of transactions on 📅")
        st.dataframe(least_transactions_date.reset_index().rename(columns={0: "Count"}))

        # ---- Categories mode / least spent category ----
        mode_category = df["Category"].mode()
        st.subheader("The categories for which you are spending the most are 😭")
        st.dataframe(mode_category.to_frame("Category"))

        st.subheader("The categories for which you are spending the least are 😊")
        least_spent_category = df["Category"].value_counts().idxmin()
        st.dataframe(df[df["Category"] == least_spent_category].reset_index(drop=True))

        # ---- Word Cloud (uses 'Description' column; fallback to 'Decription') ----
        desc_col = "Description" if "Description" in df.columns else ("Decription" if "Decription" in df.columns else None)
        if desc_col is not None:
            description_text = " ".join(df[desc_col].dropna().astype(str).tolist())
            if description_text.strip():
                st.subheader("Wordcloud for the description of your expenses 😶‍🌫️😶‍🌫️😶😶😶‍🌫️😶‍🌫️😶😶😶‍🌫️😶‍🌫️")
                wc = WordCloud(width=800, height=400, background_color="white")
                image = wc.generate(description_text).to_array()

                fig, ax = plt.subplots(figsize=(8, 4))
                ax.imshow(image)
                ax.axis("off")
                st.pyplot(fig)
            else:
                st.info("No description text available to generate a word cloud.")
        else:
            st.info("No 'Description' column found to generate a word cloud.")

    except Exception as e:
        st.header("Please add some expenses before analysing it")
        st.caption(f"(Error: {e})")

execution()



