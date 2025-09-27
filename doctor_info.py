import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
from tabulate import tabulate

def add_doctor():
    ID = int(input("enter id"))
    Name = input("enter name")
    Dept = input("enter department name")
    Type = input("enter type")
    Sal = int(input("enter salary"))
    day = input("Enter days available")
    fees = int(input("enter fees for opd"))
    sql = "Insert into Doctor_info values({},'{}','{}','{}',{},'{}',{})".format(ID,Name,Dept,Type,Sal,day,fees)
    cur.execute(sql)
    con.commit()
    print("record inserted")

def search_doctor():
    ID = int(input("enter id to search"))
    sql = "Select * from Doctor_info where ID = {}".format(ID)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Department','Type','Salary','Day','Fees']
        print(tabulate(res,headers=a,tablefmt='psql'))
    else:
        print("no records available") 

def modify_doctor():
    while True:
        Id = int(input("enter doctor id to modify"))
        sql = "Select * from Doctor_info where ID = {}".format(Id)
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount >=1:
            a = ['ID','Name','Department','Type','Salary','Day','Fees']
            print(tabulate(res,headers=a,tablefmt='grid'))
            ch = input("Do you want to modify")
            if ch in "YesyesyYYES":
                    while True:
                        print("What do you want to modify\n 1. ID\n 2. Name\n 3.Department\n 4.Type\n 5.Salary\n 6.Day\n 7.Fees")
                        a = int(input("enter your choice"))
                        if a not in [1,2,3,4,5,6,7]:
                            print("Invalid choice")
                            print("please enter right choice")
                            continue
                        else:
                            if a == 1:
                                ID = int(input("enter id to change to"))
                                sql1 = "Update Doctor_info set ID  = {} where ID = {}".format(ID,Id)
                            elif a == 2:
                                nm = input("enter name to change to")
                                sql1 = "Update Doctor_info set Name = '{}' where ID = {}".format(nm,Id)
                            elif a == 3:
                                dept = input("enter department to change to")
                                sql1 = "Update Doctor_info set Department = '{}' where ID = {}".format(dept,Id)
                            elif a == 4:
                                type = input("enter type to change to")
                                sql1 = "Update Doctor_info set Type = '{}' where ID = {}".format(type,Id)
                            elif a == 5:
                                sal = int(input("enter salary to change to"))
                                sql1 = "Update Doctor_info set Salary = {} where ID = {}".format(sal,Id)
                            elif a == 6:
                                day = input("enter new days")
                                sql1 = "Update Doctor_info set Day = '{}' where ID = {}".format(day,Id)
                            elif a == 7:
                                fees = int(input("enter new fees"))
                                sql1 = "Update Doctor_info set Fees = {} where ID = {}".format(fees,Id)

                        
                        break

                    cur.execute(sql1)
                    con.commit()
                    print("record updated")
            else:
                print("thank you")
        else:
            print("ID not found")
        
        break




def delete_doctor():
    id = int(input("enter doctor id to delete"))
    sql = "Select * from Doctor_info where ID = {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Department','Type','Salary','Day','Fees']
        print(tabulate(res,headers=a,tablefmt='fancy_grid'))
        ch = input("Do you want to delete")
        if ch in "YesyesyYYES":
               sql = "Delete from Doctor_info where ID = {}".format(id)
               cur.execute(sql)
               con.commit()
               print("record deleted")

