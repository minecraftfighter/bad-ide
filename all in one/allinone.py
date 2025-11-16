import tkinter as tk

root = tk.Tk()

root.geometry("500x400")
root.title("All in one")

def read():
    with open("filereader.py") as file:
        exec(file.read())

def write():
    with open("filewriter.py") as file:
        exec(file.read())

lable = tk.Label(root, text="All in one", font=('Arial', 15))
lable.pack(padx=10, pady=10)

btn1 = tk.Button(root, text="start file reader", font=('Arial', 15), command=read)
btn1.pack(padx=10, pady=10)

btn2 = tk.Button(root, text="start file writer", font=('Arial', 15), command=write)
btn2.pack(padx=10, pady=10)

root.mainloop()
