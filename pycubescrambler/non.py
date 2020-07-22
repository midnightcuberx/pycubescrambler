import random
from . import joinscramble

@joinscramble("")
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
    return scramble


@joinscramble("")
def get223():
    num_moves = random.randint(8, 10)
    double_moves = ["R", "F"]
    single_moves = ["U", "D"]
    turns = ["2 ", " ", "' "]
    scramble = []

    for i in range(num_moves):

        if i % 2 == 0:
            randmoves = random.choice(double_moves)
            scramble.append(randmoves)
            turn ="2 "

            scramble.append(turn)
        else:
            randmoves1 = random.choice(single_moves)
            scramble.append(randmoves1)
            scramble.append(random.choice(turns))

    return scramble

@joinscramble("\n")
def get_kilo():
  turns=["-- ","++ "]
  umoves=["U'","U"]
  scramble=[]
  for i in range(4):
    scrambles=[]
    for x in range(5):
      for y in range(2):
        if y==0:
          scrambles.append("R")
        else:
          scrambles.append("D")
        scrambles.append(random.choice(turns))
    scrambles.append(random.choice(umoves))
    if i!=3:
      scrambles.append(" x2 ")
    scramble.append("".join(scrambles))
  return scramble


@joinscramble("\n")
def get_redi():
    turns = [" ", "' "]
    scramble = []

    for i in range(8):
        scrambles = []
        num_moves = random.randint(2, 5)
        for x in range(num_moves):
            for y in range(2):
                if y == 0:
                    scrambles.append("R")
                else:
                    scrambles.append("L")
                scrambles.append(random.choice(turns))
        if i != 7:
            scrambles.append("x")
        scramble.append("".join(scrambles))

    return scramble

@joinscramble("")
def get133():
    moves = ["B", "F", "R", "L"]
    turns = ["' ", " "]
    usedmoves = []
    usedmoves1 = []
    num_moves = random.randint(5, 10)
    scramble = []
    list1=["F","B"]	
    list2=["R","L"]	
    for i in range(num_moves):
        if i % 2 == 0:
            randmoves = random.choice(moves)
            if i>1:                   	
              while (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2):	
                randmoves=random.choice(moves)    
            scramble.append(randmoves)
            scramble.append(random.choice(turns))
            usedmoves.append(randmoves)
            moves.remove(randmoves)

            if i != 0:
                moves.append(usedmoves1[-1])

        else:
            randmoves1 = random.choice(moves)
            if i>1:	
              while (randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2):
                randmoves1=random.choice(moves) 
            scramble.append(randmoves1)
            scramble.append(random.choice(turns))
            usedmoves1.append(randmoves1)
            moves.remove(randmoves1)
            moves.append(usedmoves[-1])

    return scramble

@joinscramble("")
def get_masterpyra():
    num_moves = random.randint(38, 42)
    moves = ["R", "L", "U", "B", "Uw", "Lw", "Bw", "Rw"]
    turns = [" ", "' "]
    list1 = ["U", "Uw"]
    list2 = ["L", "Lw"]
    list3 = ["R", "Rw"]
    list4 = ["B", "Bw"]
    scramble = []
    usedmoves = []
    usedmoves1 = []

    @joinscramble("")
    def sort_tips():

        tips = ['u', 'b', 'r', 'l']
        tip = []

        for x in range(4):
            number = random.randint(1, 2)
            if number == 1:
                tip.append(tips[x])
                tip.append(random.choice(turns))

        return tip

    for i in range(num_moves):

        if i % 2 == 0:
            randmoves = random.choice(moves)
            if i > 1:

                while (randmoves in list1 and scramble[-2] in list1) or (randmoves in list2 and scramble[-2] in list2) \
                        or (randmoves in list3 and scramble[-2] in list3) or (randmoves in list4 and scramble[-2] in
                                                                              list4):
                    randmoves = random.choice(moves)

            usedmoves.append(randmoves)
            scramble.append(randmoves)
            scramble.append(random.choice(turns))
            moves.remove(randmoves)
            if i != 0:
                moves.append(usedmoves1[-1])

        else:
            randmoves1 = random.choice(moves)
            if i > 1:

                while (randmoves1 in list1 and scramble[-2] in list1) or (randmoves1 in list2 and scramble[-2] in list2)\
                        or (randmoves1 in list3 and scramble[-2] in list3) or (randmoves1 in list4 and scramble[-2] in list4):
                    randmoves1 = random.choice(moves)
            scramble.append(randmoves1)
            usedmoves1.append(randmoves1)
            scramble.append(random.choice(turns))
            moves.remove(randmoves1)
            moves.append(usedmoves[-1])

    thetips = sort_tips()
    scramble.append(thetips)
    return scramble

@joinscramble("")
def get233():
    scramble = []
    usedmoves = []
    usedmoves1 = []
    moves = ["R2 ", "L2 ", "F2 ", "B2 ", "U"]
    turns = [" ", "' ", "2 "]

    for i in range(25):
        if i % 2 == 0:

            randmove = random.choice(moves)
            scramble.append(randmove)
            usedmoves.append(randmove)

            if randmove == "U":
                scramble.append(random.choice(turns))

            moves.remove(randmove)

            if i != 0:
                moves.append(usedmoves1[-1])

        else:
            randmove1 = random.choice(moves)
            scramble.append(randmove1)
            usedmoves1.append(randmove1)
            moves.remove(randmove1)
            moves.append(usedmoves[-1])

            if randmove1 == "U":
                scramble.append(random.choice(turns))

    return scramble
