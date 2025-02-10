import tkinter as tk

window =tk.Tk()


lbl_firstlabel = tk.Label(text='this is a label')
lbl_firstlabel.pack()

btn_firstbutton = tk.Button(text='this is a button')
btn_firstbutton.pack()

ent_firstentry = tk.Entry()
ent_firstentry.pack()

txt_firsttext = tk.Text()
txt_firsttext.pack()


window.mainloop()