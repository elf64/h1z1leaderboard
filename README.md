# H1Z1 King of the Kill Leaderboard Script
This is a script that will fetch all important info about a player from the H1Z1 Kotk leaderboard!
### Executable Version
```
You can find the .exe file in the dist/v00x folder
The executable files will always be up-to-date
```
### Example for windows
```
./getStatus.exe eryctriceps 2

NOTE:
  [eryctrices] - username
  [2] - Region ID

[Regions IDs]

Region: North America With ID -> 1
Region: Europe With ID -> 2
Region: South America With ID -> 3
Region: Australia With ID -> 5
Region: Asia/Pacific With ID -> 4
```

## Source code example
```python
import Stats
import sys

getInfo = Stats.GetRank(sys.argv[1], sys.argv[2])
getInfo.get_all()
```
### Cmd run Example
```
python example.py eryctriceps 2
```
```
[erytriceps] - username
[2] - Id of region
Ex of ID:
  North America - 1
  Europe - 2
  etc..
```


Use 

```python
getInfo.get_regions()
```

To get the id's for all regions.

## Output

```

User : eryctriceps

In position 1
-----------------
Top 10 Matches!
-----------------
Score:  269,250 > Kills: [ 30] >  Place: [ 1 ]
Score:  267,400 > Kills: [ 30] >  Place: [ 1 ]
Score:  265,600 > Kills: [ 29] >  Place: [ 1 ]
Score:  265,600 > Kills: [ 29] >  Place: [ 1 ]
Score:  264,050 > Kills: [ 28] >  Place: [ 1 ]
Score:  263,750 > Kills: [ 30] >  Place: [ 1 ]
Score:  262,350 > Kills: [ 28] >  Place: [ 1 ]
Score:  261,600 > Kills: [ 28] >  Place: [ 1 ]
Score:  261,400 > Kills: [ 25] >  Place: [ 1 ]
Score:  261,000 > Kills: [ 27] >  Place: [ 1 ]
-----------------

Kills per Match Ratio: 4.13490853658
Wins per Match Ratio: 0.03125
Top10 Per Match Ratio: 0.0480182926829
Top10 Total Score: 2,642,000
Top Kills: 30
Total Matches: 1,312
Total Wins: 41
Total Kills: 5,425

--> RANK: Royalty 1 <--
```
