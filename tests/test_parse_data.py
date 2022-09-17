import pytest
import parse_data

MOCK_DATA_FILENAME = 'mock_data/mock_basket.csv'

LOAD_DATA_RESULT = """             fase            team_1         team_2  score_1  score_2
0  1_fase_grupo_a     CD José Regio  Juvemaia ACDC       72       35
1  1_fase_grupo_a        Guifões SC        FC Gaia       68       54
3  1_fase_grupo_b          FC Porto   Club 5Basket       31       71
4  1_fase_grupo_b  FidesGondobasket     CLIP Teams       24       73"""


PARSE_GAMES_RESULT = [{'fase': '1_fase_grupo_a', 'CD José Regio': 72, 'Juvemaia ACDC': 35}, {'fase': '1_fase_grupo_a', 'Guifões SC': 68, 'FC Gaia': 54}, {'fase': '1_fase_grupo_b', 'FC Porto': 31, 'Club 5Basket': 71}, {'fase': '1_fase_grupo_b', 'FidesGondobasket': 24, 'CLIP Teams': 73}]

GET_TEAMS_NAMES_RESULT = ['CD José Regio', 'CLIP Teams', 'Club 5Basket', 'FC Gaia', 'FC Porto', 'FidesGondobasket', 'Guifões SC', 'Juvemaia ACDC']


def test_load_data():
    result = repr(parse_data.load_data(MOCK_DATA_FILENAME, ';'))
    assert result == LOAD_DATA_RESULT


def test_parse_games():
    data = parse_data.load_data(MOCK_DATA_FILENAME, ';')
    result = parse_data.parse_games(data)
    assert result == PARSE_GAMES_RESULT


def test_get_team_names():
    data = parse_data.load_data(MOCK_DATA_FILENAME, ';')
    result = parse_data.get_team_names(data)
    assert result == GET_TEAMS_NAMES_RESULT
