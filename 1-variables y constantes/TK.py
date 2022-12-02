#TKinter

import tkinter as tk

root = tk.Tk()

root.title("Ventana")
root.iconphoto(False, tk.PhotoImage(file='C:/Users/xtorramade/Documents/Clases/1-variables y constantes/1434.png'))
root.resizable(True, True)
frame = tk.Frame(root, width=880, height= 620) 
frame.pack()
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.mainloop()
