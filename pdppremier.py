import pandas as pd
import streamlit as st

# Load CSV
df = pd.read_csv("pdp_premier.csv")

st.title("PDP Premier Dashboard")

# Show available columns (optional for debugging)
st.write("Columns:", df.columns.tolist())

# Dropdown filters using actual columns
event = st.selectbox("Select Event", sorted(df["Event"].dropna().unique()))
position = st.selectbox("Select Position", sorted(df["Position"].dropna().unique()))

# Filtered DataFrame
filtered_df = df[(df["Event"] == event) & (df["Position"] == position)]

st.subheader("Filtered Player Data")
st.dataframe(filtered_df)
