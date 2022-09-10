import pandas as pd


def clean_up(a_string):
    return a_string.lower().replace(' ', '_').replace('ª', '')


def load_data():
    data = pd.read_csv('data/Basket.csv', sep=';')
    final_data = data[['fase', 'team_1', 'team_2', 'score_1', 'score_2']].dropna()
    final_data['score_1'] = final_data['score_1'].astype(int)
    final_data['score_2'] = final_data['score_2'].astype(int)
    final_data['fase'] = final_data['fase'].apply(clean_up)
    return final_data


def parse_games(full_data):
    all_games = []
    for index, row in full_data.iterrows():
        team_1 = row['team_1']
        team_2 = row['team_2']
        score_1 = row['score_1']
        score_2 = row['score_2']
        fase = row['fase']
        all_games.append({'fase': fase, team_1: score_1, team_2: score_2})
    return all_games


def get_team_names(full_data):
    """
    Return team's names
    :return: set
    """
    names = set()
    for index, row in full_data.iterrows():
        names.add(row['team_1'])
        names.add(row['team_2'])
    return sorted(names)


if __name__ == "__main__":
    print("Parsing data")
    data = load_data()
    games = parse_games(data)
    print(games)
    teams = get_team_names(data)
    print(teams)
