###DO NOT DELETE UNTIL MORE WORK ON TKTERMINAL IS DONE###
import tkinter as tk
from tkterminal import Terminal
import os

root = tk.Tk()
terminal = Terminal(pady=5, padx=5)
terminal.pack(expand=True, fill='both')
root.mainloop()
