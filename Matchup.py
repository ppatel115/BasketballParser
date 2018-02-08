"""Class definition for Matchup of lineups."""


class Matchup(object):
    """Main class for forming a matchup."""

# TODO - Add logic to find possession changes
# Possessions can end when:
# (1) field goal attempt is made
# (2) field goal attempt is missed and rebounded by the defense
# (3) free throws where the second free throw is made
# (4) free throws where the second free throw is missed and rebounded
#     by the defense
# (5) the offense turns the ball over, or
# (6) the half ends

    def __init__(self, floridaIndexNumber, floridaBigs, opponentLineupIndex,
                 opponentBigs, startTime, floridaStartScore,
                 opponentStartScore):
        """Init matchup with team names and lineup numbers."""
        self.floridaLineupIndex = floridaIndexNumber
        self.opponentLineupIndex = opponentLineupIndex
        self.floridaBigs = floridaBigs
        self.opponentBigs = opponentBigs
        self.startTime = startTime
        self.finishTime = 0
        self.floridaStartScore = floridaStartScore
        self.opponentStartScore = opponentStartScore
        self.floridaEndScore = 0
        self.opponentEndScore = 0

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
        self.floridaPOSS = 0

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
        self.opponentPOSS = 0
