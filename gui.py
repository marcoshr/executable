"""
FOLLOWING THIS TUTORIAL NOW:
https://likegeeks.com/es/ejemplos-de-la-gui-de-python/
"""
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Marcos Hernández App")
window.geometry("500x400")

# Couldn't use .pack with.geometry
"""
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="First")
tab_control.add(tab2, text="Second")
lbl1 = Label(tab1, text="label1", padding=[50, 50, 50, 50])
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text="label2")
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill="both")
"""
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="New")
new_item.add_separator()
new_item.add_command(label="Edit")
menu.add_cascade(label="File", menu=new_item)
window.config(menu=menu)

style = Style()
style.theme_use("default")
style.configure("orange.Horizontal.TProgressbar", background="orange")
bar = Progressbar(window, length=300, style="orange.Horizontal.TProgressbar")
bar["value"] = 70
bar.grid(column=0, row=0)

combo = Combobox(window)
combo["values"]= (1, 2, 3, 4, 5, "Text")
combo.current(1)
combo.grid(column=0, row=1)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=0, row=2)
def clicked_2():
    #messagebox.showinfo("Message title", "Message content")
    #messagebox.showwarning("Message title", "Message content")
    messagebox.showerror("Message title", "Message content")
btn = Button(window, text="Click here", command=clicked_2)
btn.grid(column=0, row=3)

lbl = Label(window, text="Hola", font=("Times New Roman", 18))
lbl.grid(column=0, row=4)
txt = Entry(window, width=10, state="disabled")
txt.focus()
txt.grid(column=0, row=5)

def clicked():
    #res = "Welcome to " + txt.get()
    #lbl.configure(text=res)
    import smtp_server

btn = Button(window, text="Enviarme correo a mi mismo", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()