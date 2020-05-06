import random

def get_fmc():
  moves = ["F","B","R","L","U","D"]
  turns = [" ","2 ","' "]
  scramble = ["R","' ","U","' ","F"," "]
  usedmoves=[]
  usedmoves1=[]
  for i in range(20):
                            
    if i % 2 ==0:
      randmoves=random.choice(moves)                      
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
      if i<=4:
        ok=random.randint(1,3)
        if ok!=1:
          scramble.append("2 ")
        else:
          scramble.append(random.choice(turns))
          
      else:
        scramble.append(random.choice(turns))
      moves.remove(randmoves)
      if i != 0:
        moves.append(usedmoves1[-1])

    else:
                                
      randmoves1=random.choice(moves)
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
      if i==19:
        while randmoves1=="F":
          randmoves1=random.choice(moves)
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      moves.remove(randmoves1)
      moves.append(usedmoves[-1])
  scramble.append("F' U R")
  return "".join(scramble)


def get2(): 
  moves = ["F","R","U"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  for i in range(10):
                
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



def get3():
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
      if i<=4:
        ok=random.randint(1,3)
        if ok!=1:
          scramble.append("2 ")
        else:
          scramble.append(random.choice(turns))
          
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
  return "".join(scramble)


def get4():
  moves = ["F","B","R","L","U","D"]
  wide_turns=["F","Fw","B","R","Rw","L","D","U","Uw"]
  turns = [" ","2 ","' "]
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
      if i<=4:
        ok=random.randint(1,3)
        if ok!=1:
          scramble.append("2 ")
        else:
          scramble.append(random.choice(turns))
          
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
  usedmoves=[]
  usedmoves1=[]
  wide_turns.remove(randmoves1)
  usedmoves1.append(randmoves1)
  for i in range(25):
                    
    if i % 2 ==0:
      randmoves=random.choice(wide_turns)
      if randmoves in moves and scramble[-2] in moves and scramble[-4] in moves:
        randmoves=random.choice(wide_turns)

      while randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1:
        randmoves=random.choice(wide_turns)
      while randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2:
        randmoves=random.choice(wide_turns)
      while randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3:
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
      while randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1:
        randmoves1=random.choice(wide_turns)
      while randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2:
        randmoves1=random.choice(wide_turns)
      while randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3:
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
  list1=["U","D","Uw","Dw"]
  list2=["R","L","Lw","Rw"]
  list3=["F","B","Fw","Bw"]
  for i in range(60):
                
    if i % 2 ==0:
      randmoves=random.choice(moves)
      if i>1:
        while randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1:
          randmoves=random.choice(moves)
        while randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2:
          randmoves=random.choice(moves)
        while randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3:
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
        while randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1:
          randmoves1=random.choice(moves)
        while randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2:
          randmoves1=random.choice(moves)
        while randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3:
          randmoves1=random.choice(moves)

      randmoves1=random.choice(moves)
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      moves.remove(randmoves1)
      moves.append(usedmoves[-1])
  return "".join(scramble)


def get6():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw"]
  list2=["R","L","Lw","Rw","3Rw"]
  list3=["F","B","Fw","Bw","3Fw"]
  for i in range(80):
                
    if i % 2 ==0:
      randmoves=random.choice(moves)
      if i>1:
        while randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1:
          randmoves=random.choice(moves)
        while randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2:
          randmoves=random.choice(moves)
        while randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3:
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
        while randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1:
          randmoves1=random.choice(moves)
        while randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2:
          randmoves1=random.choice(moves)
        while randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3:
          randmoves1=random.choice(moves)

      randmoves1=random.choice(moves)
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      moves.remove(randmoves1)
      moves.append(usedmoves[-1])
  return "".join(scramble)


def get7():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw"]
  turns = [" ","2 ","' "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw"]
  for i in range(100):
                
    if i % 2 ==0:
      randmoves=random.choice(moves)
      if i>1:
        while randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1:
          randmoves=random.choice(moves)
        while randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2:
          randmoves=random.choice(moves)
        while randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3:
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
        while randmoves1 in list1 and scramble[-2] in list1 and scramble[-4] in list1:
          randmoves1=random.choice(moves)
        while randmoves1 in list2 and scramble[-2] in list2 and scramble[-4] in list2:
          randmoves1=random.choice(moves)
        while randmoves1 in list3 and scramble[-2] in list3 and scramble[-4] in list3:
          randmoves1=random.choice(moves)

      randmoves1=random.choice(moves)
      scramble.append(randmoves1)
      usedmoves1.append(randmoves1)
      scramble.append(random.choice(turns))
      moves.remove(randmoves1)
      moves.append(usedmoves[-1])
  return "".join(scramble)

