
# coding: utf-8

# In[5]:

from tkinter import *
from tkinter import messagebox
import pymysql as sql

       
            

class Employee():
    def __init__(self,company='ABC'):
        self.company=company
         
class HourEmployee(Employee):
    def __init__(self,name,hour=7,emptype='Hourly',salary=250):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.salary=salary
        self.hour=hour
        self.salary=(self.salary)*(self.hour)
        
class SalariedEmployee(Employee):
    def __init__(self,name,hour=9,emptype='Salaried',salary=40000):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.hour=hour
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,hour=8,emptype='Manager',salary=400000):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.hour=hour
        self.salary=salary
        
class Executive(Employee):
    def __init__(self,name,hour=7,emptype='Executive',salary=900000):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.hour=hour
        self.salary=salary
        
class Company():
    def __init__(self, ki):
       
        self.ki=ki
        self.interface()
  
    def getDBConnection(ip = "localhost", usern = "root",passn = "",dbname = "company"):
        try:
            import pymysql as sql
            db = sql.connect(ip,usern,passn,dbname)
            cursor=db.cursor()
       
        except BaseException as e:
            print(e)        
        else:
            print("Connected..")
            return db,cursor
   
    
    def hire(self,r,i0):
        try:
            db=sql.connect("localhost","root","","company")
            cursor=db.cursor()
            n=r
            na=i0
            if n==2:                
                m=HourlyEmployee(name=na)    
            elif n==1: 
                m=SalariedEmployee(name=na)   
            elif n==3:  
                m=Manager(name=na)
            else:
                m=Executive(name=na)    
            m1=m.name
            m2=m.hour
            m3=m.emptype
            m4=m.salary
            sql_cmd="insert into employees2(NAME,Hour,EmpType,Salary) values('{}','{}','{}','{}')".format(m1,m2,m3,m4)
            cursor.execute(sql_cmd)       
        except BaseException as e:
            print(e)
            db.rollback()      
            msg=messagebox.showinfo("Info","Error!")
        else:
            db.commit()   
            if(cursor.rowcount>0):
                message=messagebox.showinfo("Info","Employee Hired!")
        finally:
            db.close()
            
    def gethire(self):
        r=self.entry1.get()
        i0=self.entry2.get()
        self.hire(r,i0)

    def remove(self,i1):
        try:
            u=i1
            db=sql.connect("localhost","root","","company")
            cursor=db.cursor()
            sql_cmd = "delete from employees2 where id like '%{}%'".format(u)
            cursor.execute(sql_cmd)                    
        except BaseException as e:
            print(e)
            db.rollback()     
        else:
            db.commit()
            if(cursor.rowcount>0):
                message=messagebox.showinfo("Info","Employee fired!")
            else:
                message=messagebox.showinfo("Info","Employee Not Found!")
                        
        finally:
            db.close()  
            
    def getremove(self):
        u =self.entry3.get()
        self.remove(i1 = u)
        
    def raise1(self,i2,i3,i4):
        try:
            m5=i2
            m6=i3
            m7=i4
            db=sql.connect("localhost","root","","company")
            cursor=db.cursor()
            sql_cmd = "update employees2 set EmpType='{}',salary='{}' where id like '%{}%'".format(m6,m7,m8)
            cursor.execute(sql_cmd)                    
        except BaseException as e:
            print(e)
            db.rollback() 
            msg=messagebox.showinfo("Info","Error in promoting Employee!")
        else:
            db.commit()
            if(cursor.rowcount>0):
                message=messagebox.showinfo("Info","Employee Promoted!")    
                           
        finally:
            db.close()
    
    def getraise1(self):
        u3 = self.entry4.get()
        u1=self.entry5.get()
        u2=self.entry6.get()
        
        self.raise1(i2 = u3,i3=u1,i4=u2)
        
    
    
    def interface(self):
        self.ki.geometry("500x500")
        self.ki.title("Employee management system")
        self.ki.iconbitmap('favicon.ico')
        self.ki.l1=Label(self.ki,text='Employee Manager for Company')
        self.ki.l1.pack()
        
        #Adding the employee
        self.l2=Label(self.ki,text='Enter 1.For Salaried employee 2.For hourly employee 3.For Manager 4.For Executive:')
        self.l2.pack()
    
        self.entry1 = Entry(self.ki,width=20)
        self.entry1.pack()
        self.l3=Label(self.ki,text='Enter Name of the employee to be hired:')
        self.l3.pack()
    
        self.entry2 = Entry(self.ki,width=20)
        self.entry2.pack()
        self.b1=Button(self.ki,text='Hire',activebackground="Blue",activeforeground="Red")
        self.b1.pack()

        self.b1.config(command=self.gethire)

        #Adding the employee
        #Removing the Employee

        self.l4=Label(self.ki,text='Enter ID of the Employee to be Fired:')

        self.l4.pack()

        

        self.entry3 = Entry(self.ki,width=20)

        self.entry3.pack()

        self.b2=Button(self.ki,text='Fire',activebackground="Blue",activeforeground="Red")

        self.b2.pack()

        self.b2.config(command=self.getremove)
        #update

        self.l5=Label(self.ki,text='Enter ID of Employee who is to be Raised:')

        self.l5.pack()

        

        self.entry4 = Entry(self.ki,width=20)

        self.entry4.pack()
        self.l6=Label(self.ki,text='Enter the raised postion : ')

        self.l6.pack()

    
        self.entry5 = Entry(self.ki,width=20)

        self.entry5.pack()
        self.l7=Label(self.ki,text='Enter new salary for raised employee:')

        self.l7.pack()

        
        self.entry6 = Entry(self.ki,width=20)

        self.entry6.pack()
        self.b3=Button(self.ki,text='Raise',activebackground="Blue",activeforeground="Red")

        self.b3.pack()

        self.b3.config(command=self.getraise1)
        
def main():
    root=Tk()
    d=Company(root)
    root.mainloop()

if __name__=="__main__":
    main()  
   

