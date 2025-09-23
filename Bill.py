import mysql.connector as ms

def add_bill():
    con = ms.connect(host = "localhost", user = "root", passwd = "123450", database = "hospital")
    cur = con.cursor()
    Id = int(input("enter patient id"))
    Name = input("enter name")
    print("Enter your bed type\n 1.Premium\n 2.Deluxe\n 3.Double sharing\n 4.General Ward\n 5.Single room")
    bt = int(input("enter bed type"))
    if bt == 1:
        a = 20000
    elif bt == 2:
        a = 15000
    elif bt == 3:
        a = 10000
    elif bt == 4:
        a = 2500
    else:
        a = 5000
    q = "Select Date_dis - Date_adm from Patient_info where ID = {}".format(Id)
    cur.execute(q)
    res = cur.fetchall()
    rm = a*res
    print("room rent" == "Rs.", rm)
    c = input("enter department admitted")
    n = int(input("enter how many tests conducted"))
    for i in range(n):
        if c == "ENT":
            print("Choose the tests conducted\n 1.CT Scan\n 2.MRI\n 3.Otoscopy\n 4.Allergy Testing\n 5.General Testing")
            d = int(input("enter your test"))
            if d == 1:
                e = 5000
            elif d == 2:
                e = 10000
            elif d == 3:
                e = 2500
            elif d == 4:
                e = 3000
            else:
                e = 1500
        elif c == "Cardiology":
            print("Choose the tests conducted\n 1.CT Scan\n 2.MRI\n 3.ECG\n 4.Excercise test\n 5.Blood Test")
            d = int(input("enter your test"))
            if d == 1:
                e = 5000
            elif d == 2:
                e = 10000
            elif d == 3:
                e = 500
            elif d == 4:
                e = 2500
            else:
                e = 1500
        elif c == "Urology":
            print("Choose the tests conducted\n 1.CT Scan\n 2.MRI\n 3.Urine test\n 4.Ultrasound\n 5.Cystoscopy")
            d = int(input("enter your test"))
            if d == 1:
                e = 5000
            elif d == 2:
                e = 10000
            elif d == 3:
                e = 500
            elif d == 4:
                e = 2000
            else:
                e = 45000
    tb=  e 
    print("Ypur total bill is ", tb)
add_bill()