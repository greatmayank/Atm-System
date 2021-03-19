from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors

def contin():
    
    def deposit():
        def submi():
            acc=tb2.get()
            pn=tb3.get()
            dep=tb4.get()
            print(acc)
            print(pn)
            conn=pymysql.connect(host='localhost',user='root',password='Mayank@123',db='atm')
            a=conn.cursor()
            a.execute("select * from user_info where account_number='"+acc+"' and pin='"+pn+"'") 
            results=a.fetchall()
            count=a.rowcount
            print(results)
            print(count)
            if(count>0):
                b=conn.cursor()
                b.execute("insert into statement values('"+acc+"',CURDATE(),CURTIME(),'"+dep+"',null,null)")
                print('deposit')
                c=conn.cursor()
                c.execute("update statement set total=total+'"+dep+"' where account_number='"+acc+"'")
                conn.commit()
                messagebox.showinfo("message","Amount Deposit Successfully")
            else:
                conn.rollback()
                print('not deposit')
                messagebox.showerror("meassge","Amount does not Deposit please check data")
            conn.close()    
        win=Tk()
        win.geometry("700x500")
        win.title("welcome to mayank agrawal private limited bank")
        win.config(bg="lime")
        frame3=Frame(win,width=610,height=400,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

        lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb2.place(x=70,y=80)
        tb2=Entry(win,width=50,bd=10,relief="raised")
        tb2.place(x=70,y=120)
        lb3=Label(win,text="Enter Your Pin -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb3.place(x=60,y=180)
        tb3=Entry(win,width=20,bd=10,relief="raised")
        tb3.place(x=70,y=220)
        lb4=Label(win,text="Deposit Amount -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb4.place(x=60,y=280)
        tb4=Entry(win,width=20,bd=10,relief="raised")
        tb4.place(x=70,y=320)

        btn3=Button(win,text="Deposit",command=submi,height=3,width=35,bg="white",justify=CENTER)
        btn3.place(x=350,y=350)

        frame3.place(x=50,y=50) 
        win.mainloop()
        
        

    def withdraw():
        def withd():
            acc=tb2.get()
            pn=tb3.get()
            wit=tb4.get()
            print(acc)
            print(pn)
            conn=pymysql.connect(host='localhost',user='root',password='Mayank@123',db='atm')
            a=conn.cursor()
            a.execute("select * from user_info where account_number='"+acc+"' and pin='"+pn+"'") 
            results=a.fetchall()
            count=a.rowcount
            print(results)
            print(count)
            if(count>0):
                b=conn.cursor()
                b.execute("insert into statement values('"+acc+"',CURDATE(),CURTIME(),null,'"+wit+"',null)")
                print('deposit')
                c=conn.cursor()
                c.execute("update statement set total=total-'"+wit+"' where account_number='"+acc+"'")
                conn.commit()
                messagebox.showinfo("message","Amount withdraw Successfully")
            else:
                conn.rollback()
                print('not deposit')
                messagebox.showerror("meassge","Amount does not withdraw please check data")
            conn.close()    
            
        win=Tk()
        win.geometry("700x500")
        win.title("welcome to mayank agrawal private limited bank")
        win.config(bg="lime")
        frame4=Frame(win,width=610,height=400,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

        lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb2.place(x=70,y=80)
        tb2=Entry(win,justify=CENTER,width=50,bd=10,relief="raised")
        tb2.place(x=70,y=120)
        lb3=Label(win,text="Enter Your Pin -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb3.place(x=60,y=180)
        tb3=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb3.place(x=70,y=220)
        lb4=Label(win,text="Withdraw Amount -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb4.place(x=60,y=280)
        tb4=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb4.place(x=70,y=320)

        btn4=Button(win,text="Withdraw",command=withd,height=3,width=35,bg="white",justify=CENTER)
        btn4.place(x=350,y=350)

        frame4.place(x=50,y=50)

    def balance():
        def bal():
            acc=tb2.get()
            pn=tb3.get()
    
            print(acc)
            print(pn)
            conn=pymysql.connect(host='localhost',user='root',password='Mayank@123',db='atm')
            a=conn.cursor()
            a.execute("select * from user_info where account_number='"+acc+"' and pin='"+pn+"'") 
            results=a.fetchall()
            count=a.rowcount
            print(results)
            print(count)
            if(count>0):
                res.set(row[1])
                res1.set(row[2])
                messagebox.showinfo("your balance is",row[3])
            else:
                conn.rollback()
                print('not show')
                messagebox.showerror("message","please check account number and pin")
            conn.close()    
            
        win=Tk()
        win.geometry("700x500")
        win.title("welcome to mayank agrawal private limited bank")
        win.config(bg="lime")
        frame3=Frame(win,width=610,height=350,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

        lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb2.place(x=70,y=80)
        res=StringVar()
        tb2=Entry(win,textvariable=res,justify=CENTER,width=50,bd=10,relief="raised")
        tb2.place(x=70,y=120)
        lb3=Label(win,text="Enter Your Pin -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb3.place(x=60,y=180)
        res1=StringVar()
        tb3=Entry(win,textvariable=res1,justify=CENTER,width=20,bd=10,relief="raised")
        tb3.place(x=70,y=220)
        
        btn3=Button(win,text="Check Balance",command=bal,height=3,width=35,bg="white",justify=CENTER)
        btn3.place(x=250,y=280)

        frame3.place(x=50,y=50)

    def fast():
        
        
        
        win=Tk()
        win.geometry("700x500")
        win.title("welcome to mayank agrawal private limited bank")
        win.config(bg="lime")
        frame4=Frame(win,width=610,height=450,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

        lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb2.place(x=70,y=80)
        tb2=Entry(win,justify=CENTER,width=50,bd=10,relief="raised")
        tb2.place(x=70,y=120)
        lb3=Label(win,text="Enter Your Pin -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb3.place(x=60,y=180)
        tb3=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb3.place(x=70,y=220)
        btn=Button(win,text="100",width=35,height=3,bg="white",justify=CENTER)
        btn.place(x=60,y=280)
        btn1=Button(win,text="200",width=35,height=3,bg="white",justify=CENTER)
        btn1.place(x=360,y=280)
        btn2=Button(win,text="500",width=35,height=3,bg="white",justify=CENTER)
        btn2.place(x=60,y=350)
        btn3=Button(win,text="2000",width=35,height=3,bg="white",justify=CENTER)
        btn3.place(x=360,y=350)

        btn4=Button(win,text="Withdraw",height=3,width=35,bg="white",justify=CENTER)
        btn4.place(x=250,y=420)

        frame4.place(x=50,y=50)

    def change():
        win=Tk()
        win.geometry("700x500")
        win.title("welcome to mayank agrawal private limited bank")
        win.config(bg="lime")
        frame3=Frame(win,width=610,height=450,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

        lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb2.place(x=70,y=50)
        tb2=Entry(win,justify=CENTER,width=50,bd=10,relief="raised")
        tb2.place(x=70,y=90)
        lb3=Label(win,text="Old Pin -",width=10,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb3.place(x=60,y=150)
        tb3=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb3.place(x=70,y=190)
        lb4=Label(win,text="New Pin -",width=10,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb4.place(x=60,y=250)
        tb4=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb4.place(x=70,y=290)
        lb5=Label(win,text="Confirm New Pin -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb5.place(x=60,y=350)
        tb5=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb5.place(x=70,y=390)

        btn3=Button(win,text="PinChange",height=3,width=35,bg="white",justify=CENTER)
        btn3.place(x=350,y=390)

        frame3.place(x=50,y=20)

    def update():
        win=Tk()
        win.geometry("700x500")
        win.title("welcome to mayank agrawal private limited bank")
        win.config(bg="lime")
        frame3=Frame(win,width=610,height=450,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

        lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb2.place(x=70,y=50)
        tb2=Entry(win,justify=CENTER,width=50,bd=10,relief="raised")
        tb2.place(x=70,y=90)
        lb3=Label(win,text="Old Contact -",width=12,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb3.place(x=60,y=150)
        tb3=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb3.place(x=70,y=190)
        lb6=Label(win,text="Pin -",width=10,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb6.place(x=400,y=150)
        tb6=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb6.place(x=430,y=190)
        lb4=Label(win,text="New Contact -",width=12,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb4.place(x=60,y=250)
        tb4=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb4.place(x=70,y=290)
        lb5=Label(win,text="Confirm New Contact -",width=20,font=('arial',20,'bold'),bg="white",justify=CENTER)
        lb5.place(x=60,y=350)
        tb5=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
        tb5.place(x=70,y=390)

        btn3=Button(win,text="Contact Update",height=3,width=35,bg="white",justify=CENTER)
        btn3.place(x=350,y=390)

        frame3.place(x=50,y=20)    

    def transfer():

       def select():
           
           def bank():
               win=Tk()
               win.geometry("700x500")
               win.title("welcome to mayank agrawal private limited bank")
               win.config(bg="lime")
               frame4=Frame(win,width=610,height=400,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

               lb2=Label(win,text="Enter Bank Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
               lb2.place(x=70,y=80)
               tb2=Entry(win,justify=CENTER,width=50,bd=10,relief="raised")
               tb2.place(x=70,y=120)
               lb3=Label(win,text="IFSC Code -",width=11,font=('arial',20,'bold'),bg="white",justify=CENTER)
               lb3.place(x=60,y=180)
               tb3=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
               tb3.place(x=70,y=220)
               lb4=Label(win,text="Account Holder's name -",width=20,font=('arial',20,'bold'),bg="white",justify=CENTER)
               lb4.place(x=60,y=280)
               tb4=Entry(win,justify=CENTER,width=30,bd=10,relief="raised")
               tb4.place(x=70,y=320)

               btn4=Button(win,text="Transfer Money",height=3,width=35,bg="white",justify=CENTER)
               btn4.place(x=350,y=350)

               frame4.place(x=50,y=50)
               
           
           win=Tk()
           win.geometry("700x500")
           win.title("welcome to mayank agrawal private limited bank")
           win.config(bg="lime")
    
           btn1=Button(win,text="State Bank Of India",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn1.place(x=20,y=50)

           btn2=Button(win,text="Syndicate Bank",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn2.place(x=20,y=150)

           btn3=Button(win,text="Punjab National Bank",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn3.place(x=20,y=250)

           btn4=Button(win,text="Bank of Baroda",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn4.place(x=20,y=350)

           btn5=Button(win,text="Bank Of India",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn5.place(x=400,y=50)

           btn6=Button(win,text="Indian Bank",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn6.place(x=400,y=150)

           btn7=Button(win,text="Axis Bank",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn7.place(x=400,y=250)

           btn8=Button(win,text="HDFC Bank",command=bank,height=3,width=35,bg="white",highlightthickness=5,bd=10)
           btn8.place(x=400,y=350)



        
       win=Tk()
       win.geometry("700x500")
       win.title("welcome to mayank agrawal private limited bank")
       win.config(bg="lime")
       frame4=Frame(win,width=610,height=400,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

       lb2=Label(win,text="Enter your Account Number -",width=25,font=('arial',20,'bold'),bg="white",justify=CENTER)
       lb2.place(x=70,y=100)
       tb2=Entry(win,justify=CENTER,width=50,bd=10,relief="raised")
       tb2.place(x=70,y=160)
       lb3=Label(win,text="Enter Your Pin -",width=15,font=('arial',20,'bold'),bg="white",justify=CENTER)
       lb3.place(x=60,y=250)
       tb3=Entry(win,justify=CENTER,width=20,bd=10,relief="raised")
       tb3.place(x=70,y=310)

       btn4=Button(win,text="Select   Bank",command=select,height=3,width=35,bg="white",justify=CENTER)
       btn4.place(x=350,y=350)

       frame4.place(x=50,y=50)


        
    win=Tk()
    win.geometry("700x500")
    win.title("welcome to mayank agrawal private limited bank")
    win.config(bg="lime")
    
    btn1=Button(win,text="Deposit Cash",command=deposit,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn1.place(x=20,y=50)

    btn2=Button(win,text="Withdraw Cash",command=withdraw,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn2.place(x=20,y=150)

    btn3=Button(win,text="Balance Enquiry",command=balance,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn3.place(x=20,y=250)

    btn4=Button(win,text="Transfer Fund",command=transfer,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn4.place(x=20,y=350)

    btn5=Button(win,text="Mini Statement",height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn5.place(x=400,y=50)

    btn6=Button(win,text="Fast Cash",command=fast,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn6.place(x=400,y=150)

    btn7=Button(win,text="Change Pin",command=change,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn7.place(x=400,y=250)

    btn8=Button(win,text="Update Contact",command=update,height=3,width=35,bg="white",highlightthickness=5,bd=10)
    btn8.place(x=400,y=350)



    
win=Tk()
win.geometry("710x500")
win.title("welcome to mayank agrawal private limited")
win.config(bg="lime")


frame=Frame(win,width=610,height=300,bg="white",highlightbackground="black",highlightthickness=5,bd=10,pady=20,relief="raised")

lb=Label(win,text="Welcome to mayank private bank...",width=35,font=('arial',20,'bold'),bg="white",justify=CENTER)
lb.place(x=46,y=150)

lb1=Label(win,text="press Continue...",width=33,font=('arial',20,'bold'),bg="white",justify=CENTER)
lb1.place(x=55,y=200)          

btn=Button(win,text="Continue...",command=contin,height=3,width=35,bg="white",justify=CENTER)
btn.place(x=200,y=280)

frame.place(x=45,y=100)
