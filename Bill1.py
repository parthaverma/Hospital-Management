import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
from tabulate import tabulate

def add_bill():
    while True:
        Id = int(input("Enter ID: "))
        sql = "SELECT * FROM Patient_info WHERE ID = %s"
        cur.execute(sql, (Id,))
        res = cur.fetchall()
        if not res:
            print("ID does not exist")
            print("Please enter a correct ID")
            continue
        Name = input("Enter name: ")
        print(Name)
        while True:
            print("Enter your bed type: \n 1.Premium\n 2.Deluxe\n 3.Double Sharing\n 4.General Ward\n 5.Single Room")
            bt = int(input("Enter your choice: "))
            if bt not in [1, 2, 3, 4, 5]:
                print("Invalid choice")
                print("Please enter a correct choice")
            else:
                if bt == 1:
                    a = 20000
                elif bt == 2:
                    a = 15000
                elif bt == 3:
                    a = 10000
                elif bt == 4:
                    a = 2500
                elif bt == 5:
                    a = 5000
            break  
        n = "Select Date_dis from Patient_info where ID = {}".format(Id)
        cur.execute(n)
        res = cur.fetchall()
        res = str(res)
        res = res[1:8]
        if "(None,)" in res:
              print("Patient is not discharged")         
        else:
            q = "Select Date_dis - Date_adm from Patient_info where ID = {}".format(Id)
            cur.execute(q)
            res = cur.fetchall()
            res=str(res)
            res=res[2:5]
            res=int(res)
            rm = a*res
            dur = res
            print("room rent", '=', "Rs.", rm)
        
        while True:
            print("Choose the department admitted\n 1.ENT\n 2.Cardiology\n 3.Urology")
            c = int(input("enter department admitted")) 
            if c not in [1,2,3]:
               print("Invalid Department")
               print("please enter valid department")
               break
            n = int(input("Enter how many tests conducted: "))
            total = 0
            if c == 1:
                c = "ENT"
                for i in range(n):
                        print("Choose the tests conducted:\n 1.CT Scan\n 2.MRI\n 3.Otoscopy\n 4.Allergy Testing\n 5.General Testing")
                        d = int(input("Enter your choice: "))                        
                        if d not in [1, 2, 3, 4, 5]:
                            print("Invalid choice")
                            print("Please enter a valid choice")
                            break
                        for i in range(n):                      
                            if d == 1:
                                e = 5000
                                a = "CT Scan"
                                b = 1          
                            elif d == 2:
                                e = 10000
                                a = "MRI"
                                b = 2
                                                            
                            elif d == 3:
                                e = 2500
                                a = "Ostoscopy"
                                b = 3
                                
                            elif d == 4:
                                e = 3000
                                a = "Allergy Testing"
                                b = 4                           
                            elif d == 5:
                                e = 1500
                                a = "General Testing"
                                b = 5
                        sql = "Insert into tests values({},'{}',{},'{}')".format(Id,a,b,c)
                        cur.execute(sql)
                        con.commit()
                        total=total+e                         
                break                                 
            elif c == 2:
                c = "Cardiology"
                for i in range(n):
                    print("Choose the tests conducted\n 1.CT Scan\n 2.MRI\n 3.ECG\n 4.Excercise test\n 5.Blood Test")
                    d = int(input("enter your choice"))
                    if d not in [1,2,3,4,5]:
                        print("Invalid choice")
                        print("Please enetr correct choice")
                        break
                    for i in range(n):
                        if d == 1:
                            e = 5000
                            a = "CT Scan"
                        elif d == 2:
                            e = 10000
                            a = "MRI"
                        elif d == 3:
                           e = 500
                           a = "ECG"
                        elif d == 4:
                            e = 2500
                            a = "Exercise test"
                        elif d == 5:
                            e = 1500
                            a = "Blood Test"
                    sql = "Insert into tests values({},'{}',{},'{}')".format(Id,a,b,c)
                    cur.execute(sql)
                    con.commit()
                    total = total + e
                break  
            elif c == 3:
                c = "Urology"
                for i in range(n):
                    print("Choose the tests conducted\n 1.CT Scan\n 2.MRI\n 3.Urine test\n 4.Ultrasound\n 5.Cystoscopy")
                    d = int(input("enter your choice"))
                    if d not in [1,2,3,4,5]:
                        print("Invalid choice")
                        print("Please enter correct choice")
                        break
                    for i in range(n):
                        if d == 1:
                             e = 5000
                             a = "CT Scan"
                             b = 1
                        elif d == 2:
                            e = 10000
                            a = "MRI"
                            b = 2
                        elif d == 3:
                            e = 500
                            a = "Urine test"
                            b = 3
                        elif d == 4:
                            e = 2000
                            a = "Ultrasound"
                            b = 4
                        elif d == 5:
                            e = 45000
                            a = "Cystoscopy"
                            b = 5
                    sql = "Insert into tests values({},'{}',{},'{}')".format(Id,a,b,c)
                    cur.execute(sql)
                    con.commit()
                    break
            break
        total=total+e
        total=total+rm
        print("Your total bill is ", total)
        sql = "Insert into Bill(ID,Name,Bed_type,Rent,Duration,Total_Bill)values({},'{}','{}',{},{},{})".format(Id,Name,bt,rm,dur,total)                        
        cur.execute(sql)
        con.commit()
        print("record inserted")     
        break      


