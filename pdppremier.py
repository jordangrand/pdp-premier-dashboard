import pandas as pd
import streamlit as st

from PIL import Image
import streamlit as st
import pandas as pd

# Load logo image
logo = Image.open("USA_Baseball_team_logo.png")

# Display logo
st.image(logo, width=200)  # Adjust width as needed

# Load CSV
df = pd.read_csv("pdp_premier.csv")

st.title("PDP Premier Players Dashboard")

# Convert "30 Total" to numeric just in case it's read as a string
df["30 Total"] = pd.to_numeric(df["30 Total"], errors="coerce")

# Drop rows with missing key values
df = df.dropna(subset=["NAME", "Location", "Year", "Event", "Event Type", "30 Total"])

# Sidebar Filters
st.sidebar.header("Filter Player Data")

location = st.sidebar.selectbox("Select Location", ["All"] + sorted(df["Location"].unique()))
name = st.sidebar.selectbox("Select Player", ["All"] + sorted(df["NAME"].unique()))
year = st.sidebar.selectbox("Select Year", ["All"] + sorted(df["Year"].unique()))
event = st.sidebar.selectbox("Select Event", ["All"] + sorted(df["Event"].unique()))
event_type = st.sidebar.selectbox("Select Event Type", ["All"] + sorted(df["Event Type"].unique()))

# Slider for 30 Total
min_30 = round(float(df["30 Total"].min()), 2)
max_30 = round(float(df["30 Total"].max()), 2)
avg_30 = round(float(df["30 Total"].mean()), 2)

st.sidebar.markdown(f"**Average 30 Total: {avg_30} sec**")
thirty_total_range = st.sidebar.slider(
    "30 Total Range (sec)",
    min_value=min_30,
    max_value=max_30,
    value=(min_30, max_30),
    step=0.01
)

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

# Apply slider filter
filtered_df = filtered_df[
    (filtered_df["30 Total"] >= thirty_total_range[0]) & 
    (filtered_df["30 Total"] <= thirty_total_range[1])
]

# Show result
st.dataframe(filtered_df)
