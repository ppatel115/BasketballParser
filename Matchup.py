# Parser intializes a lineup every Substitution call, stores matchup stats in Matchup
class Matchup(object):
    team1 = ""
    t1lineup = 1000                 # set these to 1000 for errorchecking because probably gonna use 0-20 for lineup numberws
    team2 = ""
    t2lineup = 1000

    #TODO: Add two lists with stats for each team's current matchup lineup like team1stats [FGM, FGA, 3PM, 3PA, etc.]

    def __init__(self, team1, t1lineup, team2, t2lineup):
        self.team1 = team1
        self.t1lineup = t1lineup
        self.team2 = team2
        self.t2lineup = t2lineup

def make_matchup(team1, t1lineup, team2, t2lineup):
    matchup = Matchup(team1, t1lineup, team2, t2lineup)
    return student
