import random
from scrambles import nnn

def get3():
  
  scramble=[]
  scramble3=nnn.get3()
  scramble.append(scramble3)
  possi=["","Rw ","Rw' ","Rw2 ","Fw ","Fw2 ","Fw' "]
  possi2=["Uw","Uw'","Uw2",""]
  scramble.append(random.choice(possi))
  scramble.append(random.choice(possi2))
  return "".join(scramble)

def get4():
  scramble=nnn.get4()
  return scramble

def get5():
  scramble=nnn.get_big_cube(5)
  return scramble
