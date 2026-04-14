import mysql.connector as c
import os
con=c.connect(host='localhost',user='root',password='123456')
print(c)
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS SANDRAJCARS")
cur.execute("use SANDRAJCARS")
cur.execute("create table if not exists ROYALCARS( SNO int(4),CNAME varchar(25),COMPANY varchar(30),PRICE int(10))")
user='y'
print("\n######## WELCOME TO SANDRAJCARS DATABASE MANAGEMENT SYSTEM #######\n\n")
while  user=='y':
    print("""1.add record
2.update record
3.delete record
4.disply record
5.exit\n""")
    choice=int(input("enter the choice from the above menu"))
    if choice==1:
        add_more='Y'
        while add_more=='Y':
            SNO=int(input("\nenter car serial no"))
            CNAME=input("enter car name")
            COMPANY=input("enter the company name")
            PRICE=int(input("enter the car price"))
            q="insert into ROYALCARS values ({},'{}','{}',{})".format(SNO,CNAME,COMPANY,PRICE)
            cur.execute(q)
            con.commit()
            print("\n##DATA SAVED SUCCESSFUL##")
            add_more=input('\ndou you want to add more data?(Y/N)')
            user=input('\ndo you waant to continue(Y/N)')
    elif choice==2:
        sno_for_updation=int(input('\n enter the serial no of the car whose details are to be updated'))
        s='Y'
        while s=='Y':
            up_details=int(input("""what do you want to update
1.COMPANY
2.CNAME
3.PRICE
ENTER YOUR CHOICE"""))
            if up_details==1:
                new_COMPANY=input('enter the new company')
                sql='update ROYALCARS set COMPANY=%s where SNO=%s'
                input_data=(new_COMPANY,sno_for_updation)
                cur.execute(sql,input_data)
                con.commit()
                s=input('\ndo you want to update more?(Y/N)')
            elif up_details==2:
                new_CNAME=int(input("enter new sno "))
                sql='update ROYALCARS set SNO=%s where SNO=%s'
                input_data=(new_CNAME,sno_for_updation)
                cur.execute(sql,input_data)
                con.commit()
                s=input('\n do you want more to update?(Y/N)')
            elif up_details==3:
                new_price=int(input('enter new price'))
                sql='update ROYALCARS set price=%s where SNO=%s'
                input_data=(new_price,sno_for_updation)
                cur.execute(sql,input_data)
                con.commit()
                s=input('\n do you want more to update?(Y/N)')
    elif choice==3:
        nm=int(input("enter SNO of car to be deleted from record"))
        sql="delete from ROYALCARS where SNO=%s"
        nml=(nm,)
        cur.execute(sql,nml)
        con.commit()
        print(cur.rowcount,"record(s) deleted")
        user=input("\n do you want to continue?(Y/N)")
    elif choice==4:
        cur.execute("select * from ROYALCARS")
        myresult=cur.fetchall()
        for x in myresult:
            print(x)
        user=input("\n do you want to continue?(Y/N)")
    elif choice==5:
        print("\n THANK YOU FOR USING SANDRAJCARS DATABASE MANAGEMENT SYSTEM ")
        user="exit"
    else:
        print("\n looks like u selected an invalid choice.try again")
        user=input("\n do you want to continue?(Y/N)")
os.system("pause")        

    
   
                            
