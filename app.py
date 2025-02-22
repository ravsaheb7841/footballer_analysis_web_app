import streamlit as st
from data_processing import load_data
from analysis import player_wise, confederation_wise, career_summary, fastest_50_goals

st.set_page_config(page_title="Footballers Data Analysis", layout="wide")

# Load Data
data = load_data()

# Remove rows where 'Player' or 'Confederation' are False
data = data[data['Player'] != False]
data = data[data['Confederation'] != False]

# Sidebar Configuration
st.sidebar.image("https://pngimg.com/uploads/fifa/fifa_PNG11.png", width=150)
st.sidebar.title("⚽ Footballers Analysis")
st.sidebar.header("Select Analysis")
analysis_type = st.sidebar.radio("", ["Player Analysis", "Confederation Analysis", "Career Summary", "Fastest 50 Goals"])

# Main Title with Larger Font Size
st.markdown("<h1 style='text-align: center; font-size: 48px;'>Footballers Data Analysis</h1>", unsafe_allow_html=True)
st.markdown("---")

if analysis_type == "Player Analysis":
    st.subheader("🔍 Player Analysis")
    player_name = st.selectbox("Select Player", ['Overall'] + list(data['Player'].unique()))
    st.success(f"Showing stats for : { player_name}")  # Highlight Selected Player
    st.dataframe(player_wise(player_name), use_container_width=True)

elif analysis_type == "Confederation Analysis":
    st.subheader("🌍 Confederation Analysis")
    conf = st.selectbox("Select Confederation", ['Overall'] + list(data['Confederation'].unique()))
    st.success(f"Showing stats for : { conf}")
    st.dataframe(confederation_wise(conf), use_container_width=True)

elif analysis_type == "Career Summary":
    st.subheader("🏆 Career Summary")
    player_name = st.selectbox("Select Player", data['Player'].unique())
    summary = career_summary(player_name)
    st.success(f"Showing stats for : { player_name}")
    st.write(f"**Player:** {summary['Player']}")
    st.write(f"**Total Goals:** {summary['Total Goals']}")
    st.write(f"**Total Caps:** {summary['Total Caps']}")
    st.write(f"**Career Span:** {summary['Career Span']}")

elif analysis_type == "Fastest 50 Goals":
    st.subheader("⚡ Fastest 50 Goals")
    player_name = st.selectbox("Select Player", ['Overall'] + list(data['Player'].unique()))
    st.success(f"Showing stats for : { player_name}")
    st.write(fastest_50_goals(player_name))

# Footer with Padding
st.markdown("---")
st.markdown("<p style='font-size:12px; color:gray;'>Note: The dataset spans from 1972 to 2024, so consider career start and end years for accurate analysis.</p>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 16px; padding: 10px;'>⚽ Developed by Football Data Analytics Team (RB) </p>", unsafe_allow_html=True)
