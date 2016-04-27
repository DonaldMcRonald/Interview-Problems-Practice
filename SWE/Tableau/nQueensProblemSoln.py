class Queen:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.left_to_top_diag = _x - _y
        self.left_to_bot_diag = _x + _y
    def __str__(self):
        return str(self.x) + " " + str(self.y)

def queenComparison(q1, q2):
    return (q1.x == q2.x or q1.y == q2.y
        or q1.left_to_top_diag == q2.left_to_top_diag
        or q1.left_to_bot_diag == q2.left_to_bot_diag)

# Input array of queens coordinates
allQueensCoordinates = [(1,3),(2,5),(3,7),(4,2),(6,5),(4,4)]
# Input Queen coordinates
inputQueen = (2,2)

def solver(queenCoord, allQueensCoordinates):
    queen = Queen(queenCoord[0], queenCoord[1])
    queenArray = [Queen(coord[0], coord[1]) for coord in allQueensCoordinates]

    return sum([1 for q in queenArray if queenComparison(queen, q)])

print(solver(inputQueen, allQueensCoordinates))
