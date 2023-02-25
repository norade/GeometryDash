import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('900x600+50+50')
root.resizable(False, False)
bg = tk.PhotoImage(file = "bg.png")
label1 = tk.Label( root, image = bg)
label1.place(x = 0, y = 0)
  

root.mainloop()