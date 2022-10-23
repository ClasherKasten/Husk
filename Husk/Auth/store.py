
import getpass
from time import sleep

def Initial_Pass():
  initialPass = input('Would you like to set up a password to use within the terminal?' '\n')
  if initialPass == 'y':
    userPass = getpass.getpass("please enter the password you would like to use")
    confirmPass = getpass.getpass("please re-enter the password")
    if userPass == confirmPass:
      print('Password confirmed')
      with open('user-data.txt','w', encoding='utf-8') as p:
        p.write(userPass)
    elif userPass != confirmPass:
      print('The entered password did not match please ty again')
      sleep(2)
      Initial_Pass()
    else: 
      print('Error')
  elif initialPass == 'n':
    print('Ok. you can set up a password anytime by going to the preferences section and clicking "setup password" ')
  else:
    print('Please enter a valid response')
    sleep(2)
    Initial_Pass()





def Reg_Pass_Prompt():
  userPass = getpass.getpass("please enter the password you would like to use")
  
  
  
Initial_Pass()