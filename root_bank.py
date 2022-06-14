from tkinter import *




root = Tk()

frame1= Frame(root)
frame2= Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)








lb1 = Label(frame1, text='Acesse sua conta', font= 'arial 25', bg= '#32a852', fg='#050505')
lb2 = Label(frame1, text='Login:', font='arial 25', bg= '#35a852', fg= '#050505')
en1 = Entry(frame1, font= 'arial 18',  bg = '#f7f7f7', fg = '#050505' )
lb3 = Label(frame1, text= 'Senha:', font='arial 25', bg='#35a852', fg='#050505')
en2 = Entry(frame1,font= 'arial 25',  bg = '#f7f7f7', fg = '#050505' )
bt1 = Button(frame1, text="Fazer login!", font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command=lambda: [frame1.pack_forget(), frame2.pack()])

bt8= Button(frame2, text='Voltar', font= 'arial 20', command= lambda: [frame2.pack_forget(), frame1.pack()])

frame1.pack()




lb1.grid(row= 0, column=0, columnspan=4, sticky=NSEW)
lb2.grid(row=1, column=0,sticky=NSEW)
lb3.grid(row=2, column=0,sticky=NSEW)
en1.grid(row=1 ,column=1, sticky=NSEW)
en2.grid(row=2   ,column=1,sticky=NSEW)
bt1.grid(row=3, column= 1, sticky=NSEW)
bt8.grid(row=0, column=0, sticky=NSEW)




























root.mainloop()