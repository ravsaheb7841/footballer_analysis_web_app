import streamlit as st
from data_processing import load_data
data = load_data()

# Functions for Analysis
def player_wise(player):
    if player == 'Overall':
        temp_df = data.drop(columns=['Confederation', 'Goals per match', 'Career span', 'Date of 50th goal'])
    else:
        temp_df = data[data['Player'] == player].drop(columns=['Player', 'Confederation', 'Goals per match', 'Career span', 'Date of 50th goal'])
    return temp_df

data = data[data["Confederation"] != False]
def confederation_wise(confederation):
    if confederation == 'Overall':
        return data.groupby('Confederation')['Goals'].sum().sort_values(ascending=False)
    else:
        temp_df = data[data['Confederation'] == confederation].drop(columns=['Confederation', 'Career span', 'Date of 50th goal'])
        total_goals = temp_df['Goals'].sum()
        st.write(f"Total Goals for {confederation}: {total_goals}")
        return temp_df.sort_values(by='Rank', ascending=True)

def career_summary(player_name):
    player_data = data[data['Player'] == player_name]
    if player_data.empty:
        return {"message": f"No data found for player: {player_name}"}
    span = player_data.iloc[0]['Career span']
    total_goals = player_data['Goals'].sum()
    total_caps = player_data['Caps'].sum()
    career_length = "Still Playing" if '-' in str(span) and span.split('-')[1] == '' else int(span.split('-')[1]) - int(span.split('-')[0])
    return {"Player": player_name, "Total Goals": total_goals, "Total Caps": total_caps, "Career Span": career_length}

def fastest_50_goals(player_name):
    if player_name == 'Overall':
        return data.sort_values(by='Date of 50th goal')[['Player', 'Date of 50th goal', 'Goals']]
    else:
        temp_df = data[data['Player'] == player_name]
        if temp_df.empty:
            return f"No data found for player: {player_name}"
        return f"{player_name} reached 50 goals on: {temp_df.iloc[0]['Date of 50th goal']}"
