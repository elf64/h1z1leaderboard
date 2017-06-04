# H1Z1 King of the Kill Leaderboard Script
This is a script that will fetch all important info about a player from the H1Z1 Kotk leaderboard!

```python
from h1z1Leader import GetRank

getInfo = GetRank('Farambe', '2') # <-- the '2' Stands for the Region you want to search for
getInfo.GetAll()
```

Use 

```python

getInfo.getRegions()
```

To get the id's for all regions.

## Output

```
User : Farambe

In position 13,698
-----------------
Top 10 Matches!
-----------------
Score:  214,500 > Kills: [ 2 ] >  Place: [ 1 ]
Score:  210,000 > Kills: [ 1 ] >  Place: [ 1 ]
Score:  184,053 > Kills: [ 4 ] >  Place: [ 2 ]
Score:  176,903 > Kills: [ 1 ] >  Place: [ 2 ]
Score:  176,903 > Kills: [ 1 ] >  Place: [ 2 ]
Score:  172,403 > Kills: [ 0 ] >  Place: [ 2 ]
Score:  172,403 > Kills: [ 0 ] >  Place: [ 2 ]
Score:  156,259 > Kills: [ 0 ] >  Place: [ 3 ]
Score:  156,259 > Kills: [ 0 ] >  Place: [ 3 ]
Score:  148,105 > Kills: [ 1 ] >  Place: [ 4 ]
-----------------

Kills per Match Ratio: 0.573333333333
Wins per Match Ratio: 0.0266666666667
Top10 Per Match Ratio: 0.293333333333
Top10 Total Score: 1,767,788
Top Kills: 4
Total Matches: 75
Total Wins: 2
Total Kills: 43

--> RANK: Platinum 2 <--
```
