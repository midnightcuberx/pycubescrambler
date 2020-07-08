import execjs
from os import path

def trim(func):
    def trimmed_func(*args, **kwargs):
        return func(*args, **kwargs).strip()
    return trimmed_func


curr_dir = path.dirname(path.realpath(__file__))

with open(path.join(curr_dir, 'js/mathlib.js')) as f:
    mathlib = f.read()

with open(path.join(curr_dir, 'js/scramble.js')) as f:
    scramble = f.read()

with open(path.join(curr_dir, 'js/sq1.js')) as f:
    sq1 = f.read()

sq1scrambler   = execjs.compile(mathlib + scramble + sq1)
