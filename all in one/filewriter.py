import tkinter as tk

root = tk.Tk()

root.geometry("400x300")
root.title("File Writer")

def save():
    filename = txtb1.get('1.0', 'end-1c')
    towrite = txtb2.get('1.0', tk.END)
    file = open(filename, 'w')
    file.write(towrite)
    file.close()

lable = tk.Label(root, text="File Writer", font=('Arial', 15))
lable.pack(padx=20, pady=20)

txtb1 = tk.Text(root, height=1, font=('Arial', 15))
txtb1.insert('1.0', 'enter the filename whit extension')
txtb1.pack(pady=10, padx=10)

txtb2 = tk.Text(root, height=4, font=('Arial', 15))
txtb2.insert('1.0', 'enter what you want to write to the file')
txtb2.pack(pady=10, padx=10)

btn1 = tk.Button(root, text="save", font=('Arial', 15), command=save)
btn1.pack(pady=12, padx=12)
