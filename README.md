# basket
This app was designed to calculate simple statistic in basketball tournaments. The statistic include all teams ranking based on: total points for the season per team, mean points, maximum and minimum point, number of games played and win percentage. 
```
Maia Basket - total points:  1142, mean points:  63.44, maximum point:   99, minimum point:  30, games played: 18, wins:  17 ( 94.44%)

```

## usage
To use the program with the original dataset:
```
(venv) ➜  basket git:(main) python basket_app.py                                
Starting
Initializing data
Calculate the ranking

Season 2021-2022 ... 
```
If you want to apply the program to another datafile:

```
(venv) ➜  basket git:(main) ✗ python basket_app.py -f data/basket_2.csv           
Starting
Initializing data
Calculate the ranking

Season 2021-2022 
```


## test
There are tests for all the function present in the `basket_app.py` and `parse_data.py` files. 

To run the tests from the command line:
```
cd tests
pytest
```

## data
The data is stored in a csv file called basket.csv. It contains all the games played in an under 14 basketball tournament for the season 2021-2022.  The columns represent the fase of the tournament, the date of the match, the two teams and their score.  

The file name should follow this format: `basket_2021-2022.csv`, in this way the season is assigned from the file name.

