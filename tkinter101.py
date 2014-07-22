from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='Here i am =))', message='hello, my darlin =*')
    
window = Tk()
button = Button(window, text='Top secret!! For Sofya only', command=reply)
button.pack()
window.mainloop()