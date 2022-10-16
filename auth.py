#VERSION:0.1.1
#AUTHOR: Marshall Burns a.k.a Schooly B
#CONFIG FILE TO START ON FIRST TIME USE OF HUSK 
import getpass, os, pathlib
from time import sleep



def User_Name(): 
  USERNAME = input('What is your user name?' )
  sleep(1)
  print('Greetings ' + (USERNAME) + '...' + ' please enter your password to use Husk')
  getpass.getuser()

def User_Auth():
  sleep(1)
  print('please enter your password')
  userAuth = getpass.getpass()
  print('please re-enter your password')
  confirmAuth = getpass.getpass()
  if confirmAuth == userAuth:
    print('Now logged in to Husk')
  ###ADD FUNCTION TO ACTUALLY US HUSK TERMINAL###
  elif confirmAuth != userAuth:
    print("you've entered the worng information..Plase try again")
    sleep(2)
    User_Auth()
    
User_Name()
User_Auth() 




  

