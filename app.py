import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -------------------- Background Image --------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.ibb.co/6JW4m0R9/flat-lay-fresh-berries-fruits-with-copy-space.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(" Streamlit App🌟")
# load dataset
grocery_df = None

try:
    grocery_df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\ML\Apriori\Groceries_dataset.csv")
    st.write("Dataset load Successfully")
except:
    st.write("Dataset not found")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home🏡", "Data Preview✨", "Analysis📉", "Chatbot🤖", "About✅"])

with tab1:
    st.header("🏠 Welcome to the Groceries Transaction Analyzer")
    st.write("Welcome! Explore your groceries dataset for insights like top items, customer behavior, and association rules.")

    # Toggle button
    show_theory = st.radio("Show detailed dataset theory?", ["Hide", "Show"])
    if show_theory == "Show":
     st.write("""
    ### Groceries Dataset Information

    This dataset contains historical transaction data from a retail store, primarily focusing on 
    the items purchased by different members over a period of time. It is commonly used for 
    Market Basket Analysis (MBA) to discover powerful association rules.
    [Image of market basket analysis diagram]

    **The dataset contains the following key columns:**
    - **Member_number**: A unique identifier for the customer making the purchase.
    - **Date**: The date of the transaction.
    - **itemDescription**: The specific grocery item purchased (e.g., 'whole milk', 'rolls/buns', 'soda').

    **Potential insights you can gain from this dataset:**
    - **Association Rules:** Discover which items are frequently bought together (e.g., customers who buy 'coffee' often buy 'sugar').
    - **Popularity:** Identify the overall most frequently purchased grocery items.
    - **Customer Value:** Analyze purchasing frequency and basket size by member.
    - **Seasonal Trends:** Understand how product demand changes over different months or seasons.

    You can explore the dataset further using the navigation tabs:
    - **Data Preview Tab** – To view the raw uploaded dataset and its structure. 
    - **Analysis Tab** – To perform statistical analysis and generate association rules. 
    - **Chatbot Tab** – To ask specific questions about the dataset and analysis results. 
    """)

    st.success("Use the navigation tabs above to dive into the data and analysis!")

with tab2:
    st.subheader("Basic Information")
    st.write(f"**Total Rows:** {grocery_df.shape[0]}")
    st.write(f"**Total Columns:** {grocery_df.shape[1]}")

    st.subheader("Column Names")
    st.write(list(grocery_df.columns))

    st.subheader("Quick Preview")
    st.dataframe(grocery_df.head()) 

    st.info("This dataset contains grocery sales data. Use other tabs for detailed analysis and visualizations.")

with tab3:
    st.header("📈 Grocery Data Analysis")

    st.subheader("Q1: Top 10 Items Sold")
    top_items = grocery_df['itemDescription'].value_counts().head(10)

    fig1, ax1 = plt.subplots()
    ax1.bar(top_items.index, top_items.values)
    plt.xticks(rotation=90)
    st.pyplot(fig1)

    st.subheader("Q2: Top 10 Members by Number of Transactions")
    member_trans = grocery_df['Member_number'].value_counts().head(10)

    fig2, ax2 = plt.subplots()
    ax2.bar(member_trans.index.astype(str), member_trans.values)
    plt.xticks(rotation=90)
    st.pyplot(fig2)

    st.subheader("Q3: Items Purchased by Most Members (Top 10)")
    item_member = grocery_df.groupby('itemDescription')['Member_number'].nunique().sort_values(ascending=False).head(10)

    fig4, ax4 = plt.subplots()
    ax4.bar(item_member.index, item_member.values)
    plt.xticks(rotation=90)
    st.pyplot(fig4)


with tab4:
    st.subheader("🥙 Grocery Dataset Chatbot")

    qa_corpus = [
        ("How many unique members are there?",
         "There are 3068 unique members in the dataset."),

        ("What is the total number of unique items?",
         "There are 166 unique grocery items in the dataset."),

        ("Which item is purchased the most?",
         "You can find the most purchased item using value_counts on the 'Item' column."),

        ("How many transactions are there per day?",
         "You can see daily transactions by grouping the 'Date' column and counting."),

        ("What is the date range of the transactions?",
         "The date range is from the earliest date to the latest date in the 'Date' column.")
    ]

    user_question = st.text_input("Ask something about the dataset:")

    if user_question:
        response = "Sorry, I don't have an answer for that."

        for question, answer in qa_corpus:
            if user_question.lower() in question.lower():
                response = answer
                break

        st.write("🤖", response)

with tab5:
  st.subheader("About This Project")
  st.write("""
    This project is a **Grocery Market Analysis** using transaction data. 
    It includes:
    - Analysis of transactions over time
    - Identifying top items and unique members
    - Visualizations like line charts for daily transactions
    - A chatbot to answer simple questions about the dataset
    """)
  st.subheader("About Me")
  st.write("""
  **Name:** Diksha  
  **Education:** BCA  
  **Skills:** Python, Data Analysis, Streamlit, Pandas  
  **Purpose of this project:** To demonstrate basic data analysis, visualization, and building a simple chatbot for a grocery dataset.
  """)


# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")  # horizontal line
st.markdown("<center>© 2025 Diksha🧡 | Grocery Analysis App</center>", unsafe_allow_html=True)
