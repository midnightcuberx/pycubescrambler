from scrambles import nnn

def get_fmc():
  a=nnn.get3().split()
  list1=["F","F2","F'","B'","B2","B"]
  list2=["R2","R","R'","L","L'","L2"]
  list3=["F","F2","F'"]
  list4=["R2","R","R'"]
  times=0
  while (a[0] in list1 and a[1] in list1) or (a[0] in list3) or (a[-1] in list2 and a[-2] in list2) or (a[-1] in list4):
    if times>3:
      a=nnn.get3().split()
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
  scramble=nnn.get1()
  return scramble

def get2():
  scramble=nnn.get2()
  return scramble

def get3():
  scramble=nnn.get3()
  return scramble

def get4():
  scramble=nnn.get4()
  return scramble

def get5():
  scramble=nnn.get_big_cube(5)
  return scramble

def get6():
  scramble=nnn.get_big_cube(6)
  return scramble

def get7():
  scramble=nnn.get_big_cube(7)
  return scramble

def get8():
  scramble=nnn.get_big_cube(8)
  return scramble

def get9():
  scramble=nnn.get_big_cube(9)
  return scramble

def get10():
  scramble=nnn.get_big_cube(10)
  return scramble

def get11():
  scramble=nnn.get_big_cube(11)
  return scramble

def get12():
  scramble=nnn.get_big_cube(12)
  return scramble

def get_big_cube(n=12):
  scramble=nnn.get_big_cube(n)
  return scramble
