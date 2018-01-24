# Parser intializes a lineup every Substitution call, stores matchup stats in
# Matchup


"""Class definition for Matchup of lineups."""


class Matchup(object):
    """Main class for forming a matchup."""
# team1stats[0]=2PFGM [1]=2PFGA  [2]=PFGM [3]=PFGA  [4]=3PFGM [5]=3PFGA
# [6]=FTM [7]=FTA  [8]=TO [9]=ORB [10]=DRB # [11]= PF [12]=BLK

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

    def __init__(self, floridaIndexNumber, floridaBigs, opponentLineupIndex,
                 opponentBigs, startTime, floridaStartScore,
                 opponentStartScore):
        """Init matchup with team names and lineup numbers."""
        self.floridaLineupIndex = floridaIndexNumber
        self.opponentLineupIndex = opponentLineupIndex
        self.floridaBigs = floridaBigs
        self.opponentBigs = opponentBigs
        self.startTime = startTime
        self.finishTime = 1000
        self.floridaStartScore = floridaStartScore
        self.opponentStartScore = opponentStartScore
        self.floridaEndScore = 1000
        self.opponentEndScore = 1000

        self.florida2PFGM = 0
        self.florida2PFGA = 0
        self.floridaPFGM = 0
        self.floridaPFGA = 0
        self.florida3PFGM = 0
        self.florida3PFGA = 0
        self.floridaFTM = 0
        self.floridaFTA = 0
        self.floridaTO = 0
        self.floridaORB = 0
        self.floridaDRB = 0
        self.floridaPF = 0
        self.floridaBLK = 0

        self.opponent2PFGM = 0
        self.opponent2PFGA = 0
        self.opponentPFGM = 0
        self.opponentPFGA = 0
        self.opponent3PFGM = 0
        self.opponent3PFGA = 0
        self.opponentFTM = 0
        self.opponentFTA = 0
        self.opponentTO = 0
        self.opponentORB = 0
        self.opponentDRB = 0
        self.opponentPF = 0
        self.opponentBLK = 0
