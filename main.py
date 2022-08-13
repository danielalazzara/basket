TEST_DATA = {
    "abc": [1, 2, 3],
    "def": [4, 5, 6, 7],
    "ghi": [56, 89, "rt"],
    "jkl": [8, 9, 1],
    "mno": [2],
    "pqr": [],
    "stu": [3, 4, 5],
}


def sum_score_games(points):
    if not isinstance(points, list):
        return "It's not a list!"
    score = []
    if len(points) <= 0:
        return 0
    for i in points:
        try:
            _i = int(i)
        except ValueError:
            _i = 0
    score.append(_i)
    return sum(score)


if __name__ == "__main__":
    print("Starting")
    for k, v in TEST_DATA.items():
        _score = sum_score_games(v) if isinstance(sum_score_games(v), int) else 0
        print(f"Squadra: {k} totale: {_score}")