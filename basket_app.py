import parse_data
from collections import defaultdict, Counter


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
        loser_team = team_2
        team1_points = 2
        team2_points = 1
    else:
        winning_team = team_2
        loser_team = team_1
        team1_points = 1
        team2_points = 2

    return winning_team, team1_points, loser_team, team2_points


def ranking(games):
    """
    Analyze game in games and create a ranking.
    :param games: list
    :return: dict
    """

    groups = defaultdict(Counter)

    for game in games:
        _fase, _ts_1, _ts_2 = game.items()
        _team_1, _score_1 = _ts_1
        _team_2, _score_2 = _ts_2
        _tournament_points = tournament_points(_team_1, _team_2, _score_1, _score_2)
        groups[_fase[1]].update({_tournament_points[0]: _tournament_points[1], _tournament_points[2]: _tournament_points[3]})
    return groups


def teams_stat(team, games):
    """
    Summary statistics for team across all games.
    :param team: string
    :param games: list
    :return: tuple
    (sum, mean, max, min)
    """
    result = []
    for game in games:
        if team in game.keys():
            result.append(game.get(team))
    stats = generate_games_stat(result)
    return stats


if __name__ == "__main__":
    print("Starting")
    print("Initializing data")
    data = parse_data.load_data()
    print("Calculate the ranking")
    games = parse_data.parse_games(data)
    all_results = ranking(games)
    # print(all_results)
    final_four = all_results['final_abp'].keys()
    # print(final_four)
    print()
    print('Final Four Ranking')
    for team in final_four:
        _sum, _mean, _max, _min = teams_stat(team, games)
        print(f"{team:>13} - total points: {_sum:>5}, mean points: {_mean:6.2f}, maximum point: {_max:>4}, minimum point: {_min:>3}")
    print()
    print('All Teams Ranking')
    teams = parse_data.get_team_names(data)
    for team in teams:
        _sum, _mean, _max, _min = teams_stat(team, games)
        print(f"{team:>16} - total points: {_sum:>5}, mean points: {_mean:6.2f}, maximum point: {_max:>4}, minimum point: {_min:>3}")
