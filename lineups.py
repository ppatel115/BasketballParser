#trying to create a lineup object
class lineups(object):
    def __init__(self, lineup, lname1, lname2, lname3, lname4, lname5):
        self.lineup = lineup
        self.lname1 = lname1
        self.lname2 = lname2
        self.lname3 = lname3
        self.lname4 = lname4
        self.lname5 = lname5

#The lineups used in the first half of the Cincinatti Game, the "lineup" is just a 10 digit code with the players numbers in numerical order

Gators_lineups = [lineups("0304051125", "Hudson", "Koulechov", "Allen", "Chiozza", "Stone"),
                  lineups("0405111324", "Koulechov", "Allen", "Chiozza", "Hayes", "Ballard"),
                  lineups("0305132425", "Hudson", "Allen", "Hayes", "Ballard", "Stone"),
                  lineups("0311122425", "Hudson", "Chiozza", "Gak", "Ballard", "Stone"),
                  lineups("0304111225", "Hudson", "Koulechov", "Chiozza", "Gak", "Stone"),
                  lineups("0304111325", "Hudson", "Koulechov", "Chiozza", "Hayes", "Stone"),
                  lineups("0304051325", "Hudson", "Koulechov", "Allen", "Hayes", "Stone"),
                  lineups("0304051113", "Hudson", "Koulechov", "Allen", "Chiozza", "Hayes"),
                  lineups("0405111224", "Koulechov", "Allen", "Chiozza", "Gak", "Ballard")]

#not sure if this will help either but here it is :^)
Gators = [("Mike", "Okauru", "00"),("Chase", "Johnson", "01"), ("Jalen", "Hudson", "03"),
            ("Egor", "Koulechov", "04"), ("Kevaughn", "Allen", "05"), ("Chris", "Chiozza", "11"),
            ("Gorjok", "Gak", "12"), ("Kevarrius", "Hayes", "13"), ("John", "Egbunu", "15"),
            ("Dontay", "Bassett", "21"), ("Deaundrae", "Ballard", "24"), ("Keith", "Stone", "25")]
