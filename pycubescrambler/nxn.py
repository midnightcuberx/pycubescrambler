import random
class main():
  def get3():	
    moves = ["F","B","R","L","U","D"]	
    turns = [" ","2 ","' ","2 "]	
    scramble = []	
    usedmoves=[]	
    usedmoves1=[]	
    list1=["F","B"]	
    list2=["R","L"]	
    list3=["D","U"]	
    for i in range(20):	

      if i % 2 ==0:	
        randmoves=random.choice(moves)	
        if i>1:                   	
          while (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3):	
            randmoves=random.choice(moves)     	
        usedmoves.append(randmoves)	
        scramble.append(randmoves)	
        scramble.append(random.choice(turns))	
        moves.remove(randmoves)	
        if i != 0:	
          moves.append(usedmoves1[-1])	

      else:	

        randmoves1=random.choice(moves)	
        if i>1:	
          while (randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3):	
            randmoves1=random.choice(moves) 	

        scramble.append(randmoves1)	
        usedmoves1.append(randmoves1)	
        scramble.append(random.choice(turns))	
        moves.remove(randmoves1)	
        moves.append(usedmoves[-1])	
    return scramble
    
  def big(n=12,scramtype="big"):
    moves = ["F","B","R","L","U","D","Uw","Dw","Fw","Bw","Rw","Lw"]
    turns = [" ","2 ","' "]
    moveslist = ["F","B","R","L","U","D"]
    scramble = []
    usedmoves=[]
    usedmoves1=[]
    ruf=["R","U","F"]
    list1=["U","D","Uw","Dw"]
    list2=["R","L","Lw","Rw"]
    list3=["F","B","Fw","Bw"]
    try:
      n1=int(n/2)
    except TypeError:
      raise TypeError("Invalid number")
    if n% 2==0:
      times=int(n/2)
      for ru in ruf:

        moves.append(f"{n1}{ru}w")
        if ru=="R":
          list2.append(f"{n1}{ru}w")
        elif ru=="U":
          list1.append(f"{n1}{ru}w")
        elif ru=="F":
          list3.append(f"{n1}{ru}w")

    else:
        times=int(n/2)+1
    for i in range(3,times):
      for move in moveslist:
          moves.append(f"{i}{move}w")
          if move=="U" or move=="D":
              list1.append(f"{i}{move}w")
          elif move=="R" or move=="L":
              list2.append(f"{i}{move}w")
          elif move=="B" or move=="F":
              list3.append(f"{i}{move}w")
    if n<8:
      num=n*20-40
    else:
      num=n*15
    for i in range(num):

      if i % 2 ==0:
        randmoves=random.choice(moves)
        if i>1:
          if (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3):
            while randmoves==scramble[-4]:
              randmoves=random.choice(moves)
          if i>2:
            while (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1 and scramble[-6] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2 and scramble[-6] in list2) or (randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3 and scramble[-6] in list3):
              randmoves=random.choice(moves)
        usedmoves.append(randmoves)
        scramble.append(randmoves)
        scramble.append(random.choice(turns))
        moves.remove(randmoves)
        if i != 0:
          moves.append(usedmoves1[-1])

      else:
        randmoves1=random.choice(moves)
        if i>2:
          randmoves1=random.choice(moves)
          if (randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3):
            while randmoves1==scramble[-4]:
              randmoves1=random.choice(moves) 
          while (randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1 and scramble[-6] in list1) or (randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2 and scramble[-6] in list2) or (randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3 and scramble[-6] in list3):
            randmoves1=random.choice(moves)         


        scramble.append(randmoves1)
        usedmoves1.append(randmoves1)
        scramble.append(random.choice(turns))
        moves.remove(randmoves1)
        moves.append(usedmoves[-1])
    if scramtype=="big":
      return "".join(scramble)
    elif scramtype=="bld":
      biggest=int(n/2)+1
      possi=[]
      possi2=[]
      if biggest % 2==0:
        possi=["","x ","x' ","x2 ","z ","z2 ","z' "]
        possi2=["y","y'","y2",""]
      else:
        for move in ruf:
          if move !="U":
            possi.append(f"{biggest}{move}w ")
            possi.append(f"{biggest}{move}w' ")
            possi.append(f"{biggest}{move}w2 ")
          else:
            possi2.append(f"{biggest}{move}w ")
            possi2.append(f"{biggest}{move}w' ")
            possi2.append(f"{biggest}{move}w2 ")
      scramble.append(random.choice(possi))
      scramble.append(random.choice(possi2))
      return "".join(scramble)
    else:
      raise ValueError("Invalid scramble type")
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
  return "".join(scramble)




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
  return "".join(scramble)

