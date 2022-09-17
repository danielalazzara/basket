import pytest
import basket_app
from collections import Counter

TEST_TEAM_SCORES = {
    "abc": [1, 2, 3],
    "def": [4, 5, 6, 7],
    "ghi": [56, 89, "rt"],
    "jkl": [8, 9, 1],
    "mno": [2],
    "pqr": [],
    "stu": [3, 4, 5],
}

TEST_TEAM_SCORES_RESULTS = [(6, 2.0, 3, 1),
                            (22, 5.5, 7, 4),
                            (145, 48.333333333333336, 89, 0),
                            (18, 6.0, 9, 1),
                            (2, 2.0, 2, 2),
                            (0,),
                            (12, 4.0, 5, 3)]

TEST_TOURNAMENT_SCORE = {
    "abc": 42,
    "def": 18,
    "ghi": 147,
}

TEST_SINGLE_MATCH = {
    "abc": 45,
    "def": 78,
}

TEST_GAMES = [{'fase': '1_fase', 'abc': 72, 'def': 35},
            {'fase': '1_fase', 'ghi': 68, 'abc': 54}]


def test_generate_games_stat():
    results = []
    for k, v in TEST_TEAM_SCORES.items():
        results.append(basket_app.generate_games_stat(v))
    assert results == TEST_TEAM_SCORES_RESULTS


def test_tournament_points():
    t1 = list(TEST_SINGLE_MATCH.keys())[0]
    t2 = list(TEST_SINGLE_MATCH.keys())[1]
    t1_points = list(TEST_SINGLE_MATCH.values())[0]
    t2_points = list(TEST_SINGLE_MATCH.values())[1]
    result = basket_app.tournament_points(t1, t2, t1_points, t2_points)
    assert result == ('def', 1, 'abc', 2)


def test_ranking():
    result = basket_app.ranking(TEST_GAMES)
    assert result == {'1_fase': Counter({'abc': 3, 'ghi': 2, 'def': 1})}


def test_teams_stat():
    result = basket_app.teams_stat('abc', TEST_GAMES)
    assert result == ((126, 63.0, 72, 54), 2, 1, 0.5)


