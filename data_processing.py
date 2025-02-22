import pandas as pd

def load_data():
    data = pd.read_excel("dataset.xlsx")
    data = pd.DataFrame(data)
    data = data.drop(columns=['Nation'], errors='ignore')

    confed_map = {
        'UEFA': 'Union of European Football Associations',
        'AFC': 'Asian Football Confederation',
        'CAF': 'Confederation of African Football'
    }
    data['Confederation'] = data['Confederation'].replace(confed_map)
    data['Player'] = data['Player'].astype(str).str.strip()
    data = data[(data['Player'] != "False") & (data['Player'] != False)]

    data['Date of 50th goal'] = pd.to_datetime(data['Date of 50th goal'], errors='coerce').dt.date
    return data
