from tkinter import *
#from classe_cliente import *
#from classe_conta import *
#from projeto_final import *



root = Tk()

frame1= Frame(root)
frame2= Frame(root)
frame3= Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


#frame1
lb1 = Label(frame1, text='Bem vindo ao Manus Bank', font='Arial 20')
bt1 = Button(frame1, text="Fazer login!", font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command=lambda: [frame1.pack_forget(), frame2.pack()])



#frame2
lb5 = Label(frame2, text='Acesse sua conta', font= 'arial 25', bg= '#32a852', fg='#050505')
lb6 = Label(frame2, text='Login:', font='arial 25', bg= '#35a852', fg= '#050505')
en1 = Entry(frame2, font= 'arial 18',  bg = '#f7f7f7', fg = '#050505' )
lb7 = Label(frame2, text= 'Senha:', font='arial 25', bg='#35a852', fg='#050505')
en2 = Entry(frame2,font= 'arial 25',  bg = '#f7f7f7', fg = '#050505' )
bt2 = Button(frame2, text="Fazer login!", font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command=lambda: [frame2.pack_forget(), frame3.pack()])
bt3= Button(frame2, text='Voltar', font= 'arial 20', command= lambda: [frame3.pack_forget(), frame2.pack()])

#frame3
bt8= Button(frame3, text='Voltar', font= 'arial 20', command= lambda: [frame3.pack_forget(), frame2.pack()])
lb8 = Label(frame3,text='Bem vindo, Mateus!', font='arial 30',bg='#35a852', fg='#050505')
frame1.pack()







#frame1
lb1.grid(row= 0, column=0, columnspan=4, sticky=NSEW)
bt1.grid(row=3, column= 1, sticky=NSEW)


#frame2
lb5.grid(row= 0, column=0, columnspan=4, sticky=NSEW)
lb6.grid(row=1, column=0,sticky=NSEW)
lb7.grid(row=2, column=0,sticky=NSEW)
en1.grid(row=1 ,column=1, sticky=NSEW)
en2.grid(row=2   ,column=1,sticky=NSEW)
bt2.grid(row=3, column= 1, sticky=NSEW)




#frame3
bt8.grid(row=1, column=0, sticky=NSEW)
lb8.grid(row= 0, column=0, columnspan=4, sticky=NSEW)




























root.mainloop()