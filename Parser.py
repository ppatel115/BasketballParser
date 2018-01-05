#!/usr/bin/python2.7

# create text file by pasting SI link into textise.net, and then copy into .txt
from lineups import fl_lineups
from lineups import cin_lineups

homeLineups = fl_lineups
awayLineups = cin_lineups


def IdentifyLineup(currentLineup, teamLineups):
    """Check currentLineup names against allLineups to determine number."""
    if currentLineup in teamLineups:
        # TODO:Once lineup is identified, need to set up matchup
        return


def SubstitutePlayers(playerIn, playerOut, homeLineup, awayLineup):
    """Substitute player into lineup, call IdentifyLineup."""
    if playerOut in homeLineup:
        homeLineup.remove(playerOut)
        homeLineup.append(playerIn)
        homeLineup = IdentifyLineup(homeLineup, homeLineups)
        return homeLineup
    elif playerOut in awayLineup:
        awayLineup.remove(playerOut)
        awayLineup.append(playerIn)
        awayLineup = IdentifyLineup(awayLineup, awayLineups)
        return awayLineup


def ConvertTimeToSeconds(gameTime):
    """Take in gametime, convert to seconds."""
    return


def ConvertSecondsToTime(gameSeconds):
    """Take in seconds, convert to gameTime."""
    return


filepath = 'sample_input.txt'                  # TODO: Take filename from stdin
with open(filepath) as fp:
    line = fp.readline()
while line:
    splitline = line.split(" ")        # do stuff based on single line data
    p1fname = ""        # generally p1 is offensive player,
    p1lname = ""        # p2 is defensive player in 2 player plays
    p2fname = ""
    p2lname = ""
    # (fname and lname)substitute player name for player name in new lineup
if (splitline[2] == "misses" and splitline[3] == "a" and splitline[4] == "jump"):
    print ("Miss 2 pointer")           # missed 2 point shot (FGA incremented)
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "misses" and splitline[4] == "a" and splitline[5] == "jump"):
    print ("Three name miss 2 pointer")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "misses" and splitline[4] == "free"):
    print ("Three name miss free throw")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "misses" and splitline[3] == "a" and splitline[4] == "3-point"):
    print ("Miss 3PA")              # missed 3PA (FGA++, 3PA++)
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "misses" and splitline[4] == "a" and splitline[5]=="3-point"):
    print ("Three name miss 3PA")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "misses" and splitline[3] == "a" and splitline[4] == "layup."):             # missed paint shot (PFGA++)
    print ("Miss paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "misses" and splitline[4] == "a" and splitline[5] == "layup."):             # missed paint shot (PFGA++)
    print ("Three name miss paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "misses" and splitline[3] == "a" and splitline[4] == "hook"):             # missed paint shot (PFGA++)
    print ("Miss paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "misses" and splitline[4] == "a" and splitline[5] == "hook"):             # missed paint shot (PFGA++)
    print ("Three name miss paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "misses" and splitline[3] == "a" and splitline[4] == "dunk."):             # missed paint shot (PFGA++)
    print ("Miss paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "misses" and splitline[4] == "a" and splitline[5] == "dunk."):             # missed paint shot (PFGA++)
    print ("Three name miss paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "makes" and splitline[3] == "a" and splitline[4] == "jump"):             # made 2 pointer (FGA++, FGM++)
    print ("Make 2 pointer")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "makes" and splitline[4] == "a" and splitline[5] == "jump"):
    print ("Three name make 2 pointer")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "makes" and splitline[4] == "free"):
    print ("Three name makes free throw")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "makes" and splitline[3] == "free"):            #FTA++ FTM+++
    print ("Free throw make")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "misses" and splitline[3] == "free"):            #FTA++
    print ("Free throw miss")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "makes" and splitline[3] == "a" and splitline[4]== "3-point"):       #3PA++ 3PM++
    print ("Make 3PA")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "makes" and splitline[4] == "a" and splitline[5]=="3-point"):
    print ("Three name make 3PA")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "makes" and splitline[3] == "a" and splitline[4] == "layup."):    #PFGM++ PFGA++
    print("Make paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "makes" and splitline[4] == "a" and splitline[5] == "layup."):
    print ("Three name make paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "makes" and splitline[3] == "a" and splitline[4] == "hook"):     #PFGM++ PFGA++
    print("Make paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "makes" and splitline[4] == "a" and splitline[5] == "hook"):
    print ("Three name make paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "dunks."):   # PFGM++ PFGA++
    print("Make paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "dunks."):
    print ("Three name make paint shot")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[1] == "foul"):          # PF++
    print ("Foul")
    p1fname = splitline[4]
    p1lname = splitline[5]
elif (splitline[3] == "turnover:"):          # TO++
    print ("Team turnover")
elif (splitline[4] == "turnover"):          # TO++
    print ("Player turnover")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[5] == "turnover"):          # TO++Ma
    print ("Three name player turnover")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "defensive"):          # DRB++
    print ("Team defensive rebound")
elif (splitline[4] == "defensive"):          # DRB++
    print ("Defensive rebound")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[5] == "defensive"):          # DRB++
    print ("Defensive rebound Three name")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[3] == "offensive"):          # ORB++
    print ("Team offensive rebound")
elif (splitline[4] == "offensive"):          # ORB++
    print ("Offensive rebound")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[5] == "offensive"):          # ORB++
    print ("Offensive rebound Three name")
    p1fname = splitline[0]
    p1lname = splitline[1]
elif (splitline[2] == "blocks"):          # BLK++
    print ("Block")
    p2fname = splitline[0]                  # opposing player made the block
    p2lname = splitline[1]
    p1fname = splitline[4]
    p1lname = splitline[5]
elif (splitline[3] == "blocks"):          # BLK++
    print ("Block Three name")
    p2fname = splitline[0]
    p2lname = splitline[1]
    p1fname = splitline[5]
    p1lname = splitline[6]
elif (splitline[2] == "steals"):          # STL++, TO++
    print ("Steal")
    p2fname = splitline[0]
    p2lname = splitline[1]
    p1fname = splitline[6]
    p1lname = splitline[7]
elif (splitline[3] == "steals"):          # STL++, TO++
    print ("Steal Three name")
    p2fname = splitline[0]
    p2lname = splitline[1]
    p1fname = splitline[7]
    p1lname = splitline[8]
elif (splitline[0] == "Substitution:"):
    print ("Sub")
    p1fname = splitline[1]                 # p1 current player
    p1lname = splitline[2]
    p2fname = splitline[5]
    p2lname = splitline[6]

# TODO: Figure out how a possession can end, set up a possession variable
# so we can keep track of which team's lineup gets stats

test = p1fname + ' ' + p1lname + ' ' + p2fname + ' ' + p2lname
print (test)
line = fp.readline()
