import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
from tabulate import tabulate

def opd():
    pno = int(input("enter patient no"))
    nm = input("enter patient name")
    print("Choose from departments\n 1.ENT\n 2.Cardiology\n 3.Urology")
    dept = int(input("enter your choice"))
    day = input("enter day(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)")
    date = input("enter date")
    if dept == 1:
        dept = "ENT"
        sql = "Select Name from Doctor_info where Department = 'ENT' and FIND_IN_SET ('{}',Day)".format(day)
        cur.execute(sql)
        res = cur.fetchall()
        res = res[0]
        res = res[0]
        print("The doctor will be",res)
        sql1 = "Select Fees from Doctor_info where Department = 'ENT' and FIND_IN_SET ('{}',Day)".format(day) 
        cur.execute(sql1)
        res1 = cur.fetchall()
        res1 = res1[0]
        res1 = res1[0]
        print(res1)
    
    elif dept == 2:
        dept = "Cardiology"
        sql = "Select Name from Doctor_info where Department = 'Cardiology' and FIND_IN_SET ('{}',Day)".format(day)
        cur.execute(sql)
        res = cur.fetchall()
        res = res[0]
        res = res[0]
        print("The doctor will be",res)
        sql1 = "Select Fees from Doctor_info where Department = 'ENT' and FIND_IN_SET ('{}',Day)".format(day) 
        cur.execute(sql1)
        res1 = cur.fetchall()
        res1 = res1[0]
        res1 = res1[0]

    elif dept == 3:
        dept = "Urology"
        sql = "Select Name from Doctor_info where Department = 'Urology' and FIND_IN_SET ('{}',Day)".format(day)
        cur.execute(sql)
        res = cur.fetchall()
        res = res[0]
        res = res[0]
        print("The doctor will be",res)
        sql1 = "Select Fees from Doctor_info where Department = 'ENT' and FIND_IN_SET ('{}',Day)".format(day) 
        cur.execute(sql1)
        res1 = cur.fetchall()
        res1 = res1[0]
        res1 = res1[0]

    print("In which OPD you want to go?\n 1.General\n 2.Private")
    ch = int(input("enter your choice"))
    if ch == 1:
        print("Your fees will be Rs.100 ")
    elif ch == 2:
        print("Your fees will be Rs.",res1)
    sql2 = "Insert into OPD values({},'{}','{}','{}','{}','{}',{})".format(pno,nm,dept,day,date,res,res1)
    cur.execute(sql2)
    con.commit()
    print("record inserted")


def search_opd():
    Id = int(input("enter patient id"))
    sql = "Select * from OPD where PNO = {}".format(Id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['PNO','Name','Department','Day','Date','DocName','Fees']
        print(tabulate(res,headers=a,tablefmt='grid'))
    else:
        print("No records found")


def delete_opd():
    id = int(input("enter patient id to delete"))
    sql = "Select * from OPD where PNO = {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['PNO','Name','Department','Day','Date','Docname','Fees']
        print(tabulate(res,headers=a,tablefmt='fancy_grid'))
        ch = input("Do you want to delete")
        if ch in "YesyesyYYES":
               sql = "Delete from OPD where PNO = {}".format(id)
               cur.execute(sql)
               con.commit()
               print("record deleted")
        else:
            print("thank you")