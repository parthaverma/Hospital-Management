import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
from tabulate import tabulate

def add_pat():
    Id = int(input("enter patient id"))
    Name = input("enter name")
    Dept = input("enter department admitted")
    Gender = input("enter gender M/F")
    Age = int(input("enter age"))
    Date_adm = input("enter date admitted in yyyy/mm/dd format")
    Date_dis = input("enter date discharged in yyyy/mm/dd format")
    sql = "Insert into Patient_info values({}, '{}','{}','{}',{},'{}','{}')".format(Id,Name,Dept,Gender,Age,Date_adm,Date_dis)
    cur.execute(sql)
    con.commit()
    print("record inserted")

def search_pat():
    Id = int(input("enter patient id"))
    sql = "Select * from Patient_info where ID = {}".format(Id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Department','Gender','Age','Date of admission','Date of discharge']
        print(tabulate(res,headers=a,tablefmt='psql'))
    else:
        print("no records available")

def modify_pat():
    while True:
        Id = int(input("enter patient id to modify"))
        sql = "Select * from Patient_info where ID = {}".format(Id)
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount >=1:
            a = ['ID','Name','Department','Gender','Age','Date of admission','Date of discharge']
            print(tabulate(res,headers=a,tablefmt='grid'))
            ch = input("Do you want to modify")
            if ch in "YesyesyYYES":
                    while True:
                        print("What do you want to modify\n 1.ID\n 2.Name\n 3.Dept\n 4.Gender\n 5.Age\n 6.Date of Admission\n 7.Date of Discharge")
                        a = int(input("enter your choice"))
                        if a not in [1,2,3,4,5,6,7]:
                            print("Invalid choice")
                            print("please enter valid choice")
                            continue
                        if a == 1:
                            ID = int(input("enter id to change to"))
                            sql1 = "Update Patient_info set ID  = {} where ID = {}".format(ID,Id)
                        elif a == 2:
                            nm = input("enter name to change to")
                            sql1 = "Update Patient_info set Name = '{}' where ID = {}".format(nm,Id)
                        elif a == 3:
                            dept = input("enter department to change to")
                            sql1 = "Update Patient_info set Dept = '{}' where ID = {}".format(dept,Id)
                        elif a == 4:
                            Gender = input("enter type to change to")
                            sql1 = "Update Patient_info set Gender = '{}' where ID = {}".format(Gender,Id)
                        elif a == 5:
                            Age = int(input("enter salary to change to"))
                            sql1 = "Update Patient_info set Age = {} where ID = {}".format(Age,Id)
                        elif a == 6:
                            Date_adm  = input("enter date of admission")
                            sql1 = "Update Patient_info set Date_adm = '{}' where ID = {}".format(Date_adm,Id)
                        elif a == 7:
                            Date_dis  = input("enter date of admission")
                            sql1 = "Update Patient_info set Date_dis = '{}' where ID = {}".format(Date_dis,Id)
                        break

            else:
                print("thank you")
                break
        cur.execute(sql1)
        con.commit()
        print("record updated")
        break

def delete_pat():
    id = int(input("enter patient id to delete"))
    sql = "Select * from Patient_info where ID = {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Department','Gender','Age','Date of admission','Date of discharge']
        print(tabulate(res,headers=a,tablefmt='fancy_grid'))
        ch = input("Do you want to delete")
        if ch in "YesyesyYYES":
               sql = "Delete from Patient_info where ID = {}".format(id)
               cur.execute(sql)
               con.commit()
               print("record deleted")
