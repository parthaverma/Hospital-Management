import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
cur = con.cursor()
import 
while True:
    print("What do you want to do\n 1.Operations with Doctor(s)\n 2.Operations o n Patient(s)\n 3.Operations on Bill\n 4.Operations on Salary\n 5.Operations on Reports")
    a = int(input("enter your choice"))
    if a not in [1,2,3,4,5]:
        print("invaild choice")
        print("please enter correct choice")
        continue
    if a == 1:
        while True:
            print("What do you want to do now\n 1.Add docotr\n 2.Modify doctor\n 3.Search doctor\n 4.Delete doctor")
            b = int(input("enter your choice"))
            if b not in [1,2,3,4]:
                print("invaild choice")
                print("please enter correct choice")
                continue
            if b == 1:
                add_doctor()
            elif b == 2:
                modify_doctor()
            elif b == 3:
                search_doctor()
            elif b == 4:
                delete_doctor()
            
            break

    elif a == 2:
        while True:
            print("What do you want to do\n 1.Add patient\n 2.Modify patient\n 3.Search patient\n 4.Delete patient")
            b = int(input("enter your choice"))
            if b not in [1,2,3,4]:
                print("invaild choice")
                print("please enter correct choice")
                continue
            if b == 1:
                add_patient()
            elif b == 2:
                modify_doctor()
            elif b == 3:
                search_doctor()
            elif b == 4:
                delete_doctor()

            break
    elif a == 3:
        while True:
            print("What do you want to do\n 1.Add bill\n 2.Modify bill\n 3.Search bill\n 4.Delete bill")
            b = int(input("enter your choice"))
            if b not in [1,2,3,4]:
                print("invaild choice")
                print("please enter correct choice")
                continue
            if b == 1:
                add_bill()
            elif b == 2:
                modify_bill()
            elif b == 3:
                search_bill()
            elif b == 4:
                delete_bill()
            
            break
    elif a == 4:
        while True:
            print("What do you want to do\n 1.Add salary\n 2.Modify salary\n 3.Search salary\n 4.Delete salary")
            b = int(input("enter your choice"))
            if b not in [1,2,3,4]:
                print("invaild choice")
                print("please enter correct choice")
                continue
            if b == 1:
                add_salary()
            elif b == 2:
                modify_salary()
            elif b == 3:
                search_salary()
            elif b == 4:
                delete_salary()
            
            break
    elif a == 5:
        while True:
            print("What do you want to do\n 1. View doctor report \n 2.View Patient report\n 3.View Bill report")
            b = int(input("enter your choice"))
            if b not in [1,2,3]:
                print("invaild choice")
                print("please enter correct choice")
                continue
            if b == 1:
                doc_report()
            elif b == 2:
                pat_report()
            elif b == 3:
                bill_report()
            

            break
    
    break
