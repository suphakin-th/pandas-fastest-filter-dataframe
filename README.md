# pandas-fastest-filter-dataframe

Use pandas for query and filter data and made answer for fastest that i can.

# Function loop_solve

| Index         |      age      |   time_in_bed   |   pct_sleeping   |   favourite_food   |    hate_food    |     reward      |
|---------------|:-------------:|:---------------:|:----------------:|:------------------:|:---------------:|:---------------:|
| 0             |      108      |        4        |     0.912562     |      antelope      |     bagels      |    antelope     |
| 1             |      106      |        8        |     0.029709     |    baked beans     |  Avocado roll   |   baked beans   |
| 2             |      32       |        8        |     0.504870     |      ahi tuna      |       BBQ       |    ahi tuna     |
| 3             |      24       |       11        |     0.237198     |    Avocado roll    |   Apple juice   |   Apple juice   |
| 4             |      108      |        9        |     0.512351     |    Avocado roll    |     almond      |  Avocado roll   |
| ...           |      ...      |       ...       |       ...        |        ...         |       ...       |       ...       |
| 99995         |      29       |        8        |     0.985923     |      antelope      |      bacon      |    antelope     |
| 99996         |      66       |       11        |     0.488156     |   albacore tuna    |    antelope     |    antelope     |
| 99997         |      88       |        5        |     0.385050     |     applesauce     |      bacon      |      bacon      |
| 99998         |      79       |        4        |     0.795359     |      egg-fire      |   black beans   |   black beans   |
| 99999         |      25       |        7        |     0.286298     |    Avocado roll    |      bacon      |      bacon      |

## [100000 rows x 6 columns]: 
### loop_time Took :  9.319525241851807 sec
### apply_time Took :  0.7549371719360352 sec
### vectorized_time Took :  0.010896444320678711 sec

![alt text](https://github.com/suphakin-th/pandas-fastest-filter-dataframe/blob/main/result.png?raw=true)
