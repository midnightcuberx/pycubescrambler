import random
from . import main, joinscramble,bldify

@joinscramble("")
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

@joinscramble("")
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

@joinscramble("")
def get3(scramtype="3x3"):
  def get3():
    scramble=main.get3()
    return scramble
  
  @bldify(3)
  def get3bld():
    scramble=main.get3()
    return scramble

  def fmc():
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

  if scramtype=="3x3":
    return get3()
  
  elif scramtype=="bld":
    return get3bld()
  
  elif scramtype=="fmc":
    return fmc()
  
  else:
    raise ValueError("That type of scramble does not exist")


@joinscramble("")
def get4(scramtype="4x4"):
  def get4():
    scramble=main.get4()
    return scramble
  
  @bldify(4)
  def get4bld():
    scramble=main.get4()
    return scramble
  
  if scramtype=="4x4":
    return get4()
  
  elif scramtype=="bld":
    return get4bld()

  else:
    raise ValueError("That type of scramble does not exist")

@joinscramble("")
def get5(scramtype="5x5"):
  def get5():
    scramble=main.big(5)
    return scramble
  
  @bldify(5)
  def get5bld():
    scramble=main.big(5)
    return scramble

  if scramtype=="5x5":
    return get5()
  
  elif scramtype=="bld":
    return get5bld()

  else:
    raise ValueError("That type of scramble does not exist")


@joinscramble("")
def get6():
  scramble=main.big(6)
  return scramble

@joinscramble("")
def get7():
  scramble=main.big(7)
  return scramble

@joinscramble("")
def get8():
  scramble=main.big(8)
  return scramble

@joinscramble("")
def get9():
  scramble=main.big(9)
  return scramble

@joinscramble("")
def get10():
  scramble=main.big(10)
  return scramble

@joinscramble("")
def get11():
  scramble=main.big(11)
  return scramble

@joinscramble("")
def get12():
  scramble=main.big(12)
  return scramble

@joinscramble("")
def get_big_cube(n=12,scramtype="big"):
  def big():
    scramble=main.big(n)
    return scramble

  @bldify(n)
  def bld():
    scramble=main.big(n)
    return scramble
  
  if scramtype=="big":
    return big()
  
  elif scramtype=="bld":
    return bld()

  else:
    raise ValueError("That type of scramble does not exist")
