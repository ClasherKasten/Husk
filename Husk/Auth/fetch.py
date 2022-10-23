from store import userPass

def fetch():
  
  readData = open('user-data.txt', 'r')

  if readData == userPass:
    ###RUN WHATEVER FUNCTION###
    print('hello')
  elif readData != userPass:
    print('Incorrect password please try again')
  else:
    print('incorrect password')###ADD MORE###

  readData.close()    
  
fetch()