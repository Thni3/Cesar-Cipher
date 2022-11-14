import tkinter as tk


root = tk.Tk()

text1 = tk.Text(root, width = 50, height = 25)
text1.pack()

text1.insert(1.0, "Hei")
text1.delete(1.0, 1.1)

a = text1.get(1.0, "end")
text1.insert(1.0, a)


root.mainloop()