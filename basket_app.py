import parse_data


def generate_games_stat(points):
    """
    Verify data and generate useful stat.
    :param points: list
    :return: tuple
    (sum, mean, max, min)
    """
    if not isinstance(points, list):
        return "It's not a list!"
    score = []
    if len(points) <= 0:
        return 0,
    for i in points:
        try:
            _i = int(i)
        except ValueError:
            _i = 0
        score.append(_i)
    _sum = sum(score)
    _mean = _sum / len(score)
    _max = max(score)
    _min = min(score)
    return _sum, _mean, _max, _min


def tournament_points(team_1, team_2, t_1_score, t_2_score):
    """
    Evaluate a match and return the winning team and their points.
    :param team_1: string
    :param team_2: string
    :param t_1_score: int
    :param t_2_score: int
    :return: tuple
    """

    if t_1_score > t_2_score:
        winning_team = team_1
        team1_points = 2
        team2_points = 1
    else:
        winning_team = team_2
        team1_points = 1
        team2_points = 2

    return winning_team, team1_points, team2_points


if __name__ == "__main__":
    print("Starting")
    print("Initializing data")
    data = parse_data.load_data()
    games = parse_data.parse_games(data)
    # print(games)
    for game in games:
        _ts_1, _ts_2 = game.items()
        _team_1, _score_1 = _ts_1
        _team_2, _score_2 = _ts_2
        _ = tournament_points(_team_1, _team_2, _score_1, _score_2)
        print(_)
