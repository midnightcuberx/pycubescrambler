import random

def get_ivy():
    moves = ["L", "R", 'D', 'B']
    turns= [' ', "' "]
    scramble = []
    usedmoves = []
    usedmoves1 = []
    
    for i in range(8):

        if i % 2 == 0:
            
            randmoves = random.choice(moves)
            usedmoves.append(randmoves)
            scramble.append(randmoves)
            scramble.append(random.choice(turns))
            moves.remove(randmoves)

            if i != 0:
                moves.append(usedmoves1[-1])

        else:
            randmoves1 = random.choice(moves)
            scramble.append(randmoves1)
            usedmoves1.append(randmoves1)
            scramble.append(random.choice(turns))
            moves.remove(randmoves1)
            moves.append(usedmoves[-1])
    return "".join(scramble)
