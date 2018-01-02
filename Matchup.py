# Parser intializes a lineup every Substitution call, stores matchup stats in Matchup
class Matchup(object):
    team1 = ""
    t1lineup = 1000                 # set these to 1000 for errorchecking because probably gonna use 0-20 for lineup numberws
    team2 = ""
    t2lineup = 1000

    #TODO: Add two lists with stats for each team's current matchup lineup like team1stats [FGM, FGA, 3PM, 3PA, etc.]
team1stats = [0,0,0,0,0,0,0,0,0,0,0]
team2stats = [0,0,0,0,0,0,0,0,0,0,0]
#team1stats[0]=2PFGM [1]=2PFGA  [2]=PFGM [3]=PFGA  [4]=3PFGM [5]=3PFGA  [6]=FTM [7]=FTA  [8]=TO [9]=ORB [10]=DRB
#how to track minutes?
    

    def __init__(self, team1, t1lineup, team2, t2lineup):
        self.team1 = team1
        self.t1lineup = t1lineup
        self.team2 = team2
        self.t2lineup = t2lineup

def make_matchup(team1, t1lineup, team2, t2lineup):
    matchup = Matchup(team1, t1lineup, team2, t2lineup)
    return student
