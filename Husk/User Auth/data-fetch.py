import getpass
from time import sleep


def Initial_Pass():
  initialPass = input('Would you like to set up a password to use within the terminal?' '\n')
  if initialPass == 'y':
    Initial_Pass_Setup()
  elif initialPass == 'n':
    print('Ok. you can set up a password anytime by going to the preferences section and clicking "setup password" ')
  else:
    print('Please enter a valid response')
    sleep(2)
    Initial_Pass()



def test():
  
  print('hello world')
  
  
  
def Initial_Pass_Setup():
  userPass = getpass.getpass("please enter the password you would like to use")
  confirmPass = getpass.getpass("please re-enter the password")
  if userPass == confirmPass:
    with open('user-data.txt','w', encoding='utf-8') as p:
      p.write(userPass)


def Reg_Pass_Prompt():
  userPass = getpass.getpass("please enter the password you would like to use")
  
  
  
def Retrieve_Pass(userPass):
  userData = open('user-data.txt', 'r')
  userData.close()
  
  if userData == userPass:
    ###RUN WHATEVER FUNCTION###
    test()
  elif userData != userPass:
    print('Incorrect password please try again')
  else:
    print('incorrect password')###ADD MORE###
      

    
###CALLING INITIAL PASS REQUEST###
Initial_Pass()
Retrieve_Pass(userPass)