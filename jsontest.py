#!python3
import json
from Matchup import Matchup

HOME = True
data = json.load(open('pbp_cincinnati.json'))

florida_bigs = ["Kevarrius Hayes", "Gorjok Gak", "John Egbunu",
                "Isaiah Stokes"]
opp_bigs = ["Gary Clark", "Kyle Washington", "Nysier Brooks", "Eliel Nsoseme"]
florida_starters = ("Keith Stone, Egor Koulechov, Chris Chiozza, Jalen Hudson, Kevaughn Allen")
opp_starters = ("Kyle Washington, Gary Clark, Justin Jenifer, Jacob Evans, Jarron Cumberland")
floridaLineups = []
opponentLineups = []
matchupsList = []
currentFloridaLineup = ""
currentOpponentLineup = ""


def ConvertTimeToSeconds(time):
    """Take in game time, convert to seconds."""
    splittime = time.split(":")
    minutes = int(splittime[0])
    seconds = int(splittime[1])
    timetotal = 60*minutes + seconds
    return timetotal


def CheckFloridaBigs(lineup):
    """Count and return number of bigs in current Florida Lineup."""
    bigs = 0
    for name in florida_bigs:
        if name in lineup:
            bigs += 1
    return bigs


def CheckOpponentBigs(lineup):
    """Count and return number of bigs in current Opponent Lineup."""
    bigs = 0
    for name in opp_bigs:
        if name in lineup:
            bigs += 1
    return bigs


def CreateStarterMatchup(floridaLineupNumber, opponentLineupNumber, time,
                  floridaScore, opponentScore):
    """Create matchup between lineups, check num of bigs."""
    global matchupsList
    # Fix counting bigs for starters
    floridaBigs = 0
    opponentBigs = 0
    matchup = Matchup(floridaLineupNumber, floridaBigs,
                      opponentLineupNumber, opponentBigs, time, floridaScore,
                      opponentScore)
    matchupsList.append(matchup)
    return 0


def CreateFloridaStartingLineup(lineup, time, floridaScore, opponentScore):
    """Take in new lineup, append lineup, call CreateMatchup."""
    global currentFloridaLineup
    global floridaLineups
    currentFloridaLineup = lineup
    floridaLineups.append(lineup)
    floridaLineupNum = floridaLineups.index(lineup)
    opponentLineupNum = 0
    CreateStarterMatchup(floridaLineupNum, opponentLineupNum, time, floridaScore, opponentScore)
    return 0


def CreateOpponentStartingLineup(lineup, time, floridaScore, opponentScore):
    """Take in new lineup, append lineup, call CreateMatchup."""
    global currentOpponentLineup
    global opponentLinups
    currentOpponentLineup = lineup
    opponentLineups.append(lineup)
    opponentLineupNum = opponentLineups.index(lineup)
    floridaLineupNum = 0
    CreateStarterMatchup(floridaLineupNum, opponentLineupNum, time, floridaScore, opponentScore)
    return 0


def CreateMatchup(floridaLineupNumber, opponentLineupNumber, time,
                  floridaScore, opponentScore):                                                      #TODO: turn time to int, seperate scores and turn to ints, fix starter matchup
    """Create matchup between lineups, check num of bigs."""
    global matchupsList
    floridaBigs = CheckFloridaBigs(floridaLineups[floridaLineupNumber])
    opponentBigs = CheckOpponentBigs(opponentLineups[opponentLineupNumber])
    matchup = Matchup(floridaLineupNumber, floridaBigs,
                      opponentLineupNumber, opponentBigs, time, floridaScore,
                      opponentScore)
    matchupsList[-1].floridaEndScore = floridaScore
    matchupsList[-1].opponentEndScore = opponentScore
    matchupsList[-1].finishTime = time
    matchupsList.append(matchup)
    return 0


def CreateFloridaLineup(lineup, time, floridaScore, opponentScore):
    """Take in new lineup, append lineup, call CreateMatchup."""
    global currentFloridaLineup
    global floridaLineups
    currentFloridaLineup = lineup
    if (lineup in floridaLineups):
        floridaLineupNum = floridaLineups.index(lineup)
        opponentLineupNum = opponentLineups.index(currentOpponentLineup)
        CreateMatchup(floridaLineupNum, opponentLineupNum, time, floridaScore, opponentScore)
        return 0
    else:
        floridaLineups.append(lineup)
        floridaLineupNum = floridaLineups.index(lineup)
        opponentLineupNum = opponentLineups.index(currentOpponentLineup)
        CreateMatchup(floridaLineupNum, opponentLineupNum, time, floridaScore, opponentScore)
        return 0


