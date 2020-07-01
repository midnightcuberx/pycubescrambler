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


def get_223():
    num_moves = random.randint(8, 10)
    double_moves = ["R", "F"]
    single_moves = ["U", "D"]
    turns = ["2 ", " ", "' "]
    usedmoves = []
    usedmoves1 = []
    scramble = []

    for i in range(num_moves):

        if i % 2 == 0:
            randmoves = random.choice(double_moves)
            scramble.append(randmoves)
            usedmoves.append(randmoves)
            double_moves.remove(randmoves)
            turn = random.choice(turns)

            while turn != "2 ":
                turn = random.choice(turns)

            scramble.append(turn)

            if i != 0:
                double_moves.append(usedmoves[-1])

        else:
            randmoves1 = random.choice(single_moves)
            scramble.append(randmoves1)
            usedmoves.append(randmoves1)
            single_moves.remove(randmoves1)
            scramble.append(random.choice(turns))
            usedmoves1.append(randmoves1)

            if i != 0:
                single_moves.append(usedmoves1[-1])

    return "".join(scramble)
