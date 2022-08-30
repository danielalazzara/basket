import pandas as pd


def load_data():
    data = pd.read_csv('data/Basket.csv', sep=';')
    final_data = data[['team_1', 'team_2', 'score_1', 'score_2']].dropna()
    final_data['score_1'] = final_data['score_1'].astype(int)
    final_data['score_2'] = final_data['score_2'].astype(int)
    return final_data


def parse_games(full_data):
    games = []
    for index, row in full_data.iterrows():
        team_1 = row['team_1']
        team_2 = row['team_2']
        score_1 = row['score_1']
        score_2 = row['score_2']
        games.append({team_1: score_1, team_2: score_2})
    return games


if __name__ == "__main__":
    print("Parsing data")
    data = load_data()
    games = parse_games(data)
    print(games)
