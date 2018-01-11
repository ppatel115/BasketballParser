# Parser intializes a lineup every Substitution call, stores matchup stats in
# Matchup


"""Class definition for Matchup of lineups."""


class Matchup(object):
    """Main class for forming a matchup."""

    floridaLineupIndex = 1000     # 0-15ish probably used per team
    opponentLineupIndex = 1000
    floridaLineupStats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    opponentLineupStats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# team1stats[0]=2PFGM [1]=2PFGA  [2]=PFGM [3]=PFGA  [4]=3PFGM [5]=3PFGA
# [6]=FTM [7]=FTA  [8]=TO [9]=ORB [10]=DRB [12]=Initial time
# [13]=Final time [14]=Total time in play
# how to track minutes?

# TODO
# For minutes, can take in the current game time when sub occurs, ex: 19:33
# Then, convert that time to seconds after parsing minutes and seconds ex: 1173
# Store this as [11] = initial time.
# The next sub initial time is this lineup's [12] = final time.  ex: 765
# After getting the final time, calculate the lineup's time and add it to
# the lineup's total time on the floor [13] ex: 1173 - 765 = 408 seconds

# fakestring = " 5:99"
# print(fakestring)
# sliced1 = fakestring[-4:]
# print(sliced1)
# sliced2 = sliced1[:1]
# print(int(sliced2))

# Maybe after parsing whole game, go back and convert total seconds to actual
# minutes?

    def __init__(self, floridaLineupIndex, opponentLineupIndex,
                 floridaLineupStats, opponentLineupStats):
        """Init matchup with team names and lineup numbers."""
        self.floridaLineupIndex = floridaLineupIndex
        self.opponentLineupIndex = opponentLineupIndex
        self.floridaLineupStats = floridaLineupStats
        self.opponentLineupStats = opponentLineupStats


def make_matchup(floridaLineup, opponentLineup):
    """Create a matchup."""
    matchup = Matchup(floridaLineup, opponentLineup)
    return matchup
