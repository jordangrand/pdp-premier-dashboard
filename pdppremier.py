import pandas as pd
import streamlit as st

# Load CSV
df = pd.read_csv("pdp_premier.csv")

st.title("PDP Premier Dashboard")

# Drop rows with missing critical fields
df = df.dropna(subset=["NAME", "Location", "Year", "Event", "Event Type"])

# Sidebar Filters
st.sidebar.header("Filter Player Data")

location = st.sidebar.selectbox("Select Location", ["All"] + sorted(df["Location"].unique()))
name = st.sidebar.selectbox("Select Player", ["All"] + sorted(df["NAME"].unique()))
year = st.sidebar.selectbox("Select Year", ["All"] + sorted(df["Year"].unique()))
event = st.sidebar.selectbox("Select Event", ["All"] + sorted(df["Event"].unique()))
event_type = st.sidebar.selectbox("Select Event Type", ["All"] + sorted(df["Event Type"].unique()))

# Apply filters
filtered_df = df.copy()

if location != "All":
    filtered_df = filtered_df[filtered_df["Location"] == location]

if name != "All":
    filtered_df = filtered_df[filtered_df["NAME"] == name]

if year != "All":
    filtered_df = filtered_df[filtered_df["Year"] == year]

if event != "All":
    filtered_df = filtered_df[filtered_df["Event"] == event]

if event_type != "All":
    filtered_df = filtered_df[filtered_df["Event Type"] == event_type]

# Show result
st.subheader("Filtered Results")
st.dataframe(filtered_df)
