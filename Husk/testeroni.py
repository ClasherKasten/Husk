###TEST/DEBUG ENVIORNMENT SPECIFICALLY FOR 'KEY INPUTS'###


import readchar

key = readchar.readkey()

def test():
  k = input('click a key')
  from readchar import readkey, key
  if k == 'a':
    print('hello world')
  elif k == key.UP:
    print('up')
  elif k == key.DOWN:
    print('down')
  elif k == key.LEFT:
    print('left')
  elif k == key.RIGHT:
    print('right')
  elif k == 'bk':
    print('back')

  

test()