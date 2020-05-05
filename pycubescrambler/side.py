import random

def get_clock():
  moves = ["0+","1+","2+","3+","4+","5+","6+","1-","2-","3-","4-","5-"]
  pinOrder = ["UR","DR","DL","UL","U","R","D","L","ALL","U","R","D","L","ALL"]
  last4pins = ["UR", "DR", "DL", "UL"]

  finalScramble = []

  for i in range(14):
      finalScramble.append(pinOrder[i])
      finalScramble.append(random.choice(moves))
      finalScramble.append(" ")


  def sort_l4m():
    l4m=["UR ","DR ","DL ","UL "]
    l4ms=[]
    l3m1=["UR ","DR ","DL "]
    l3m2=["UR ","DR ","UL "]
    l3m3=["DR ","DL ","UL "]
    l3m4=["UR ","DL ","UL "]
    l2m1=["UR ","DR "]
    l2m2=["UR ","DL "]
    l2m3=["UR ","UL "]
    l2m4=["DR ","DL "]
    l2m5=["DR ","UL "]
    l2m6=["DL ","UL "]
    l4m2=[l2m1,l2m2,l2m3,l2m4,l2m5,l2m6]
    l4m3=[l3m1,l3m2,l3m3,l3m4]
    length=random.randint(0,4)
    if length==4:
      for i in range(4):
        l4ms.append(l4m[i])
    elif length==3:
      for i in range(3):
        choice=random.choice(l4m3)
        l4ms.append(choice[i])

    elif length==2:
      for i in range(2):
        choice=random.choice(l4m2)
        l4ms.append(choice[i])
      
    elif length==1:
      l4ms.append(random.choice(l4m))
    elif length==0:
      l4ms.append("")
    return "".join(l4ms)

  last4=sort_l4m()
  finalScramble.append(last4)


  return "".join(finalScramble)
  

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
  U=["U' ","U "]
  for i in range(7):
    scramble=[]
    for y in range(10):
      if y % 2 ==0:
        scramble.append("R")
        scramble.append(random.choice(turns))

      else:
        scramble.append("D")
        scramble.append(random.choice(turns))
    scramble.append(random.choice(U))
    if i == 0:
      a="".join(scramble)
    elif i ==1:
      b = "".join(scramble)
    elif i ==2:
      c="".join(scramble)
    elif i ==3:
      d="".join(scramble)
    elif i==4:
      e="".join(scramble)
    elif i ==5:
      f="".join(scramble)
    elif i ==6:
      g="".join(scramble)

  return"""
{}
{}
{}
{}
{}
{}
{}""".format(a,b,c,d,e,f,g)

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
    tip1=["l","r","b"]
    tip2=["l","r","u"]
    tip3=["r","b","u"]
    tip4=["l","b","u"]
    tip21=["l","r"]
    tip22=["l","b"]
    tip23=["l","u"]
    tip24=["r","b"]
    tip25=["r","u"]
    tip26=["u","b"]
    tips2=[tip21,tip22,tip23,tip24,tip25,tip26]
    tips3=[tip1,tip2,tip3,tip4]
    length=random.randint(1,4)
    if length==4:
      for i in range(4):
        tip.append(tips[i])
        tip.append(random.choice(turns))
    elif length==3:
      for i in range(3):
        choice=random.choice(tips3)
        tip.append(choice[i])
        tip.append(random.choice(turns))
    
    elif length==2:
      for i in range(2):
        choice=random.choice(tips2)
        tip.append(choice[i])
        tip.append(random.choice(turns))
      
    elif length==1:
      tip.append(random.choice(tips))
      tip.append(random.choice(turns))
    elif number==0:
      tip.append("")
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
