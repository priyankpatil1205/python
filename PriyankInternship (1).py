
# coding: utf-8

# In[11]:

from tkinter import *
from tkinter import messagebox
import pymysql as sql



def uploadData(empName):
    try:
        uname=empName
        
        db=sql.connect("localhost","root","","company")
        cursor=db.cursor()
        sql_cmd="insert into employee(empName) values('{}')".format(uname)
        cursor.execute(sql_cmd)
        
    except BaseException as e:
        print(e)
        db.rollback()
        msg=messagebox.showinfo("Info","Error in upload")
        
    else:
        db.commit()
        if(cursor.rowcount>0):
            message=messagebox.showinfo("Info","Data Uplaoded")
            
    finally:
        db.close()
        master.destroy()
        
def getEntry():
    user = entry1.get()
    uploadData(empName = user)







def deleteRecord(empName):
    try:
        uname=empName
        
        db=sql.connect("localhost","root","","company")
        cursor=db.cursor()
        sql_cmd = "delete from employee where empName like '%{}%'".format(uname)
        cursor.execute(sql_cmd)
                       
    except BaseException as e:
        print(e)
        db.rollback()                       
    else:
        db.commit()
        if(cursor.rowcount>0):
            message=messagebox.showinfo("Info","Data Deleted")
            
        else:
            message=messagebox.showinfo("Info","No Record Found")
                     
    finally:
        db.close()
        master.destroy()
        
        
def getExit():
    user = entry1.get()
    deleteRecord(empName = user)
    
    
    
    
    
    
    
def uploadMang(mangName):
    try:
        uname=mangName

        
        db=sql.connect("localhost","root","","company")
        cursor=db.cursor()
        sql_cmd="insert into manager(mangName) values('{}')".format(uname)
        cursor.execute(sql_cmd)
        
    except BaseException as e:
        print(e)
        db.rollback()
        msg=messagebox.showinfo("Info","Error in upload")
        
    else:
        db.commit()
        if(cursor.rowcount>0):
            message=messagebox.showinfo("Info","Data Uplaoded")
            
    finally:
        db.close()
        master.destroy()
        
def getEntry1():
    user = entry3.get()
    uploadMang(mangName = user)
    
def selecttop(): 
    try:
        
        db,cursor = getDBConnection()
        sql_cmd = "SELECT * FROM employee"
        cursor.execute(sql_cmd)
        
        #Fetch all the rows in a list of lists
        
        results = cursor.fetchall()
        for row in results:
            empName = row[0]
            print("EMPNAME=%s"%(empName))
        
    except:
        print("Error: unable to fetch data")
        
    finally:
        db.close()


    
    


    
    
root=Tk()
root.geometry("300x250")
root.title("MANAGE EMPLOYEE")
root.iconbitmap('favicon.ico')
label5=Label(root,text='EMPLOYEE MANAGEMENT SYSTEM')
label5.pack()
label5.config(justify = CENTER)
#Adding the employee
label1=Label(root,text='Name of employee to be added')
label1.pack()
label1.config(justify = CENTER)

entry1 = Entry(root,width=30)
entry1.pack()

button1=Button(root,text='ADD',activebackground="Blue",activeforeground="Red")
button1.pack()
button1.config(command=getEntry)

#Removing the Employee
label3=Label(root,text='Name of employee to be removed')
label3.pack()
label3.config(justify = CENTER)

entry2 = Entry(root,width=30)
entry2.pack()

button1=Button(root,text='REMOVE',activebackground="Blue",activeforeground="Red")
button1.pack()
button1.config(command=getExit)


#Add manager
label4=Label(root,text='Name of manager to be added')
label4.pack()
label4.config(justify = CENTER)

entry3 = Entry(root,width=30)
entry3.pack()

button1=Button(root,text='ADD manager',activebackground="Blue",activeforeground="Red")
button1.pack()
button1.config(command=getEntry1)

button1=Button(root,text='Display',activebackground="Blue",activeforeground="Red")
button1.pack()
button1.config(command=selecttop)

root.mainloop()