def CreateOpponentLineup(lineup, time, floridaScore, opponentScore):
    """Take in new lineup, append lineup, call CreateMatchup."""
    global currentOpponentLineup
    global opponentLineups
    currentOpponentLineup = lineup
    if (lineup in opponentLineups):
        opponentLineupNum = opponentLineups.index(lineup)
        floridaLineupNum = floridaLineups.index(currentFloridaLineup)
        CreateMatchup(floridaLineupNum, opponentLineupNum, time, floridaScore,
                      opponentScore)
        return 0
    else:
        opponentLineups.append(lineup)
        opponentLineupNum = opponentLineups.index(lineup)
        floridaLineupNum = floridaLineups.index(currentFloridaLineup)
        CreateMatchup(floridaLineupNum, opponentLineupNum, time, floridaScore,
                      opponentScore)
        return 0


def IdentifyPlayFlorida(play, time, score):
    """Take in play, identify which kind of play it is to increment proper stats."""
    if ("misses" in play) and ("two" in play):
        print("Florida two point miss")
        matchupsList[-1].florida2PFGA += 1
        return 0
    elif ("misses" in play) and ("three" in play):
        print("Florida three point miss")
        matchupsList[-1].florida3PFGA += 1
        return 0
    elif ("misses" in play) and ("free" in play):
        print("Florida free point miss")
        matchupsList[-1].floridaFTA += 1
        return 0
    elif ("misses" in play) and (("layup" in play) or
                                 ("hook" in play) or ("dunk" in play)):
        print("Florida paint miss")
        matchupsList[-1].floridaPFGA += 1
        return 0
    elif ("makes" in play) and ("two" in play):
        print("Florida two point make")
        matchupsList[-1].florida2PFGA += 1
        matchupsList[-1].florida2PFGM += 1
        return 0
    elif ("makes" in play) and ("three" in play):
        print("Florida three point make")
        matchupsList[-1].florida3PFGA += 1
        matchupsList[-1].florida3PFGM += 1
        return 0
    elif ("makes" in play) and ("free" in play):
        print("Florida free point make")
        matchupsList[-1].floridaFTA += 1
        matchupsList[-1].floridaFTM += 1
        return 0
    elif ("makes" in play) and (("layup" in play) or
                                ("hook" in play) or ("dunk" in play)):
        print("Florida paint make")
        matchupsList[-1].floridaPFGA += 1
        matchupsList[-1].floridaPFGM += 1
        return 0
    elif ("foul" in play):
        print("Florida foul")
        matchupsList[-1].floridaPF += 1
        return 0
    elif ("defensive" in play):
        print("Florida defensive rebound")
        matchupsList[-1].floridaDRB += 1
        return 0
    elif ("offensive" in play):
        print("Florida offensive rebound")
        matchupsList[-1].floridaORB += 1
        return 0
    elif ("turnover" in play):
        print("Florida turnover")
        matchupsList[-1].floridaTO += 1
        return 0
    elif ("blocks" in play):
        print("Florida block")
        matchupsList[-1].floridaBLK += 1
        return 0
    elif ("lineup" in play):
        print("Florida substitution")
        splitstring = play.split(" ")
        pieces = splitstring[3:]
        lineupstring = " "
        lineupstring = lineupstring.join(pieces)
        lineupstring = lineupstring[1:-1]
        lineuptime = ConvertTimeToSeconds(time)
        splitScores = score.split("-")
        if (HOME):
            floridaScore = int(splitScores[0])
            opponentScore = int(splitScores[1])
        else:
            opponentScore = int(splitScores[0])
            floridaScore = int(splitScores[1])
        CreateFloridaLineup(lineupstring, lineuptime, floridaScore,
                            opponentScore)
        return 0
    else:
        print(play)
        return 0


