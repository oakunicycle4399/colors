from tkinter import *
import random
root = Tk()
root.title("Dictionary")
root.geometry("600x400")
Dictionary = {"color":["red","orange","yellow","green","blue","purple","pink"]}

def colorchange():
    random_no = random.randint(0,6)
    print(Dictionary["color"][random_no])
    root.configure(background = Dictionary["color"][random_no])
    
btn = Button(root,text = "cilck me",command = colorchange)
btn.place(relx = 0.5,rely = 0.5, anchor = CENTER)

root.mainloop()