import random

def get3():
  colours=["white","yellow","red","orange","green","blue"]
  moves = ["F","B","R","L","U","D"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  for i in range(20):
                            
    if i % 2 ==0:
      randmoves=random.choice(moves)
      if i>1:                      
        while randmoves=="F" and scramble[-4]=="F" and scramble[-2]=="B":
          randmoves=random.choice(moves)
        while randmoves=="B" and scramble[-4]=="B" and scramble[-2]=="F":
          randmoves=random.choice(moves)
        while randmoves=="R" and scramble[-4]=="R" and scramble[-2]=="L":
          randmoves=random.choice(moves)
        while randmoves=="L" and scramble[-4]=="L" and scramble[-2]=="R":
          randmoves=random.choice(moves)
        while randmoves=="U" and scramble[-4]=="U" and scramble[-2]=="D":
          randmoves=random.choice(moves)
        while randmoves=="D" and scramble[-4]=="D" and scramble[-2]=="U":
          randmoves=random.choice(moves)     
      usedmoves.append(randmoves)
      scramble.append(randmoves)
      if i<=2:
        scramble.append("2 ")
      else:
        scramble.append(random.choice(turns))
      moves.remove(randmoves)
      if i != 0:
        moves.append(usedmoves1[-1])

    else:
                                
      randmoves1=random.choice(moves)
      if i>1:
        while randmoves1=="F" and scramble[-4]=="F" and scramble[-2]=="B":
          randmoves1=random.choice(moves)
        while randmoves=="B" and scramble[-4]=="B" and scramble[-2]=="F":
          randmoves1=random.choice(moves)
        while randmoves1=="R" and scramble[-4]=="R" and scramble[-2]=="L":
          randmoves1=random.choice(moves)
        while randmoves1=="L" and scramble[-4]=="L" and scramble[-2]=="R":
          randmoves1=random.choice(moves)
        while randmoves1=="U" and scramble[-4]=="U" and scramble[-2]=="D":
          randmoves1=random.choice(moves)
        while randmoves1=="D" and scramble[-4]=="D" and scramble[-2]=="U":
          randmoves1=random.choice(moves) 
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      moves.remove(randmoves1)
      moves.append(usedmoves[-1])
  cprob=random.randint(1,10)
  if cprob==3:
    moves12=["Uw", "Uw'"]
    scramble.append(random.choice(moves12))
  else:
    colour=random.choice(colours)
    if colour=="yellow":
      scramble.append("Rw2 ")
    elif colour=="green":
      scramble.append("Rw ")
    elif colour=="blue":
      scramble.append("Rw' ")
    elif colour=="red":
      scramble.append("Fw' ")
    elif colour=="orange":
      scramble.append("Fw ")
    chance=random.randint(1,12)
    if chance==3:
      scramble.append("Uw ")
    elif chance==6:
      scramble.append("Uw' ")
    elif chance==9:
      scramble.append("Uw2 ")

  return "".join(scramble)

def get4():
  wide_turns=["F","Fw","B","R","Rw","L","D","U","Uw"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]

  for i in range(40):
                    
    if i % 2 ==0:
      randmoves=random.choice(wide_turns)
      if i>1:
        while randmoves==scramble[-2]:
          randmoves=random.choice(wide_turns)                      
        while randmoves=="F" and scramble[-4]=="F" and scramble[-2]=="B":
          randmoves=random.choice(wide_turns)
        while randmoves=="B" and scramble[-4]=="B" and scramble[-2]=="F":
          randmoves=random.choice(wide_turns)
        while randmoves=="R" and scramble[-4]=="R" and scramble[-2]=="L":
          randmoves=random.choice(wide_turns)
        while randmoves=="L" and scramble[-4]=="L" and scramble[-2]=="R":
          randmoves=random.choice(wide_turns)
        while randmoves=="U" and scramble[-4]=="U" and scramble[-2]=="D":
          randmoves=random.choice(wide_turns)
        while randmoves=="D" and scramble[-4]=="D" and scramble[-2]=="U":
          randmoves=random.choice(wide_turns)
        while randmoves=="Uw" and scramble[-4]=="Uw" and scramble[-2]=="U":
          randmoves=random.choice(wide_turns)
        while randmoves=="Rw" and scramble[-4]=="Rw" and scramble[-2]=="R":
          randmoves=random.choice(wide_turns)
        while randmoves=="Uw" and scramble[-4]=="Uw" and scramble[-2]=="U":
          randmoves=random.choice(wide_turns)
        while randmoves=="U" and scramble[-4]=="U" and scramble[-2]=="Uw":
          randmoves=random.choice(wide_turns)
        while randmoves=="R" and scramble[-4]=="R" and scramble[-2]=="Rw":
          randmoves=random.choice(wide_turns)
        while randmoves=="F" and scramble[-4]=="F" and scramble[-2]=="Fw":
          randmoves=random.choice(wide_turns)
        while randmoves=="B" and scramble[-4]=="B" and scramble[-2]=="Fw":
          randmoves=random.choice(wide_turns)
        while randmoves=="L" and scramble[-4]=="L" and scramble[-2]=="Rw":
          randmoves=random.choice(wide_turns)
        while randmoves=="D" and scramble[-4]=="D" and scramble[-2]=="Uw":
          randmoves=random.choice(wide_turns)
        while randmoves=="Fw" and scramble[-4]=="Fw" and scramble[-2]=="B":
          randmoves=random.choice(wide_turns)
        while randmoves=="Rw" and scramble[-4]=="Rw" and scramble[-2]=="L":
          randmoves=random.choice(wide_turns)
        while randmoves=="Uw" and scramble[-4]=="Uw" and scramble[-2]=="D":
          randmoves=random.choice(wide_turns)
        while randmoves=="Uw" and scramble[-4]=="D" and scramble[-2]=="U":
          randmoves=random.choice(wide_turns)  
        while randmoves=="Uw" and scramble[-4]=="U" and scramble[-2]=="D":
          randmoves=random.choice(wide_turns)
        while randmoves=="U" and scramble[-4]=="D" and scramble[-2]=="Uw":
          randmoves=random.choice(wide_turns)
        while randmoves=="D" and scramble[-4]=="Uw" and scramble[-2]=="U":
          randmoves=random.choice(wide_turns)
        while randmoves=="D" and scramble[-4]=="U" and scramble[-2]=="Uw":
          randmoves=random.choice(wide_turns)
        while randmoves=="U" and scramble[-4]=="Uw" and scramble[-2]=="D":
          randmoves=random.choice(wide_turns)
        while randmoves=="Rw" and scramble[-4]=="R" and scramble[-2]=="L":
          randmoves=random.choice(wide_turns)
        while randmoves=="Rw" and scramble[-4]=="L" and scramble[-2]=="R":
          randmoves=random.choice(wide_turns)
        while randmoves=="R" and scramble[-4]=="L" and scramble[-2]=="Rw":
          randmoves=random.choice(wide_turns)
        while randmoves=="R" and scramble[-4]=="Rw" and scramble[-2]=="L":
          randmoves=random.choice(wide_turns)
        while randmoves=="L" and scramble[-4]=="R" and scramble[-2]=="Rw":
          randmoves=random.choice(wide_turns)
        while randmoves=="L" and scramble[-4]=="Rw" and scramble[-2]=="R":
          randmoves=random.choice(wide_turns)
        while randmoves=="Fw" and scramble[-4]=="F" and scramble[-2]=="B":
          randmoves=random.choice(wide_turns)
        while randmoves=="Fw" and scramble[-4]=="B" and scramble[-2]=="F":
          randmoves=random.choice(wide_turns)
        while randmoves=="F" and scramble[-4]=="B" and scramble[-2]=="Fw":
          randmoves=random.choice(wide_turns)
        while randmoves=="F" and scramble[-4]=="Fw" and scramble[-2]=="B":
          randmoves=random.choice(wide_turns)
        while randmoves=="B" and scramble[-4]=="F" and scramble[-2]=="Fw":
          randmoves=random.choice(wide_turns)
        while randmoves=="B" and scramble[-4]=="Fw" and scramble[-2]=="F":
          randmoves=random.choice(wide_turns)
          
        
      usedmoves.append(randmoves)
      scramble.append(randmoves)
      scramble.append(random.choice(turns))
      wide_turns.remove(randmoves)
      if i != 0:
        wide_turns.append(usedmoves1[-1])
    else:                  
      randmoves1=random.choice(wide_turns)
      if i>1:
        while randmoves1==scramble[-2]:
          randmoves1=random.choice(wide_turns)                      
        while randmoves1=="F" and scramble[-4]=="F" and scramble[-2]=="B":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="B" and scramble[-4]=="B" and scramble[-2]=="F":
          randmoves1=random.choice(wide_turns)
        while randmoves=="R" and scramble[-4]=="R" and scramble[-2]=="L":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="L" and scramble[-4]=="L" and scramble[-2]=="R":
          randmoves1=random.choice(wide_turns)
        while randmoves=="U" and scramble[-4]=="U" and scramble[-2]=="D":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="D" and scramble[-4]=="D" and scramble[-2]=="U":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Uw" and scramble[-4]=="Uw" and scramble[-2]=="U":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Rw" and scramble[-4]=="Rw" and scramble[-2]=="R":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Uw" and scramble[-4]=="Uw" and scramble[-2]=="U":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="U" and scramble[-4]=="U" and scramble[-2]=="Uw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="R" and scramble[-4]=="R" and scramble[-2]=="Rw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="F" and scramble[-4]=="F" and scramble[-2]=="Fw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="B" and scramble[-4]=="B" and scramble[-2]=="Fw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="L" and scramble[-4]=="L" and scramble[-2]=="Rw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="D" and scramble[-4]=="D" and scramble[-2]=="Uw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Fw" and scramble[-4]=="Fw" and scramble[-2]=="B":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Rw" and scramble[-4]=="Rw" and scramble[-2]=="L":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Uw" and scramble[-4]=="Uw" and scramble[-2]=="D":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Uw" and scramble[-4]=="D" and scramble[-2]=="U":
          randmoves1=random.choice(wide_turns)  
        while randmoves1=="Uw" and scramble[-4]=="U" and scramble[-2]=="D":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="U" and scramble[-4]=="D" and scramble[-2]=="Uw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="D" and scramble[-4]=="Uw" and scramble[-2]=="U":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="D" and scramble[-4]=="U" and scramble[-2]=="Uw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="U" and scramble[-4]=="Uw" and scramble[-2]=="D":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Rw" and scramble[-4]=="R" and scramble[-2]=="L":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Rw" and scramble[-4]=="L" and scramble[-2]=="R":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="R" and scramble[-4]=="L" and scramble[-2]=="Rw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="R" and scramble[-4]=="Rw" and scramble[-2]=="L":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="L" and scramble[-4]=="R" and scramble[-2]=="Rw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="L" and scramble[-4]=="Rw" and scramble[-2]=="R":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Fw" and scramble[-4]=="F" and scramble[-2]=="B":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="Fw" and scramble[-4]=="B" and scramble[-2]=="F":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="F" and scramble[-4]=="B" and scramble[-2]=="Fw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="F" and scramble[-4]=="Fw" and scramble[-2]=="B":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="B" and scramble[-4]=="F" and scramble[-2]=="Fw":
          randmoves1=random.choice(wide_turns)
        while randmoves1=="B" and scramble[-4]=="Fw" and scramble[-2]=="F":
          randmoves1=random.choice(wide_turns)
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      wide_turns.remove(randmoves1)
      wide_turns.append(usedmoves[-1])
  return "".join(scramble)

def get5():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  for i in range(60):
                
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