def IdentifyPlayOpponent(play, time, score):
    """Take in play, identify which kind of play it is to increment proper stats."""
    if ("misses" in play) and ("two" in play):
        print("Opponent two point miss")
        matchupsList[-1].opponent2PFGA += 1
        return 0
    elif ("misses" in play) and ("three" in play):
        print("Opponent three point miss")
        matchupsList[-1].opponent3PFGA += 1
        return 0
    elif ("misses" in play) and ("free" in play):
        print("Opponent free point miss")
        matchupsList[-1].opponentFTA += 1
        return 0
    elif ("misses" in play) and (("layup" in play) or
                                 ("hook" in play) or ("dunk" in play)):
        print("Opponent paint miss")
        matchupsList[-1].opponentPFGA += 1
        return 0
    elif ("makes" in play) and ("two" in play):
        print("Opponent two point make")
        matchupsList[-1].opponent2PFGA += 1
        matchupsList[-1].opponent2PFGM += 1
        return 0
    elif ("makes" in play) and ("three" in play):
        print("Opponent three point make")
        matchupsList[-1].opponent3PFGA += 1
        matchupsList[-1].opponent3PFGM += 1
        return 0
    elif ("makes" in play) and ("free" in play):
        print("Opponent free point make")
        matchupsList[-1].opponentFTA += 1
        matchupsList[-1].opponentFTM += 1
        return 0
    elif ("makes" in play) and (("layup" in play) or
                                ("hook" in play) or ("dunk" in play)):
        print("Opponent paint make")
        matchupsList[-1].opponentPFGA += 1
        matchupsList[-1].opponentPFGM += 1
        return 0
    elif ("foul" in play):
        print("Opponent foul")
        matchupsList[-1].opponentPF += 1
        return 0
    elif ("defensive" in play):
        print("Opponent defensive rebound")
        matchupsList[-1].opponentDRB += 1
        return 0
    elif ("offensive" in play):
        print("Opponent offensive rebound")
        matchupsList[-1].opponentORB += 1
        return 0
    elif ("turnover" in play):
        print("Opponent turnover")
        matchupsList[-1].opponentTO += 1
        return 0
    elif ("blocks" in play):
        print("Opponent block")
        matchupsList[-1].opponentBLK += 1
        return 0
    elif ("lineup" in play):
        print("Opponent substitution")
        splitstring = play.split(" ")
        pieces = splitstring[3:]
        lineupstring = " "
        lineupstring = lineupstring.join(pieces)
        lineupstring = lineupstring[1:-1]
        lineuptime = ConvertTimeToSeconds(time)

        splitScores = score.split("-")
        if (HOME):
            floridaScore = int(splitScores[0])
            opponentScore = int(splitScores[1])
        else:
            opponentScore = int(splitScores[0])
            floridaScore = int(splitScores[1])

        CreateOpponentLineup(lineupstring, lineuptime, floridaScore,
                             opponentScore)
        return 0
    else:
        print(play)
        return 0


CreateFloridaStartingLineup(florida_starters, "20:00", 0, 0)
CreateOpponentStartingLineup(opp_starters, "20:00", 0, 0)
latestScore = ""
if(HOME):
    for i in range(len(data['periods'][0]['playStats'])):
        if (data['periods'][0]['playStats'][i]['homeText']):
            IdentifyPlayFlorida((data['periods'][0]['playStats'][i]['homeText']), (data['periods'][0]['playStats'][i]['time']), latestScore)
            if ((data['periods'][0]['playStats'][i]['score'])):
                latestScore = (data['periods'][0]['playStats'][i]['score'])
        else:
            IdentifyPlayOpponent((data['periods'][0]['playStats'][i]['visitorText']), (data['periods'][0]['playStats'][i]['time']), latestScore)
            if ((data['periods'][0]['playStats'][i]['score'])):
                latestScore = (data['periods'][0]['playStats'][i]['score'])
    for j in range(len(data['periods'][1]['playStats'])):
        if (data['periods'][1]['playStats'][j]['homeText']):
            IdentifyPlayFlorida((data['periods'][1]['playStats'][j]['homeText']), (data['periods'][1]['playStats'][j]['time']), latestScore)
            if ((data['periods'][1]['playStats'][j]['score'])):
                latestScore = (data['periods'][1]['playStats'][j]['score'])
        else:
            IdentifyPlayOpponent((data['periods'][1]['playStats'][j]['visitorText']), (data['periods'][1]['playStats'][j]['time']), latestScore)
            if ((data['periods'][1]['playStats'][j]['score'])):
                latestScore = (data['periods'][1]['playStats'][j]['score'])
    if (int(data['meta']['period']) >= 3):
        for o in range(3, int(data['meta']['period'])):
            for k in range(len(data['periods'][o]['playStats'])):
                if (data['periods'][o]['playStats'][k]['homeText']):
                    IdentifyPlayFlorida((data['periods'][o]['playStats'][k]['homeText']), (data['periods'][o]['playStats'][k]['time']), latestScore)
                    if ((data['periods'][o]['playStats'][k]['score'])):
                        latestScore = (data['periods'][o]['playStats'][k]['score'])
                else:
                    IdentifyPlayOpponent((data['periods'][o]['playStats'][k]['visitorText']), (data['periods'][o]['playStats'][k]['time']), latestScore)
                    if ((data['periods'][o]['playStats'][k]['score'])):
                        latestScore = (data['periods'][o]['playStats'][k]['score'])
