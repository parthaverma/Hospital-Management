import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
from tabulate import tabulate

def doc_report():
    sql = "Select * from Doctor_info Natural join Salary"
    cur.execute(sql)
    res = cur.fetchall()
    a = ['ID','Name','Department','Type','Salary','Days','DA','TA','Tax']
    print(tabulate(res,headers=a,tablefmt='grid'))

def pat_report():
    sql = "Select * from Patient_info"
    cur.execute(sql)
    res = cur.fetchall()
    a = ['ID','Name','Department','Gender','Age','Date of admission','Date of discharge','Test','Test_id','Department']
    print(tabulate(res,headers=a,tablefmt='psql'))
def bill_report():
    sql = "Select * from Bill"
    cur.execute(sql)
    res = cur.fetchall()
    a = ['ID','Name','Bed_type','Rent','Duration','Total_Bill']
    print(tabulate(res,headers = a,tablefmt = 'fancy_grid'))
    sql1 = "Select * from Tests"
    cur.execute(sql1)
    res = cur.fetchall()
    a = ['Pat_ID','Test','Test_ID','Date']
    print(tabulate(res,headers=a,tablefmt='grid'))