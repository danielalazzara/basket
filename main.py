TEST_DATA = {
    "abc": [1, 2, 3],
    "def": [4, 5, 6, 7],
    "ghi": [56, 89, "rt"],
    "jkl": [8, 9, 1],
    "mno": [2],
    "pqr": [],
    "stu": [3, 4, 5],
}


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


if __name__ == "__main__":
    print("Starting")
    for k, v in TEST_DATA.items():
        _stat = generate_games_stat(v)
        _output = " / ".join(str(i) for i in _stat)
        print(f"Team: {k} sum/mean/max/min: {_output}")
