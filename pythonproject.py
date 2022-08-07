from tkinter import*
import random
import time
import sqlite3

root = Tk()
root.geometry("890x580+0+0")
root.title("Restraunt Billing System")


Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="My Restauraunt",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*30
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.18)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)*.12)
    Service="Rs.",str('%.2f'% Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)
    OverAllCost1 = 0
    if couponcode.get() !="offer10":
        OverAllCost1 ="Rs.",str( PayTax + Totalcost + Ser_Charge)
        OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    else:
        OverAllCost1 ="Rs.",str( PayTax + Totalcost + Ser_Charge)
        OverAllCost="Rs.",str( PayTax - 0.10*PayTax+ Totalcost - 0.10*Totalcost + Ser_Charge -0.10*Ser_Charge)


    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(OverAllCost1)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")
    couponcode.set("")


#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()
couponcode = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="brown",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="yellow" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text=" French Fries ",fg="blue",bd=10,anchor='w')
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="green" ,justify='right')
txtfries.grid(row=2,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch ",fg="blue",bd=10,anchor='w')
lblLargefries.grid(row=3,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="green" ,justify='right')
txtLargefries.grid(row=3,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger ",fg="blue",bd=10,anchor='w')
lblburger.grid(row=4,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="green" ,justify='right')
txtburger.grid(row=4,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza ",fg="blue",bd=10,anchor='w')
lblFilet.grid(row=5,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="green" ,justify='right')
txtFilet.grid(row=5,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="blue",bd=10,anchor='w')
lblCheese_burger.grid(row=6,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="green" ,justify='right')
txtCheese_burger.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
lblDrinks.grid(row=1,column=0)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="green" ,justify='right')
txtDrinks.grid(row=1,column=1)

lblcoupon = Label(f1, font=( 'aria' ,16, 'bold' ),text="Enter Coupon Code",fg="black",bd=10,anchor='w')
lblcoupon.grid(row=1,column=2)
txtcoupon = Entry(f1,font=('ariel' ,16,'bold'), textvariable=couponcode , bd=6,insertwidth=4,bg="red" ,justify='right')
txtcoupon.grid(row=1,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=4,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total before Discount",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text=" Grand Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTotal.grid(row=6,column=3)
# ----------------------------------------Database-----------------------------------------


conn = sqlite3.connect("sourav38.db")
conn.execute("CREATE TABLE menu38(orderno TEXT,friesdata TEXT,largefriesdata TEXT,burgerdata TEXT,pizza TEXT,cheeseburgerdata TEXT,drinksdata TEXT,coupondata TEXT,costdata REAL,servicedata REAL,taxdata REAL,subtotaldata REAL,totaltaxdata REAL)")
def add_val():
    print("helloo in add fun")
    conn.execute("INSERT INTO menu38 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(rand.get(),Fries.get(),Largefries .get(),Burger.get(),Filet .get(),Cheese_burger.get(),Drinks.get(),couponcode.get(),cost.get(),Service_Charge.get(),Tax.get(),Subtotal.get(),Total.get()))
    cursor = conn.execute("SELECT * from menu38")
    for row in cursor:
        print("Order NO:",row[0])
        print("DRINKS:",row[1])
        print("FRENCH FRIES:",row[2])
        print("LUNCH:",row[3])
        print("BURGER:",row[4])
        print("PIZZA:",row[5])
        print("CHEESE BURGER:",row[6])
        print("COUPON CODE:",row[7])
        print("COST:",row[8])
        print("SERVICE CHARGE:",row[9])
        print("TAX:",row[10])
        print("SUBTOTAL:",row[11])
        print("GRAND TOTAL:",row[12])

def invoicefile():
    cursor = conn.execute("SELECT * from menu38")
    for row in cursor:
        file = open("invoice.txt",'w')
        file.write("Order NO:")
        file.write(row[0])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("DRINKS:")
        file.write(row[1])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("FRENCH FRIES:")
        file.write(row[2])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("LUNCH:")
        file.write(row[3])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("BURGER:")
        file.write(row[4])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("PIZZA:")
        file.write(row[5])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("CHEESE BURGER:")
        file.write(row[6])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("COUPON CODE:")
        file.write(row[7])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("COST:")
        file.write(row[8])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("SERVICE CHARGE:")
        file.write(row[9])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("TAX:")
        file.write(row[10])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("TOTAL BEFORE DISCOUNT:")
        file.write(row[11])
        file.write("\n")
        file.write("----------------")
        file.write("\n")
        file.write("GRAND TOTAL:")
        file.write(row[12])
        file.write("\n")
        file.write("-------END---------")
        file.close()


#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=Ref)
btnTotal.grid(row=8, column=1)

btnsave=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Save Bill", bg="red",command=add_val)
btnsave.grid(row=8, column=2)

btninvoice=Button(f1,padx=18,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=12, text="Generate Invoice", bg="red",command=invoicefile)
btninvoice.grid(row=8, column=3)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red",command=reset)
btnreset.grid(row=8, column=4)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=8, column=5)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="red",command=price)
btnprice.grid(row=8, column=0)
root.mainloop()
