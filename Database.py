import sqlite3
import random
from tkinter import *

# Backend

#con = sqlite3.connect("student.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS outofstock_meds (id INTEGER PRIMARY KEY, Name text, Date DateTime, UNIQUE(Name))")
#con.commit()
#con.close()


def outofstock_meds(ID, Name):
    """
        Ideally, the pharmacy would remove that medicine from the out of stock table once its back in stock.
        For the time being, I am dropping any table if it already exists to avoid any error.

        For example, consider a medicine got out of stock, Quantity is 0 and the outofstock table was created.
        The next time I run this program, it will see a stock of 0 and try to add the same medicine again, but this
        would not be the case in the real work where pharmacy would have simply removed the medicine from the out of stock table
    """
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS outofstock_meds")
    cur.execute("CREATE TABLE IF NOT EXISTS outofstock_meds (id INTEGER PRIMARY KEY, Name text, Date DateTime, UNIQUE(Name))")
    print(f"inserting {ID, Name}")
    cur.execute("INSERT OR IGNORE INTO outofstock_meds VALUES(?, ?, datetime('now', 'localtime'))", (ID, Name))
    con.commit()
    con.close()


def authenticate_login(u, p):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID = ?", (u,))
    rows = cur.fetchone()
    if rows[0] == u and rows[2] == p:
        status = True
    else:
        status = False
    con.close()
    return status


# Change 'like' to exact match
def get_price(name):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE Name like ?", (name + '%',))
    price = cur.fetchall()
    con.close()
    return price[0][3]


def get_quantity(Name):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE Name like ?", (Name+'%',))
    rec = cur.fetchall()
    con.close()
    return rec[0][2]


# Change 'like' to exact match
def get_id(Name):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE Name like ?", (Name+'%',))
    rec = cur.fetchall()
    con.close()
    return rec[0][0]


def transact(rows, username, root2):
    global bill
    bill = dict()
    meds = []
    for name in rows:
        meds.append(name)

    for element in meds:
        if element in bill:
            bill[element] += 1
        else:
            bill[element] = 1

    global t_id
    print(bill)
    t_id = random.randint(10000, 20000)
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    for item in bill.items():
        cur.execute("INSERT INTO transactions VALUES (?,?,?,?,datetime('now', 'localtime'))", (t_id, get_id(item[0]), username, item[1]))

    con.commit()
    con.close()
    Receipt(root2)


def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines order by Name asc")
    rows = cur.fetchall()
    con.close()
    return rows


def searchData(Name=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE Name like ?", (Name + '%',))
    rows = cur.fetchall()
    cur.execute("SELECT * FROM outofstock_meds order by Name asc")
    out_of_stock = cur.fetchall()
    for i, x in enumerate(rows):
        for y in out_of_stock:
            print(x, y)
            if x[1] == y[1]:
                del rows[i]

    print("Out of stock meds", out_of_stock)
    print("Search results", rows)
    con.close()
    return rows


def Receipt(root2):
    R = Toplevel(root2)
    txtReceipt = Text(R, width=100, height=120, bg="white", bd=2, font=('arial', 17, 'bold'), fg="black")
    txtReceipt.grid(row=0, column=0)

    txtReceipt.insert(END, f'Transaction ID :\t\t {t_id}')
    txtReceipt.insert(END, f'\n\nMedicines:\t\t\t\t Price:\t\t Quantity:\t\t Subtotal:')
    txtReceipt.insert(END, '\n--------------------------------------------------------------------------------------------------------------------------------')
    Total = 0
    for item in bill.items():
        P = get_price(item[0])
        Total += P * item[1]
        txtReceipt.insert(END, f'\n{item[0]}\t\t\t\t Rs. {P}\t\t   {item[1]}\t\t Rs. {P*item[1]}')

    txtReceipt.insert(END, f'\n\n\t\t\t\t\t\t\t      Total: Rs. {Total}')

    txtReceipt.insert(END, f'\n\n\n\n\n\n\n\nContact number\t:\t\t9876543210\nEmail ID\t\t:\tbluecircle@snu.edu.in')
