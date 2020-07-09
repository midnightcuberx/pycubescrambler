from . import main, joinscramble, bldify

@joinscramble
@bldify(3)
def get3():
  scramble=main.get3()
  return scramble

@joinscramble
@bldify(4)
def get4():
  scramble=main.get4()
  return scramble

@joinscramble
@bldify(5)
def get5():
  scramble=main.get5()
  return scramble

@joinscramble
@bldify(6)
def get6():
  scramble=main.big(6)
  return scramble

@joinscramble
@bldify(7)
def get7():
  scramble=main.big(7)
  return scramble

@joinscramble
@bldify(8)
def get8():
  scramble=main.big(8)
  return scramble

@joinscramble
@bldify(9)
def get9():
  scramble=main.big(9)
  return scramble

@joinscramble
@bldify(10)
def get10():
  scramble=main.big(10)
  return scramble

@joinscramble
@bldify(11)
def get11():
  scramble=main.big(11)
  return scramble

@joinscramble
@bldify(12)
def get12():
  scramble=main.big(12)
  return scramble
