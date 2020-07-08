import random
from . import sq1scrambler, trim

@trim
def get_squan():
    return sq1scrambler.call("sql_scrambler.getRandomScramble")

def get_clock():
  moves = ["0+ ","1+ ","2+ ","3+ ","4+ ","5+ ","6+ ","1- ","2- ","3- ","4- ","5- "]
  pins = ["UR","DR","DL","UL","U","R","D","L","ALL","U","R","D","L","ALL"]
  scramble = []

  for i in range(14):
      scramble.append(pins[i])
      scramble.append(random.choice(moves))

  def sort_l4m():
    l4m=["UR ","DR ","DL ","UL "]
    l4ms=[]
    for i in range(4):
      number=random.randint(1,2)
      if number==1:
        l4ms.append(l4m[i])
    return "".join(l4ms)

  last4=sort_l4m()
  scramble.append(last4)

  return "".join(scramble)


def get_skewb():
  y=random.randint(8,10)
  moves = ["B","R","L","U"]
  turns = [" ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  for i in range(y):

      if i % 2 ==0:

        randmoves=random.choice(moves)
        usedmoves.append(randmoves)
        scramble.append(randmoves)
        scramble.append(random.choice(turns))
        moves.remove(randmoves)
        if i != 0:
          moves.append(usedmoves1[-1])

      else:

        randmoves1=random.choice(moves)
        scramble.append(randmoves1)
        usedmoves1.append(randmoves1)
        scramble.append(random.choice(turns))
        moves.remove(randmoves1)
        moves.append(usedmoves[-1])
  return "".join(scramble)

def get_mega():
  turns=["-- ","++ "]
  umoves=["U'","U"]
  scramble=[]
  for i in range(7):
    scrambles=[]
    for x in range(5):
      for y in range(2):
        if y==0:
          scrambles.append("R")
        else:
          scrambles.append("D")
        scrambles.append(random.choice(turns))
    scrambles.append(random.choice(umoves))
    scramble.append("".join(scrambles))
  return "\n".join(scramble)


def get_pyra():
  y=random.randint(8,10)
  moves = ["B","R","L","U"]
  turns = [" ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]

  def sort_tips():

    tips=["l","r","b","u"]
    tip=[]

    for i in range(4):
      number=random.randint(1,2)
      if number==1:
        tip.append(tips[i])
        tip.append(random.choice(turns))

    return "".join(tip)


  for i in range(y):

      if i % 2 ==0:

        randmoves=random.choice(moves)
        usedmoves.append(randmoves)
        scramble.append(randmoves)
        scramble.append(random.choice(turns))
        moves.remove(randmoves)
        if i != 0:
          moves.append(usedmoves1[-1])

      else:

        randmoves1=random.choice(moves)
        scramble.append(randmoves1)
        usedmoves1.append(randmoves1)
        scramble.append(random.choice(turns))
        moves.remove(randmoves1)
        moves.append(usedmoves[-1])

  thetips=sort_tips()
  scramble.append(thetips)
  return "".join(scramble)
