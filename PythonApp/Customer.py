
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql.cursors


class App(Frame):
 # GUI Database Query Frame
 try:
    # class constructor
    def __init__(self, master):

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        frame = tk.Frame(master)
        frame.pack()

        # create widgets for the window
        label = Label(self, text= "CustomerID")
        label.grid(row=0, column =0)
        self.id = Entry(self,name="CustomerID".lower(), font= "courier 12")
        self.id.grid(row=0, column=1, sticky = W + E + N + S, padx=5)

        label = Label(self, text="Name")
        label.grid(row=1, column=0)
        self.name = Entry(self, name="Name".lower(), font="courier 12")
        self.name.grid(row=1, column=1, sticky=W + E + N + S, padx=5)

        label = Label(self, text="Address")
        label.grid(row=2, column=0)
        self.address = Entry(self, name="Address".lower(), font="courier 12")
        self.address.grid(row=2, column=1, sticky=W + E + N + S, padx=5)

        label = Label(self, text="Phone")
        label.grid(row=3, column=0)
        self.phone = Entry(self, name="Phone".lower(), font="courier 12")
        self.phone.grid(row=3, column=1, sticky=W + E + N + S, padx=5)

        self.text = Text(self, width=15, height=8)
        self.text.grid(row=4, column=0, columnspan=2, sticky=W + E + N + S)

        button = Button(self, text="connect to DB", command = self.connect_to_db)
        button.grid(row=5, column=0, sticky=W + E + N + S, padx=5)

        button = Button(self, text="insert customer", command=self.insert)
        button.grid(row=5, column=1, sticky=W + E + N + S, padx=5)

        button = Button(self, text="modify customer", command=self.modify)
        button.grid(row=5, column=2, sticky=W + E + N + S, padx=5)

        button = Button(self, text="delete customer", command=self.delete)
        button.grid(row=5, column=3, sticky=W + E + N + S, padx=5)

        button = Button(self, text="search customer", command=self.search)
        button.grid(row=5, column=4, sticky=W + E + N + S, padx=5)

    # method for connecting to database
    def connect_to_db(self):

        self.con = pymysql.connect(host='mysql.cc.puv.fi',
                                user='e1000656',
                                password='M8v65JXAh6re',
                                db='e1000656_examples',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                 )
        self.cur = self.con.cursor()

    # method for closing db connection
    def close(self):
        self.con.close()

    # method for inserting customer data into db
    def insert(self):

        #retrieve inputs
        id_entry = self.id.get()
        name_entry = self.name.get()
        address_entry = self.address.get()
        phone_entry = self.phone.get()

        self.cur.execute("INSERT INTO pyCustomer(id, name, address, phone)values(%s,%s, %s, %s)",
                                 (id_entry, name_entry, address_entry,phone_entry))

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.address.delete(0, END)
        self.phone.delete(0, END)
        self.close()

    # method for deleting customer data from db
    def delete(self):
        # retrieve inputs
        id_entry = self.id.get()

        self.cur = self.con.cursor()
        sql = "DELETE FROM pyCustomer WHERE id = '%s'"%(id_entry)
        self.cur.execute(sql)
        self.con.commit()

        self.id.delete(0, END)
        self.close()

    # method for modifying customer data in db
    def modify(self):
        # retrieve inputs
        id_entry = self.id.get()
        name_entry = self.name.get()
        address_entry = self.address.get()
        phone_entry = self.phone.get()
        self.cur = self.con.cursor()
        sql = "UPDATE pyCustomer SET name = '%s', address = '%s', phone = '%s' WHERE  id = '%s'" % (name_entry,address_entry, phone_entry,id_entry)
        self.cur.execute(sql)
        #commits transaction
        self.con.commit()


        self.id.delete(0, END)
        self.name.delete(0, END)
        self.address.delete(0, END)
        self.phone.delete(0, END)

        self.close()

    #method for searching customer data from db
    def search(self):
        # retrieve inputs
        id_entry = self.id.get()
        self.cur = self.con.cursor()
        sql = "SELECT * FROM pyCustomer WHERE id = '%s'" % id_entry
        self.cur.execute(sql)
        result = self.cur.fetchall()
        #self.text.delete(0, END)
        #display search result in a text widget
        self.text.insert(INSERT, result)

 except Exception as e:
        print("Error :" + str(e))

# Here we create the main window
root = Tk()
root.title("Customer Info Window")
app = App(root)
root.mainloop()
