# H1Z1 King of the Kill Leaderboard Script
This is a script that will fetch all important info about a player from the H1Z1 Kotk leaderboard!

```python
import Stats
import sys

getInfo = Stats.GetRank(sys.argv[1], sys.argv[2])
getInfo.get_all()
```
### Example
```
python example.py eryctriceps 2
```


Use 

```python

getInfo.getRegions()
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
