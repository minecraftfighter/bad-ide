import tkinter as tk

root = tk.Tk()

root.geometry("500x400")
root.title("file reader")

def read():
    filename = txtb1.get('1.0', 'end-1c')
    print(filename)
    file = open(filename, 'r+')
    ou = file.read()
    file.close()
    out.insert('1.0', ou)

lable = tk.Label(root, text="file reader", font=('Arial', 15))
lable.pack(padx=10, pady=10)

txtb1 = tk.Text(root, height=1, font=('Arial', 15))
txtb1.insert('1.0', 'enter the filename to open whit extension')
txtb1.pack(padx=12, pady=12)

out = tk.Text(root, height=4, font=('Arial', 15))
out.pack(padx=12, pady=12)

btn1 = tk.Button(root, text="read", font=('Arial', 15), command=read)
btn1.pack(padx=12, pady=12)

root.mainloop()

