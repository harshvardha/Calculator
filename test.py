# import tkinter as tk
# from tkinter import ttk

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x200")
#         self.overrideredirect(1)
        
#     def startMove(self,event):
#         self.x = event.x
#         self.y = event.y

#     def stopMove(self,event):
#         self.x = None
#         self.y = None

#     def moving(self,event):
#         x = (event.x_root - self.x - self.winfo_rootx() + self.winfo_rootx())
#         y = (event.y_root - self.y - self.winfo_rooty() + self.winfo_rooty())
#         self.geometry("+%s+%s" % (x, y))

#     def exit(self):
#         self.destroy()


# def save():
#     print ('save')
#     return None
# def add():
#     print('add')
#     return None

  

# class MenuBar(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master, bd=1, relief='raised')
#         self.master=master
#         self.configure(background='black',
#                        cursor='hand2')

#         file = tk.Menubutton(self, text='File',
#                              background='black',
#                              foreground='white',
#                              activeforeground='black',
#                              activebackground='white'
#                              )
#         file_menu = tk.Menu(file,tearoff=0)
#         file_menu.add_command(label='save', command=save,
#                               background='black',
#                               foreground='white',
#                               activeforeground='black',
#                               activebackground='white'
#                               )
        
#         file.config(menu=file_menu)
#         file.pack(side='left')

#         edit = tk.Menubutton(self, text='Edit',
#                              background='black',
#                              foreground='white',
#                              activeforeground='black',
#                              activebackground='white'
#                              )
#         edit_menu = tk.Menu(edit,tearoff=0)
#         edit_menu.add_command(label='add', command=add,
#                               background='black',
#                               foreground='white',
#                               activeforeground='black',
#                               activebackground='white'
#                               )

#         edit.config(menu=edit_menu)
#         edit.pack(side='left')

#         close = tk.Button(self, text='X', command=lambda:root.exit(),
#                           background='black',
#                           foreground='white')
#         close.pack(side='right')

# def show():
#     print('show')
#     return None
# def ex_it():
#     print('exit')
#     return None

# class MainFrame(tk.LabelFrame):
#     def __init__(self, master=None):
#         tk.LabelFrame.__init__(self, master, bd=1, relief='raised', text='MainFrame', background='black', foreground='white')
#         self.master=master
#         self.note = tk.Label(self, text='Your typed chars appear here:',
#                              background='black',
#                              foreground='white',
#                              )
#         self.note.grid(column=0, row=0, columnspan=2, sticky='w')
#         self.entry = ttk.Entry(self, style='My.TEntry')
#         self.entry.grid(column=0,row=1,columnspan=3, sticky='ew')
#         self.columnconfigure(0, weight=1)
#         self.b_frame=tk.Frame(self, bg='black')
#         self.b_frame.grid(column=0,row=2,sticky='w')
#         self.sh_b = tk.Button(self.b_frame, text='Show', command=show)
#         self.ex_b = tk.Button(self.b_frame, text='Exit', command=ex_it)
#         self.sh_b.grid(column=0, row=0, sticky='w')
#         self.ex_b.grid(column=1, row=0, sticky='w', padx=5)

# root = App()

# menubar = MenuBar(root)
# menubar.pack(side='top', fill='x')

# mainframe = MainFrame(root)
# mainframe.pack(fill='both', expand=1)

# menubar.bind("<Button-1>", root.startMove)
# menubar.bind("<ButtonRelease-1>", root.stopMove)
# menubar.bind("<B1-Motion>", root.moving)

# style = ttk.Style(root)
# style.element_create("plain.field", "from", "clam")
# style.layout("My.TEntry",
#              [('Entry.plain.field', {'children': [(
#                  'Entry.background', {'children': [(
#                      'Entry.padding', {'children': [(
#                          'Entry.textarea', {'sticky': 'nswe'})],
#                                        'sticky': 'nswe'})], 'sticky': 'nswe'})],
#                                      'border':'2', 'sticky': 'nswe'})])
# style.configure("My.TEntry",
#                  foreground="white",
#                  fieldbackground="grey")

# root.mainloop()

import tkinter
def callback(event):
    print(event.char)
root = tkinter.Tk()
# label = tkinter.Label(root, text="hello")
# label.pack(pady=20)
# label.bind("<Button-1>", callback)
# print(label.bindtags())
# print(root.bindtags())
button1 = tkinter.Button(root)
button1.pack(pady=20)
button1.focus_set()
button1.bind("<Return>", callback)
button2 = tkinter.Button(root)
button2.pack(pady=20)

#button2.focus_set(
root.mainloop()