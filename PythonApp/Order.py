import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql.cursors
import time


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
        label = Label(self, text= "OrderID")
        label.grid(row=0, column =0)
        self.id = Entry(self,name="OrderID".lower(), font= "courier 12")
        self.id.grid(row=0, column=1, sticky = W + E + N + S, padx=5)


        label = Label(self, text="CustomerID")
        label.grid(row=1, column=0)
        self.customer_id = Entry(self, name="CustomerID".lower(), font="courier 12")
        self.customer_id.grid(row=1, column=1, sticky=W + E + N + S, padx=5)

        label = Label(self, text="ProductID")
        label.grid(row=2, column=0)
        self.product_id = Entry(self, name="ProductID".lower(), font="courier 12")
        self.product_id.grid(row=2, column=1, sticky=W + E + N + S, padx=5)

        label = Label(self, text="Amount")
        label.grid(row=3, column=0)
        self.amount = Entry(self, name="Amount".lower(), font="courier 12")
        self.amount.grid(row=3, column=1, sticky=W + E + N + S, padx=5)

        self.text = Text(self, width=15, height=8)
        self.text.grid(row=4, column=0, columnspan=2, sticky=W + E + N + S)

        button = Button(self, text="connect to DB", command = self.connect_to_db)
        button.grid(row=5, column=0, sticky=W + E + N + S, padx=5)

        button = Button(self, text="insert order", command=self.insert)
        button.grid(row=5, column=1, sticky=W + E + N + S, padx=5)

        button = Button(self, text="modify order", command=self.modify)
        button.grid(row=5, column=2, sticky=W + E + N + S, padx=5)

        button = Button(self, text="delete order", command=self.delete)
        button.grid(row=5, column=3, sticky=W + E + N + S, padx=5)

        button = Button(self, text="search order", command=self.search)
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
        customer_id_entry = self.customer_id.get()
        product_id_entry = self.product_id.get()
        amount_entry = self.amount.get()

        order_date = time.strftime('%d %B %Y', time.localtime())

        self.cur.execute("INSERT INTO pyOrders(id, date, customerId, productId, productAmount)values(%s,%s, %s, %s, %s)",
                                 (id_entry, order_date, customer_id_entry, product_id_entry,amount_entry))

        self.id.delete(0, END)
        self.customer_id.delete(0, END)
        self.product_id.delete(0, END)
        self.amount.delete(0, END)


        self.close()

    # method for deleting customer data from db
    def delete(self):
        # retrieve inputs
        id_entry = self.id.get()

        self.cur = self.con.cursor()
        sql = "DELETE FROM pyOrders WHERE id = '%s'"%(id_entry)
        self.cur.execute(sql)
        self.con.commit()

        self.id.delete(0, END)
        self.close()


    # method for modifying customer data in db
    def modify(self):
        # retrieve inputs
        id_entry = self.id.get()
        customer_id_entry = self.customer_id.get()
        product_id_entry = self.product_id.get()
        amount_entry = self.amount.get()

        self.cur = self.con.cursor()
        sql = "UPDATE pyOrders SET customerId = '%s', productId = '%s', productAmount = '%s' WHERE  id = '%s'" % (customer_id_entry,product_id_entry, amount_entry,id_entry)
        self.cur.execute(sql)
        #commits transaction
        self.con.commit()

        self.id.delete(0, END)
        self.customer_id.delete(0, END)
        self.product_id.delete(0, END)
        self.amount.delete(0, END)

        self.close()

    #method for searching customer data from db
    def search(self):
        # retrieve inputs
        id_entry = self.id.get()
        self.cur = self.con.cursor()
        sql = "SELECT * FROM pyOrders WHERE id = '%s'" % id_entry
        self.cur.execute(sql)
        result = self.cur.fetchall()
        #self.text.delete(0, END)
        #display search result in a text widget
        self.text.insert(INSERT, result)

        self.id.delete(0, END)

        self.close()

 except Exception as e:
        print("Error :" + str(e))

# Here we create the main window
root = Tk()
root.title("Customer Info Window")
app = App(root)
root.mainloop()