def delete_bill():
    id = int(input("enter patient id to delete"))
    sql = "Select * from Bill Natural Join Tests where ID= {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Bed_type','Rent','Duration','Total_Bill','Test','Test_ID']
        print(tabulate(res,headers = a,tablefmt = 'grid'))
        ch = input("Do you want to delete")
        if ch in "YesyesyYYES":
                sql = "Delete from Bill where ID = {}".format(id)
                cur.execute(sql)
                con.commit()
                print("record deleted")

def search_bill():
    id  = int(input("enter patient id to search"))
    sql = "Select * from Bill  Natural Join Tests where ID= {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Bed_type','Rent','Duration','Total_Bill','Test','Test_ID']
        print(tabulate(res,headers = a,tablefmt = 'psql'))
    else:
        print("no record available")

def modify_bill():
    id = int(input("enter patient id to modify"))
    sql = "Select * from Bill  Natural Join Tests where ID= {}".format(id)
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount >=1:
        a = ['ID','Name','Bed_type','Rent','Duration','Total_Bill','Test','Test_ID']
        print(tabulate(res,headers = a,tablefmt = 'fancy_grid'))
        ch = input("Do you want to delete")
        if ch in "YesyesyYYES":
                while True:
                    print("What do you want to modify\n 1.ID\n 2.Name\n 3.Bed_type\n 4.Rent\n 5.Duration\n 6.Total_bill")
                    ch1 = int(input("enter your choice"))
                    if ch1 not in[1,2,3,4,5,6]:
                         print("Invalid choice")
                         print("Please enter correct choice")
                         continue
                    if ch1 == 1:
                        ID = int(input("enter id to change to"))
                        sql1 = "Update Bill set ID  = {} where ID = {}".format(ID,id)
                    elif ch1 == 2:
                        nm = input("enter name to change to")
                        sql1 = "Update Bill set Name = '{}' where ID = {}".format(nm,id)
                    elif ch1 == 3:
                        bd = input("enter bed type to change to")
                        sql1 = "Update Bill set Bed_Type = '{}' where ID = {}".format(bd,id)
                    elif ch1 == 4:
                        rent = int(input("enter new rent"))
                        sql1 = "Update Bill set Rent = {} where ID = {}".format(rent,id)
                    elif ch1 == 5:
                        dur1 = int(input("enter new duration"))
                        sql1 = "Update Bill set Duration = {} where ID = {}".format(dur1,id)
                    elif ch1 == 6:
                        tb = int(input("enter total bill to change to"))
                        sql1 = "Update Bill set Total_bill = {} where ID = {}".format(tb,id)
                    else:
                        print("Thnak you")
                    cur.execute(sql1)
                    con.commit()
                    print("record updated")
                    break

