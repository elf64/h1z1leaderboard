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

In position 13678
-----------------
Top 10 Matches!
-----------------
Score:  214500 , Kills: [ 2 ],  Place: [ 1 ]
Score:  210000 , Kills: [ 1 ],  Place: [ 1 ]
Score:  184053 , Kills: [ 4 ],  Place: [ 2 ]
Score:  176903 , Kills: [ 1 ],  Place: [ 2 ]
Score:  176903 , Kills: [ 1 ],  Place: [ 2 ]
Score:  172403 , Kills: [ 0 ],  Place: [ 2 ]
Score:  172403 , Kills: [ 0 ],  Place: [ 2 ]
Score:  156259 , Kills: [ 0 ],  Place: [ 3 ]
Score:  156259 , Kills: [ 0 ],  Place: [ 3 ]
Score:  148105 , Kills: [ 1 ],  Place: [ 4 ]
-----------------

Kills per Match Ratio: 0.5733333333333
Wins per Match Ratio: 0.02666666666667
Top10 Per Match Ratio: 0.2933333333333
Top10 Total Score: 1767788
Top Kills: 4
Total Matches: 75
Total Wins: 2
Total Kills: 43

--> RANK: Platinum 2 <--
```
