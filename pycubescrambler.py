import random

class main():

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


  def get_big_cube(n=12):
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

class nxn:

  def get1():
    scramble=main.get1()
    return scramble

  def get2():
    scramble=main.get2()
    return scramble

  def get3():
    scramble=main.get3()
    return scramble
  
  def get4():
    scramble=main.get4()
    return scramble
  
  def get5():
    scramble=main.get_big_cube(5)
    return scramble

  def get6():
    scramble=main.get_big_cube(6)
    return scramble

  def get7():
    scramble=main.get_big_cube(7)
    return scramble

  def get8():
    scramble=main.get_big_cube(8)
    return scramble

  def get9():
    scramble=main.get_big_cube(9)
    return scramble

  def get10():
    scramble=main.get_big_cube(10)
    return scramble

  def get11():
    scramble=main.get_big_cube(11)
    return scramble

  def get12():
    scramble=main.get_big_cube()
    return scramble
  def get_big_cube(n=12):
    scramble=main.get_big_cube(n)
    return scramble
  
  def get_fmc():
    a=main.get3().split()
    list1=["F","F2","F'","B'","B2","B"]
    list2=["R2","R","R'","L","L'","L2"]
    list3=["F","F2","F'"]
    list4=["R2","R","R'"]
    times=0
    while (a[0] in list1 and a[1] in list1) or (a[0] in list3) or (a[-1] in list2 and a[-2] in list2) or (a[-1] in list4):
      if times>3:
        a=main.get3().split()
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


class bld:
  def get3():
    scramble=[]
    scramble3=main.get3()
    scramble.append(scramble3)
    possi=["","Rw ","Rw' ","Rw2 ","Fw ","Fw2 ","Fw' "]
    possi2=["Uw","Uw'","Uw2",""]
    scramble.append(random.choice(possi))
    scramble.append(random.choice(possi2))

    return "".join(scramble)

  def get4():
    scramble=main.get4()
    return scramble
  
  def get5():
    scramble=main.get_big_cube(5)
    return scramble

class side:

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
