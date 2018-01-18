import json
from pprint import pprint

data = json.load(open('pbp_cincinnati.json'))


def IdentifyPlayFlorida(play):
    """Take in play, identify which kind of play it is to increment proper stats."""
    if ("misses" in play) and ("two" in play):
        print("Florida two point miss")
        # matchupsList[-1].floridaLineupStats[1]++
        return
    elif ("misses" in play) and ("three" in play):
        print("Florida three point miss")
        # matchupsList[-1].floridaLineupStats[5]++
        return
    elif ("misses" in play) and ("free" in play):
        print("Florida free point miss")
        # matchupsList[-1].floridaLineupStats[7]++
        return
    elif ("misses" in play) and (("layup" in play) or
                                 ("hook" in play) or ("dunk" in play)):
        print("Florida paint miss")
        # matchupsList[-1].floridaLineupStats[3]++
        return
    elif ("makes" in play) and ("two" in play):
        print("Florida two point make")
        # matchupsList[-1].floridaLineupStats[1]++
        # matchupsList[-1].floridaLineupStats[0]++
        return
    elif ("makes" in play) and ("three" in play):
        print("Florida three point make")
        # matchupsList[-1].floridaLineupStats[5]++
        # matchupsList[-1].floridaLineupStats[4]++
        return
    elif ("makes" in play) and ("free" in play):
        print("Florida free point make")
        # matchupsList[-1].floridaLineupStats[7]++
        # matchupsList[-1].floridaLineupStats[6]++
        return
    elif ("makes" in play) and (("layup" in play) or
                                ("hook" in play) or ("dunk" in play)):
        print("Florida paint make")
        # matchupsList[-1].floridaLineupStats[3]++
        # matchupsList[-1].floridaLineupStats[2]++
        return
    elif ("foul" in play):
        print("Florida foul")
        # matchupsList[-1].floridaLineupStats[17]++
        return
    elif ("defensive" in play):
        print("Florida defensive rebound")
        # matchupsList[-1].floridaLineupStats[10]++
        return
    elif ("offensive" in play):
        print("Florida offensive rebound")
        # matchupsList[-1].floridaLineupStats[9]++
        return
    elif ("turnover" in play):
        print("Florida turnover")
        # matchupsList[-1].floridaLineupStats[8]++
        return


def IdentifyPlayOpponent(play):
    """Take in play, identify which kind of play it is to increment proper stats."""
    if ("misses" in play) and ("two" in play):
        print("Opponent two point miss")
        # matchupsList[-1].opponentLineupStats[1]++
        return
    elif ("misses" in play) and ("three" in play):
        print("Opponent three point miss")
        # matchupsList[-1].opponentLineupStats[5]++
        return
    elif ("misses" in play) and ("free" in play):
        print("Opponent free point miss")
        # matchupsList[-1].opponentLineupStats[7]++
        return
    elif ("misses" in play) and (("layup" in play) or
                                 ("hook" in play) or ("dunk" in play)):
        print("Opponent paint miss")
        # matchupsList[-1].opponentLineupStats[3]++
        return
    elif ("makes" in play) and ("two" in play):
        print("Opponent two point make")
        # matchupsList[-1].opponentLineupStats[1]++
        # matchupsList[-1].opponentLineupStats[0]++
        return
    elif ("makes" in play) and ("three" in play):
        print("Opponent three point make")
        # matchupsList[-1].opponentLineupStats[5]++
        # matchupsList[-1].opponentLineupStats[4]++
        return
    elif ("makes" in play) and ("free" in play):
        print("Opponent free point make")
        # matchupsList[-1].opponentLineupStats[7]++
        # matchupsList[-1].opponentLineupStats[6]++
        return
    elif ("makes" in play) and (("layup" in play) or
                                ("hook" in play) or ("dunk" in play)):
        print("Opponent paint make")
        # matchupsList[-1].opponentLineupStats[3]++
        # matchupsList[-1].opponentLineupStats[2]++
        return
    elif ("foul" in play):
        print("Opponent foul")
        # matchupsList[-1].opponentLineupStats[17]++
        return
    elif ("defensive" in play):
        print("Opponent defensive rebound")
        # matchupsList[-1].opponentLineupStats[10]++
        return
    elif ("offensive" in play):
        print("Opponent offensive rebound")
        # matchupsList[-1].opponentLineupStats[9]++
        return
    elif ("turnover" in play):
        print("Opponent turnover")
        # matchupsList[-1].opponentLineupStats[8]++
        return

for i in range(0, 100):
    if (data['periods'][0]['playStats'][i]['homeText']):
        IdentifyPlayFlorida((data['periods'][0]['playStats'][i]['homeText']))
    else:
        IdentifyPlayOpponent((data['periods'][0]['playStats'][i]['visitorText']))

# team1stats[0]=2PFGM [1]=2PFGA  [2]=PFGM [3]=PFGA  [4]=3PFGM [5]=3PFGA
# [6]=FTM [7]=FTA  [8]=TO [9]=ORB [10]=DRB  [11]=Initial Time  [12]=Final time
# [13]=Total Time [14]=Initial Points [15]=Final Points [16]=Total Points
# [17] PF
