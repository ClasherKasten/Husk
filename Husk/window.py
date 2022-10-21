from tkinter import *
from tkinter import messagebox as mb

def openMainWindow():

  window = Tk()

  window.title = 'Husk version 0.3.1'
  window.geometry('500x500')
  window.configure(bg='black')
  window.mainloop()


def setupPassWindow():
###ADD TOP LEVEL ROOT FOR THIS WINDOW###
  passWindow = Tk()

  passWindow.title = 'Set up password?'
  passWindow.geometry('100x100')
  passWindow.configure(bg='black')
  mb.askquestion("askquestion", "Are you sure?")

  passWindow.mainloop()
  

###WINDOW TO OPEN USER AUTHNENTIFICATION PROMPT###
def openPassWindow():
  window = Tk()
  window.title = 'Authentification'
  window.geometry('200x200')
  window.configure(bg='black')
  window.mainloop()
  m
###TESTING WINDOW FUNCTION###
openMainWindow()
setupPassWindow()
