import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/metadata.csv", low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df = df.dropna(subset=['title', 'year'])

# Title
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Year filter
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample
st.subheader("Sample of the Data")
st.write(filtered_df.head())

# Publications per year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
st.subheader("Top 10 Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)
