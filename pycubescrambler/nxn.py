import random

def get_fmc():
  def main_scram():
    moves = ["F","B","R","L","U","D"]
    turns = [" ","2 ","' ","2 "]
    scramble = []
    usedmoves=[]
    usedmoves1=[]
    for i in range(20):
                              
      if i % 2 ==0:
        randmoves=random.choice(moves)
        if i==0:
          while randmoves=="F":
            randmoves=random.choice(moves)
            
        elif i>1:                      
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
            

        scramble.append(random.choice(turns))
        moves.remove(randmoves)
        if i != 0:
          moves.append(usedmoves1[-1])

      else:
                                  
        randmoves1=random.choice(moves)
        if i==1:
          while scramble[-2]=="B" and randmoves1=="F":
            randmoves1=random.choice(moves)
          
        elif i>1:
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

  a=main_scram().split()
  list1=["F","F2","F'","B'","B2","B"]
  list2=["R2","R","R'","L","L'","L2"]
  list3=["F","F2","F'"]
  list4=["R2","R","R'"]
  times=0
  while (a[0] in list1 and a[1] in list1) or (a[0] in list3) or (a[-1] in list2 and a[-2] in list2) or (a[-1] in list4):
    if times>3:
      a=main_scram.split()
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
  turns = [" ","2 ","' ","2 "]
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
  turns = [" ","2 ","' ","2 "]
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
  return "".join(scramble)



def get5():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw"]
  turns = [" ","2 ","' ","2 "]
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
        if (randmoves in list1 and scramble[-2] in list1 and scramble[-4] in list1) or (randmoves in list2 and scramble[-2] in list2 and scramble[-4] in list2) or (randmoves in list3 and scramble[-2] in list3 and scramble[-4] in list3):
          while randmoves==scramble[-4]:
            randmoves=random.choice(moves)
        if i > 2:
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





def get6():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw"]
  turns = [" ","2 ","' ","2 "]
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



def get7():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw"]
  turns = [" ","2 ","' ","2 "]
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


def get8():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw","4Uw","4Rw","4Fw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw","4Uw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw","4Rw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw","4Fw"]
  for i in range(120):
                
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

def get8():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw","4Uw","4Rw","4Fw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw","4Uw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw","4Rw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw","4Fw"]
  for i in range(120):
                
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

def get8():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw","4Uw","4Rw","4Fw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw","4Uw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw","4Rw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw","4Fw"]
  for i in range(120):
                
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


def get9():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw","4Uw","4Rw","4Fw","4Dw","4Lw","4Bw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw","4Uw","4Dw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw","4Rw","4Lw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw","4Fw","4Bw"]
  for i in range(120):
                
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

def get10():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw","4Uw","4Rw","4Fw","4Dw","4Lw","4Bw","5Rw","5Fw","5Uw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw","4Uw","4Dw","5Uw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw","4Rw","4Lw","5Rw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw","4Fw","4Bw","5Fw"]
  for i in range(120):
                
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

def get11():
  moves = ["F","Fw","B","Bw","R","Rw","L","Lw","D","Dw","U","Uw","3Uw","3Rw","3Fw","3Bw","3Dw","3Lw","4Uw","4Rw","4Fw","4Dw","4Lw","4Bw","5Rw","5Fw","5Uw","5Dw","5Lw","5Bw"]
  turns = [" ","2 ","' ","2 "]
  scramble = []
  usedmoves=[]
  usedmoves1=[]
  list1=["U","D","Uw","Dw","3Uw","3Dw","4Uw","4Dw","5Uw","5Dw"]
  list2=["R","L","Lw","Rw","3Rw","3Lw","4Rw","4Lw","5Rw","5Lw"]
  list3=["F","B","Fw","Bw","3Fw","3Bw","4Fw","4Bw","5Fw","5Bw"]
  for i in range(120):
                
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


def get_big_cube(n=12):
  moves = ["F","B","R","L","U","D","Uw","Dw","Fw","Bw","Rw","Lw"]
  turns = [" ","2 ","' ","2 "]
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
  
  for i in range(n*15):
                
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
