import tkinter as tk


root = tk.Tk()
root.title("Das is QUAKE!")
root.geometry("900x450+300+250")
root.resizable(width=False, height=False)

bg_image = tk.PhotoImage(file='background.png')
icon = tk.PhotoImage(file='rifle.png')

root.iconphoto(False, icon)

label1 = tk.Label(root, image=bg_image)
label1.place(x=0, y=0)

root.mainloop()
