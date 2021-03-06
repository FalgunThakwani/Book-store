from tkinter import *
import backend
from backendOOP import Database

database=Database()

class Window(object):

    def __init__(self,window):

            self.window=window

            self.window.wm_title("BookStore")
            label1=Label(window,text="Title")
            label1.grid(row=0, column =0 )

            label2=Label(window,text="Author")
            label2.grid(row=0 , column =3 )

            label3=Label(window,text="Year")
            label3.grid(row=1 , column = 0)

            label4=Label(self.window,text="ISBN")
            label4.grid(row=1 , column = 3)

            self.title_text=StringVar()
            self.e1=Entry(self.window,textvariable=self.title_text)
            self.e1.grid(row=0 , column=1 )

            self.author_text=StringVar()
            self.e2=Entry(self.window,textvariable=self.author_text)
            self.e2.grid(row=0 , column=4 )


            self.year_text=StringVar()
            self.e3=Entry(self.window,textvariable=self.year_text)
            self.e3.grid(row=1 , column= 1)

            self.isbn_text=StringVar()
            self.e4=Entry(self.window,textvariable=self.isbn_text)
            self.e4.grid(row= 1, column= 4)

            self.l1=Listbox(self.window,height=10,width=55)
            self.l1.grid(row=2,column=0,rowspan=6,columnspan=2)

            self.l1.bind('<<ListboxSelect>>',self.get_selected_row)


            sc=Scrollbar(self.window)
            sc.grid(row=2,column=2,rowspan=6)

            self.l1.configure(yscrollcommand=sc.set)
            sc.configure(command=self.l1.yview)


            b1=Button(self.window,text="View all", width=30,command=self.view_command)
            b1.grid(row=2,column=3,columnspan=3)

            b2=Button(window,text="Search entry", width=30,command=self.search_command)
            b2.grid(row=3,column=3,columnspan=3)

            b3=Button(window,text="Add entry", width=30,command=self.add_command)
            b3.grid(row=4,column=3,columnspan=3)

            b4=Button(window,text="Update selected", width=30,command=self.update_command)
            b4.grid(row=5,column=3,columnspan=3)

            b5=Button(window,text="Delete selected", width=30,command=self.delete_command)
            b5.grid(row=6,column=3,columnspan=3)

            b6=Button(window,text="Close", width=30,command=window.destroy)
            b6.grid(row=7,column=3,columnspan=3)


    def get_selected_row(self,event):


            try:
                self.index=self.l1.curselection()[0]
            except:
                return None
            self.selected_tuple=self.l1.get(self.index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])


    def view_command(self):
        self.l1.delete(0,END)
        for row in database.view():
            self.l1.insert(END,row)

    def search_command(self):
        self.l1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.l1.insert(END,row)

    def add_command(self):
        self.l1.delete(0,END)
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.l1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.view_command()








window=Tk()
Window(window)
window.mainloop()
