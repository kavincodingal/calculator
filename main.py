import tkinter as tk
root=tk.Tk()
root.title("top level window")
root.geometry("600x600")


def top():
    t=tk.Toplevel()
    t.title("clild window")
    t.geometry("400x500")
    def add():
        num1=int(e1.get())
        num2=int(e2.get())
        total=num1+num2
        r.config(text="sum= "+str(total))
    t.config(bg="cyan")
    l2=tk.Label(t,text="enter  the first number",font=("Arial",20))
    l2.pack(pady=15)
    e1=tk.Entry(t)
    e1.pack(pady=15)
    l3=tk.Label(t,text="enter  the second number",font=("Arial",20))
    l3.pack(pady=15)
    e2=tk .Entry(t)
    e2.pack(pady=15)
    b=tk.Button(t,text="add",command=add)
    b.pack(pady=15)
    r=tk.Label(t,text="sum= ",font=("Arial",20))
    r.pack(pady=15)
    t.mainloop()


l1=tk.Label(root,text="this is parent window",font=("Arial",20))
l1.pack(pady=15)

b1=tk.Button(root,text="click for opening top level window",command=top)
b1.pack(pady=15)

root.mainloop()