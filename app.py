import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.markdown(
    f"""
    <style>
        .stApp {{
            background: url("") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Custom CSS for Styling with Background Image
st.markdown(f'''
    <style>
        body {{
            background: url("") no-repeat center center fixed;
            background-size: cover;
            font-family: 'Arial', sans-serif;
        }}
        .main {{
            background-color: black;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0);
        }}
        .sidebar .sidebar-content {{
            background-color: #000000;
            color: white;
        }}
        h1, h2, h3 {{
            color: black !important;
        }}
    </style>
''', unsafe_allow_html=True)

# Introduction Page
st.title("🎮 Game Sales Analysis Dashboard")
st.markdown("""
    Welcome to the Game Sales Analysis Dashboard! This interactive platform provides insights into game sales 
    across different platforms, genres, and more. Data updates in real time.
""")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("vgchartz-2024.csv")

def update_data():
    time.sleep(5)  # Simulate real-time updates
    return load_data()

df_placeholder = st.empty()
df = update_data()

df_placeholder.write(df.head())

# Sidebar
st.sidebar.title("🎮 Game Sales Analysis")
st.sidebar.markdown("Select an analysis type below:")
option = st.sidebar.selectbox("Select Analysis", ["Dataset Overview", "Top Selling Games", "Sales by Platform", "Genre Analysis", "Image Viewer"])

st.markdown("<div class='main'>", unsafe_allow_html=True)

# Dataset Overview
if option == "Dataset Overview":
    st.title("📊 Dataset Overview")
    st.write(df.head())
    st.write("**Shape of dataset:**", df.shape)
    st.write("**Missing values:**")
    st.write(df.isna().sum())

# Top Selling Games Visualization
elif option == "Top Selling Games":
    st.title("🏆 Top 10 Best-Selling Games")
    top_selling_games = df.groupby('title', as_index=False)['total_sales'].sum().nlargest(10, 'total_sales')
    fig = px.bar(top_selling_games, x='title', y='total_sales', title="Top 10 Best-Selling Games", color='total_sales',
                 labels={'title': 'Game Title', 'total_sales': 'Total Sales (in millions)'}, template="plotly_dark")
    st.plotly_chart(fig)

# Sales by Platform
elif option == "Sales by Platform":
    st.title("🎮 Top Selling Games by Platform")
    platform_sales = df.groupby(['console'])['total_sales'].sum().reset_index()
    fig = px.bar(platform_sales, x='console', y='total_sales', title="Sales Distribution by Platform",
                 color='total_sales', labels={'console': 'Platform', 'total_sales': 'Total Sales (in millions)'},
                 template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# Genre Analysis
elif option == "Genre Analysis":
    st.title("📌 Genre-Based Analysis")
    genre_sales = df.groupby('genre')['total_sales'].sum().reset_index()
    fig = px.bar(genre_sales, x='genre', y='total_sales', title="Total Sales by Genre", color='total_sales',
                 labels={'genre': 'Genre', 'total_sales': 'Total Sales (in millions)'}, template="plotly_dark")
    st.plotly_chart(fig)

# Image Viewer Section
elif option == "Image Viewer":
    st.title("🖼️ Uploaded Images Viewer")
    image_files = ["1q.png", 
                   "2q.png", 
                   "3q.png", 
                   "4q.png", 
                   "5q.png",
                   "6q.png"]
    for img in image_files:
        st.image(img, use_column_width=True)

st.markdown("</div>", unsafe_allow_html=True)
