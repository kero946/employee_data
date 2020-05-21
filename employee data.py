from tkinter import *
from tkinter import ttk
from tkinter import messagebox

f = Tk()

fnt = "tahoma 25 bold"
bg  = "#ffcd4f"
bgtxt  = "#ffffff"
fg  = "#332501"
fw  = 700
fh  = 500
x   = (f.winfo_screenwidth() - fw) / 2
y   = (f.winfo_screenheight() - fh) / 2 - 40
pad = 10

f.geometry('%dx%d+%d+%d' % ( fw ,fh, x, y) )
f.title('employee data')
f.config(bg=bg)
f.iconbitmap('icon.ico')

Label(f, text='Employee Data',bg='#ffb800',fg=fg, font=fnt ).pack(pady=pad)

frame = Frame(f, bg=bg)
frame.pack(pady=pad)

Label(frame, text='code: ',bg=bg,fg=fg, font=fnt).grid(row=0,column=0)
Label(frame, text='name: ',bg=bg,fg=fg, font=fnt).grid(row=1,column=0)
Label(frame, text='address: ',bg=bg,fg=fg, font=fnt).grid(row=2,column=0)

svcode    = StringVar()
svname    = StringVar()
svaddress = StringVar()

txtcode    = Entry(frame, bg=bgtxt, fg=fg,font=fnt, textvariable=svcode )
txtname    = Entry(frame, bg=bgtxt, fg=fg,font=fnt, textvariable=svname )
txtaddress = Entry(frame, bg=bgtxt, fg=fg,font=fnt, textvariable=svaddress )

txtcode.grid(row=0,column=1,pady=pad)
txtname.grid(row=1,column=1,pady=pad)
txtaddress.grid(row=2,column=1,pady=pad)

def creat():
    if svcode.get().strip()=="":
        messagebox.showinfo('','code is empty !!!')
        txtcode.focus()
    elif svname.get().strip()=="":
        messagebox.showinfo('','name is empty !!!')
        txtname.focus()
    elif svaddress.get().strip()=="":
        messagebox.showinfo('','address is empty !!!')
        txtaddress.focus()
    else:
        filename = svname.get() + '.txt'
        f = open("df/filename" , 'w+')
        f.write('Code: ' + svcode.get() + '\n')
        f.write('name: ' + svname.get() + '\n')
        f.write('address: ' + svaddress.get() + '\n')
        f.close()
        messagebox.showinfo('','Creating successfully')



btns = ttk.Style()
btns.configure('TButton', font=fnt,pady=pad,padding=pad)
ttk.Button(f, text='Creat new file now',command=creat).pack(pady=pad)
ttk.Button(f, text='exit now', command=f.destroy).pack(pady=pad)



f.mainloop()
