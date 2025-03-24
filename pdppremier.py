import pandas as pd
import streamlit as st

# Load your CSV
df = pd.read_csv("pdp_premier.csv")

st.title("PDP Premier Dashboard")

# Filters
team = st.selectbox("Select Team", sorted(df["team"].dropna().unique()))
position = st.selectbox("Select Position", sorted(df["primary_position"].dropna().unique()))

# Filtered Table
filtered_df = df[(df["team"] == team) & (df["primary_position"] == position)]

st.subheader("Filtered Player Data")
st.dataframe(filtered_df)
