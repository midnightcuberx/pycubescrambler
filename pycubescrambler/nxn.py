import random
class main():
  def get3():	
    moves = ["F","B","R","L","U","D"]	
    turns = [" ","2 ","' ","2 "]	
    scramble = []	
    usedmoves=[]	
    usedmoves1=[]	
    list1=["F","B","Fw"]	
    list2=["R","L","Rw"]	
    list3=["D","U","Uw"]	
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
    return "".join(scramble)
    
  def big(n):
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
    n1=int(n/2)
    if n% 2==0:
        times=int(n/2)
    else:
        times=int(n/2)+1
    for i in range(3,times):
      if n % 2==0:
          for ru in ruf:

              moves.append(f"{n1}{ru}w")
              if ru=="R":
                  list2.append(f"{n1}{ru}w")
              elif ru=="U":
                  list1.append(f"{n1}{ru}w")
              elif ru=="F":
                  list3.append(f"{n1}{ru}w")

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
    return "".join(scramble)
