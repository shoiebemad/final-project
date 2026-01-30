import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Instacart Orders Analysis")


@st.cache_data
def load_data():
    df = pd.read_csv("final_dataset.csv")  
    return df

df = load_data()
# univariate analysis
st.subheader("Sample of the Dataset")
st.dataframe(df.head())

st.subheader("Univariate Analysis")
column = st.selectbox(
    "Choose a column:",
    ['products_per_order', 'user_reorder_rate', 'is_it_morning', 'is_it_weekend']
)


fig, ax = plt.subplots()
sns.histplot(df[column], bins=30, kde=True, ax=ax)
ax.set_title(f"Distribution of {column}")
st.pyplot(fig)

st.subheader("Bivariate Analysis")

x_col = st.selectbox("Choose X (categorical)", ['is_it_weekend', 'is_it_morning', 'products_per_order'])
y_col = st.selectbox("Choose Y (numerical)", ['user_reorder_rate'])

fig2, ax2 = plt.subplots()
sns.boxplot(x=x_col, y=y_col, data=df, ax=ax2)
ax2.set_title(f"{x_col} vs {y_col}")
st.pyplot(fig2)


