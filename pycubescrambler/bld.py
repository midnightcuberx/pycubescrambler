import random
import nxn

def get3():
  scramble=[]
  scramble3=nxn.get3()
  scramble.append(scramble3)
  
  possi=["","Rw ","Rw' ","Rw2 ","Fw ","Fw2 ","Fw' "]
  possi2=["Uw","Uw'","Uw2",""]
  scramble.append(random.choice(possi))
  scramble.append(random.choice(possi2))
  

  return "".join(scramble)



def get4():
  scramble=nxn.get4()
  return scramble



def get5():
  scramble=nxn.get5()
  return scramble