else:
    for i in range(len(data['periods'][0]['playStats'])):
        if (data['periods'][0]['playStats'][i]['homeText']):
            IdentifyPlayOpponent((data['periods'][0]['playStats'][i]['homeText']), (data['periods'][0]['playStats'][i]['time']), latestScore)
            if ((data['periods'][0]['playStats'][i]['score'])):
                latestScore = (data['periods'][0]['playStats'][i]['score'])
        else:
            IdentifyPlayFlorida((data['periods'][0]['playStats'][i]['visitorText']), (data['periods'][0]['playStats'][i]['time']), latestScore)
            if ((data['periods'][0]['playStats'][i]['score'])):
                latestScore = (data['periods'][0]['playStats'][i]['score'])
    for j in range(len(data['periods'][1]['playStats'])):
        if (data['periods'][1]['playStats'][j]['homeText']):
            IdentifyPlayOpponent((data['periods'][1]['playStats'][j]['homeText']), (data['periods'][1]['playStats'][j]['time']), latestScore)
            if ((data['periods'][1]['playStats'][j]['score'])):
                latestScore = (data['periods'][1]['playStats'][j]['score'])
        else:
            IdentifyPlayFlorida((data['periods'][1]['playStats'][j]['visitorText']), (data['periods'][1]['playStats'][j]['time']), latestScore)
            if ((data['periods'][1]['playStats'][j]['score'])):
                latestScore = (data['periods'][1]['playStats'][j]['score'])
    if (int(data['meta']['period']) >= 3):
        for o in range(3, int(data['meta']['period'])):
            for k in range(len(data['periods'][o]['playStats'])):
                if (data['periods'][o]['playStats'][k]['homeText']):
                    IdentifyPlayOpponent((data['periods'][o]['playStats'][k]['homeText']), (data['periods'][o]['playStats'][k]['time']), latestScore)
                    if ((data['periods'][o]['playStats'][k]['score'])):
                        latestScore = (data['periods'][o]['playStats'][k]['score'])
                else:
                    IdentifyPlayFlorida((data['periods'][o]['playStats'][k]['visitorText']), (data['periods'][o]['playStats'][k]['time']), latestScore)
                    if ((data['periods'][o]['playStats'][k]['score'])):
                        latestScore = (data['periods'][o]['playStats'][k]['score'])


# team1stats[0]=2PFGM [1]=2PFGA  [2]=PFGM [3]=PFGA  [4]=3PFGM [5]=3PFGA
# [6]=FTM [7]=FTA  [8]=TO [9]=ORB [10]=DRB # [11]= PF [12]=BLK

for x in matchupsList:
    print("Matchup: Florida ", x.floridaLineupIndex, " vs. Cincinatti ",
          x.opponentLineupIndex)
    print("Florida lineup: ", floridaLineups[x.floridaLineupIndex])
    print("Opponent lineup: ", opponentLineups[x.opponentLineupIndex])
    print("Start time: ", x.startTime)
    print("Finish time: ", x.finishTime)
    print("Florida bigs: ", x.floridaBigs)
    print("Opponent bigs: ", x.opponentBigs)
    print("Florida starting score: ", x.floridaStartScore)
    print("Florida ending score: ", x.floridaEndScore)
    print("Opponent starting score: ", x.opponentStartScore)
    print("Opponent starting score: ", x.opponentEndScore)
    print("Florida Stats: ")
    print("Two point field goals made: ", x.florida2PFGM)
    print("Two point field goals attempted: ", x.florida2PFGA)
    print("Paint field goals made: ", x.floridaPFGM)
    print("Paint field goals attempted: ", x.floridaPFGA)
    print("Three point field goals made: ", x.florida3PFGM)
    print("Three point field goals attempted: ", x.florida3PFGA)
    print("Free throws made: ", x.floridaFTM)
    print("Free throws attempted: ", x.floridaFTA)
    print("Turnovers commited: ", x.floridaTO)
    print("Offensive rebounds: ", x.floridaORB)
    print("Defensive rebounds: ", x.floridaDRB)
    print("Personal fouls: ", x.floridaPF)
    print("Blocks: ", x.floridaBLK)
    print("Opponent Stats: ")
    print("Two point field goals made: ", x.opponent2PFGM)
    print("Two point field goals attempted: ", x.opponent2PFGA)
    print("Paint field goals made: ", x.opponentPFGM)
    print("Paint field goals attempted: ", x.opponentPFGA)
    print("Three point field goals made: ", x.opponent3PFGM)
    print("Three point field goals attempted: ", x.opponent3PFGA)
    print("Free throws made: ", x.opponentFTM)
    print("Free throws attempted: ", x.opponentFTA)
    print("Turnovers commited: ", x.opponentTO)
    print("Offensive rebounds: ", x.opponentORB)
    print("Defensive rebounds: ", x.opponentDRB)
    print("Personal fouls: ", x.opponentPF)
    print("Blocks: ", x.opponentBLK)
