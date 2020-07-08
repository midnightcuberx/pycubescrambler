def joinscramble(func):
  def inner(*args,**kwargs):
    scramble=func(*args,**kwargs)
    return "".join(scramble)
  return inner
