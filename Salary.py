import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
from tabulate import tabulate

def add_sal():
    ID = int(input("enter ID"))
    nm = input("enter name")
    TA = int(input("enter travel allowance"))
    DA = int(input("enter Dearness Allowance"))
    Tax = int(input("enter tax deducted"))
    sql = "Insert into Salary values({},'{}',{},{},{},)".format(ID,nm,TA,DA,Tax)
    cur.execute(sql)
    con.commit()
    print("record inserted")

def search_sal():
    Id = int(input("enter doctor id"))
    sql = "Select * from Salary where ID = {}".format(Id)
    cur.execute(sql)
    res = cur.fetchall()                                                                             
    if cur.rowcount >=1:
        a = ['ID','Name','TA','DA','Tax']
        print(tabulate(res,headers = a,tablefmt = 'psql'))
    else:
        print("no records available")

def modify_sal():
    while True:
        Id = int(input("enter doctor id to modify"))
        sql = "Select * from Patient_info where ID = {}".format(Id)
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount >=1:
            a = ['ID','Name','TA','DA','Tax']
            print(tabulate(res,headers = a,tablefmt = 'grid'))
            ch = input("Do you want to modify")
            if ch in "YesyesyYYES":
                    while True:
                        print("What do you want to modify\n 1.ID\n 2.Name\n 3.TA\n 4.DA\n 5.Tax\n 6.Salary of Doctor")
                        a = int(input("enter your choice"))
                        if a not in[1,2,3,4,5,6]:
                            print("Invalid choice")
                            print("Please enter valid choice")
                            continue
                        if a == 1:
                            ID = int(input("enter id to change to"))
                            sql1 = "Update Patient_info set ID  = {} where ID = {}".format(ID,Id)
                        elif a == 2:
                            nm = input("enter name to change to")
                            sql1 = "Update Patient_info set Name = '{}' where ID = {}".format(nm,Id)
                        elif a == 3:
                            ta = int(input("enter travel allownace to change to"))
                            sql1 = "Update Salary set TA = '{}' where ID = {}".format(ta,Id)
                        elif a == 4:
                            da = int(input("enter type to change to"))
                            sql1 = "Update Salary set DA = '{}' where ID = {}".format(da,Id)
                        elif a == 5:
                            tax = int(input("enter tax to change to"))
                            sql1 = "Update Salary set Tax = {} where ID = {}".format(tax,Id)
                        elif a == 6:
                            sal = int(input("enter new salary"))
                            sql1 = "Update doctor_info set Salary = {} where ID = {}".format(sal,Id)
                        break
            else:
                print("thank you")
                break
        cur.execute(sql1)
        con.commit()
        print("record updated")
        break

def delete_sal():
    id = int(input("enter patient id to delete"))
    sql = "Select * from Salary where ID = {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','TA','DA','Tax']
        print(tabulate(res,headers = a,tablefmt = 'fancy_grid'))
        ch = input("Do you want to delete")
        if ch in "YesyesyYYES":
               sql = "Delete from Salary where ID = {}".format(id)
               cur.execute(sql)
               con.commit()
               print("record deleted")
