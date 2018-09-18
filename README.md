# About

This is a collection of code to get the top time trial scores of the game Skidstorm. To run the code, please follow tutorial below. You need to have `Python 2.7` installed.

### Collecting the data

`json_collect_data.py` - Fetches all the data from the Skidstorm site per car per map

To run:
```
python json_collect_data
```
All output is in `json_data` directory. This needs to be executing before any other command.

### Analyzing the data

`data_analyse.py` - Calculates average and standard deviation of score per car per map
To run:
```
python data_analyse
```

All output is in `aggregated_data` directory which contains only the average of all cars in each map. The average and standard deviation is in `json_stat` directory. 

### Finding score of top k players

`calc_top_k.py` - Prints the top k players in each car in each map.

To run:
```
python calc_top_k 50
```
This finds the top 50 players of each car and each map. The ouput directory is `json_stat_topk`

### Finding ideal car groups

This code is a bit buggy as of now. The supplied list needs to be transposed before being fed to the clustering algorithm. Will update later.