def get3(scramtype="3x3"):
  a=main.get3()
  scramtype=scramtype.lower()
  if scramtype=="3x3":
    return "".join(a)
  elif scramtype=="bld":
    scramble=[]
    scramble3=a
    for item in scramble3:
      scramble.append(item)
    possi=["","Rw ","Rw' ","Rw2 ","Fw ","Fw2 ","Fw' "]
    possi2=["Uw","Uw'","Uw2",""]
    scramble.append(random.choice(possi))
    scramble.append(random.choice(possi2))
    return "".join(scramble)
  elif scramtype=="fmc":
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
  else:
    raise ValueError("Invalid scramble type")


def get4(scramtype="4x4"):
  moves=["F","B","R","L","U","D"]
  wide_turns=["F","Fw","B","R","Rw","L","D","U","Uw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["F","B","Fw"]
  list2=["R","L","Rw"]
  list3=["D","U","Uw"]
  scramble=main.get3()
  for i in range(25):
                    
    if i % 2 ==0:
      randmoves=random.choice(wide_turns)
      if randmoves in moves and scramble[-2] in moves and scramble[-4] in moves:
        randmoves=random.choice(wide_turns)
      if (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3):
        while randmoves==scramble[-4]:
          randmoves=random.choice(moves)
      while (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1 and scramble[-6] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2 and scramble[-6] in list2) or (randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3 and scramble[-6] in list3):
        randmoves=random.choice(wide_turns)
      usedmoves.append(randmoves)
      scramble.append(randmoves)
      scramble.append(random.choice(turns))
      wide_turns.remove(randmoves)
      if i != 0:
        wide_turns.append(usedmoves1[-1])
    else:                  
      randmoves1=random.choice(wide_turns)
      if randmoves1 in moves and scramble[-2] in moves and scramble[-4] in moves:
        randmoves1=random.choice(wide_turns)
      if (randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3):
        while randmoves1==scramble[-4]:
          randmoves1=random.choice(moves)
      while (randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3):
        randmoves1=random.choice(wide_turns)
  
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      wide_turns.remove(randmoves1)
      wide_turns.append(usedmoves[-1])
  if scramtype=="4x4":
    return "".join(scramble)
  elif scramtype=="bld":
    possi=["","x ","x' ","x2 ","z ","z2 ","z' "]
    possi2=["y","y'","y2",""]
    scramble.append(random.choice(possi))
    scramble.append(random.choice(possi2))
    return "".join(scramble)
  else:
    raise ValueError("Invalid scramble type")

def get5(scramtype="5x5"):

  if scramtype=="5x5":
    scramble=main.big(5)
  elif scramtype=="bld":
    scramble=main.big(5,"bld")
  else:
    raise ValueError("Invalid scramble type")
  return scramble


def get6():
  scramble=main.big(6)
  return scramble

def get7():
  scramble=main.big(7)
  return scramble

def get8():
  scramble=main.big(8)
  return scramble

def get9():
  scramble=main.big(9)
  return scramble

def get10():
  scramble=main.big(10)
  return scramble

def get11():
  scramble=main.big(11)
  return scramble

def get12():
  scramble=main.big(12)
  return scramble

def get_big_cube(n=12,scramtype="big"):
  scramble=main.big(n,scramtype)
  return scramble
