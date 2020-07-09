import random
from . import main, joinscramble

@joinscramble
def big(n):
  scramble=main.big(n)
  return scramble

@joinscramble
def get1():
  moves = ["x","y","z"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  for i in range(8):
                
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
  return scramble

@joinscramble
def get2(): 
  moves = ["F","R","U"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  num=random.randint(8,12)
  for i in range(num):
                
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
  return scramble

@joinscramble
def get3():
  scramble=main.get3()
  return scramble



def get_fmc():
  a=main.get3()
  a="".join(a).split()
  list1=["F","F2","F'","B'","B2","B"]
  list2=["R2","R","R'","L","L'","L2"]
  list3=["F","F2","F'"]
  list4=["R2","R","R'"]
  times=0
  while (a[0] in list1 and a[1] in list1) or (a[0] in list3) or (a[-1] in list2 and a[-2] in list2) or (a[-1] in list4):
    if times>3:
      a=main.get3()
      a="".join(a).split()
      times=0

    if a[0] in list3:
      a.remove(a[0])
      times+=1

    if (a[0] in list1 and a[1] in list1):
      if a[0] not in list3:
        a.remove(a[1])
        times+=1

    
    if a[-1] in list4:
      a.remove(a[-1])
      times+=1
    
    if (a[-1] in list2 and a[-2] in list2):
      if a[-1] not in list4:
        a.remove(a[-2])
        times+=1

  scramble="R' U' F " + " ".join(a) + " R' U' F"
  return scramble

@joinscramble
def get4():
  scramble=main.get4()
  return scramble




@joinscramble
def get5():
  scramble=main.get5()
  return scramble

@joinscramble
def get6():
  scramble=main.big(6)
  return scramble

@joinscramble
def get7():
  scramble=main.big(7)
  return scramble

@joinscramble
def get8():
  scramble=main.big(8)
  return scramble

@joinscramble
def get9():
  scramble=main.big(9)
  return scramble

@joinscramble
def get10():
  scramble=main.big(10)
  return scramble

@joinscramble
def get11():
  scramble=main.big(11)
  return scramble

@joinscramble
def get12():
  scramble=main.big(12)
  return scramble

@joinscramble
def get_big_cube(n=12):
  scramble=main.big(n)
  return scramble
