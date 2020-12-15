from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import tkinter
import MainModule

def main():
    root=Tk()
    app= Window1(root)
    root.mainloop()
class Window1:
    def __init__(self, master):
        self.master=master
        self.master.title("HR LOGIN")
        self.master.geometry("300x300+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.master.configure(bg="grey")
        
        self.Username = StringVar()
        self.Pass = StringVar()
        
        #self.labelTitle= Label(self.frame, text="HR Login", font=("Arial",20,'bold'), fg="black", bg="lightblue") 
        #self.labelTitle.grid(row=0,column=0, columnspan=2,pady=20)
        
        self.loginFrame = Frame(self.frame, width=600, height=300, relief='ridge')
        self.loginFrame.grid(row=1,column=0)
        
        self.loginFrame.configure(bg="grey")
        self.frame.configure(bg="grey")
        
        self.loginFrame2 = Frame(self.frame, width=600, height=300, relief='ridge')
        self.loginFrame2.grid(row=2,column=0)
        
        self.loginFrame3 = Frame(self.frame, width=600, height=300, relief='ridge')
        self.loginFrame3.grid(row=3,column=0,pady=2)
        #_______________________________________________________________________________________________________________
        self.labelUser= Label(self.loginFrame, text="Username ", font=("Arial",12, "bold"), pady=8,fg="black", bg="grey") 
        self.labelUser.grid(row=0,column=0, pady=5)
        self.txtUser= Entry(self.loginFrame, font=("Arial",12), textvariable=self.Username, bg="snow2") 
        self.txtUser.grid(row=1,column=0)
        
        self.labelPass= Label(self.loginFrame, text="Password ", font=("Arial",12,"bold"),pady=5, fg="black",bg="grey") 
        self.labelPass.grid(row=2,column=0)
        self.txtPass= Entry(self.loginFrame, text="Username: ", font=("Arial",12),textvariable=self.Pass, show="*",bg="snow2") 
        self.txtPass.grid(row=3,column=0, pady=10)
        #_______________________________________________________________________________________________________________
        self.btnLogin= Button(self.loginFrame2,text="Login",command=self.loginSys, font=("Arial",12),bg="steelblue3", width=5)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset= Button(self.loginFrame2,text="Reset", command=self.reset, font=("Arial",12),bg="steelblue3",width=5)
        self.btnReset.grid(row=0,column=1)
        
        self.btnExit= Button(self.loginFrame2,text="Exit", command=self.exit,font=("Arial",12),bg="steelblue3",width=5)
        self.btnExit.grid(row=0,column=2)
        
        #_______________________________________________________________________________________________________________
        
        
        self.btnHR= Button(self.loginFrame3,text="Manage Employees", command=self.HR_window, bg="honeydew3", fg="black",state=DISABLED)
        self.btnHR.grid(row=0,column=0)
        
        #_______________________________________________________________________________________________________________
    def loginSys(self):
        user=(self.Username.get())
        pas=(self.Pass.get())
        if (user == str("admin") and pas== str("admin")):
            self.btnHR.config(state= NORMAL)
        else:
            tkinter.messagebox.showwarning("HR LOGIN PAGE", "Incorrect Credentials!")
            self.btnHR.config(state= DISABLED)
            self.Username.set("")
            self.Pass.set("")
            self.txtUser.focus()
    
    def reset(self):
        self.btnHR.config(state= DISABLED)
        self.Username.set("")
        self.Pass.set("")
        self.txtUser.focus()
    def exit(self):
        self.exit= tkinter.messagebox.askyesno("HR LOGIN", "Confirm if you want to exit")
        if self.exit>0:
            self.master.destroy()
            return
#_______________________________________________________________________________________________________________

    def HR_window(self):
        self.new_window= Toplevel(self.master)
        self.app=Window2(self.new_window)
class Window2:
    def __init__(self, master):
        self.master=master
        self.master.title("HR Management System")
        self.master.geometry("960x580+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
    #_______________________________________________________________________________________________________________
        empID= StringVar()
        empName= StringVar()
        empDesig= StringVar()
        empDOB= StringVar()
        empJoining= StringVar()
        empPhone= StringVar()
        empEmail= StringVar()
        empSalary= StringVar()
        empAllowance= StringVar()
        empMedicExp= StringVar()
        empTax= StringVar()
        empLeave= StringVar()    
        
    #______________________________________Function_________________________________________________________________________
        def iexit():
            exit=tkinter.messagebox.showwarning("HR Management System", "Logging Out!")
            self.master.destroy()
            return
            
        def sendSlip():
            mail=empEmail.get()
            salary=MainModule.getEmployeeSalary(empID.get())
            send=tkinter.messagebox.askyesno("Salary Slip", f"Are you sure you want to send {mail} his Salary Slip of Rupee {salary}" )
            if send:
                tkinter.messagebox.showwarning("Sending", "Mailing...")
                MainModule.Salary_Slip(empID.get())
            
            
        def clearData():
            self.txtEmpId.delete(0, END)
            self.txtEmpName.delete(0, END)
            self.txtDesig.delete(0, END)
            self.txtEmpPhone.delete(0, END)
            self.txtEmpEmail.delete(0, END)
            self.txtEmpDOB.delete(0, END)
            self.txtEmpAllowance.delete(0, END)
            self.txtEmpJoining.delete(0, END)
            self.txtEmpMedical.delete(0, END)
            self.txtEmpSalary.delete(0, END)
            self.txtEmpTax.delete(0, END)
            self.txtEmpLeave.delete(0, END)
            
        def addData():
            if(len(empID.get())!=0):
                MainModule.Add_Employee(empID.get(), empName.get(), empDesig.get(), empDOB.get(),empJoining.get(), empPhone.get(), empEmail.get(), empSalary.get(), empAllowance.get(), empMedicExp.get())
                empList.delete(0, END)
                empList.insert(END,(empID.get(), empName.get(), empDesig.get(), empDOB.get(),empJoining.get(), empPhone.get(), empSalary.get(), empAllowance.get(),empMedicExp.get()))
        def DisplayData():
            empList.delete(0, END)
            for row in MainModule.View_Data():
                empList.insert(END,row, str(""))
          
         
        def empRec(event):
            global sd
            searchStd= empList.curselection()[0]
            sd= empList.get(searchStd)
            
            self.txtEmpId.delete(0, END)
            self.txtEmpId.insert(END, sd[0])
            self.txtEmpName.delete(0, END)
            self.txtEmpName.insert(END, sd[1])
            self.txtDesig.delete(0, END)
            self.txtDesig.insert(END, sd[2])
            self.txtEmpDOB.delete(0, END)
            self.txtEmpDOB.insert(END, sd[3])
            self.txtEmpJoining.delete(0, END)
            self.txtEmpJoining.insert(END, sd[4])
            self.txtEmpPhone.delete(0, END)
            self.txtEmpPhone.insert(END, sd[5])
            self.txtEmpEmail.delete(0, END)
            self.txtEmpEmail.insert(END, sd[6])
            self.txtEmpSalary.delete(0, END)
            self.txtEmpSalary.insert(END, sd[7])
            self.txtEmpAllowance.delete(0, END)
            self.txtEmpAllowance.insert(END, sd[8])
            self.txtEmpMedical.delete(0, END)
            self.txtEmpMedical.insert(END, sd[9])
            self.txtEmpTax.delete(0, END)
            self.txtEmpTax.insert(END, sd[10])
            self.txtEmpLeave.delete(0, END)
            self.txtEmpLeave.insert(END, sd[11])
            
        
        def deleteData():
            if(len(empID.get())!=0):
                MainModule.Delete_Employee(sd[0])
                clearData()
                DisplayData()
        def searchDB():
            empList.delete(0,END)
            row = MainModule.Search_Data(empID.get(), empName.get(), empDesig.get(), empDOB.get(), empJoining.get(), empPhone.get(), empSalary.get(), empAllowance.get(), empMedicExp.get())
            for employee in row:
                empList.insert(END,employee,str(""))
            
        def update():
            if(len(empID.get())!=0):
                MainModule.Manage_Employee(empID.get(), empName.get(), empDesig.get(), empDOB.get(), empJoining.get(), empPhone.get(), empEmail.get(), empSalary.get(), empAllowance.get(), empMedicExp.get(),empTax.get(),empLeave.get())  
                empList.delete(0, END)
                empList.insert(END, empID.get(), empName.get(), empDesig.get(), empDOB.get(), empJoining.get(), empPhone.get(), empEmail.get(), empSalary.get(), empAllowance.get(), empMedicExp.get())
                
#_______________________________________________________________________________________________________
        
        MainFrame= Frame(self.master, bg="snow3")
        MainFrame.pack()
        
        titFrame= Frame(MainFrame, bd=2, padx=24, pady=8,bg="snow3", relief=RIDGE)
        titFrame.pack(side=TOP)
        

       # self.lbTit= Label(titFrame, text="HR Management Systems", font=("Arial,", 25), bg="snow3")
       # self.lbTit.grid(pady=20)
        
        buttonFrame= Frame(MainFrame, bd=2, width=1350, height=50, padx=10, pady=20, relief=RIDGE, bg="snow3")
        buttonFrame.pack(side=BOTTOM, pady=20)
         
        DataFrame= Frame(MainFrame, bd=1, width=1000, height= 400, padx=20, pady=20,bg="snow3", relief=RIDGE)
        DataFrame.pack(side=BOTTOM,pady=20)
         
        DataFrameLeft= LabelFrame(DataFrame, text= "Employee Info \n" ,bd=1, width=1000, height= 600, padx=20, pady=20,bg="snow3",font=("Arial,", 20) ,relief=RIDGE)
        DataFrameLeft.pack(side=LEFT)
         
        DataFrameRight= LabelFrame(DataFrame, bd=1, text= "Employee Details \n", font=("Arial,", 15),width=450, height= 250, padx=31,bg="snow3", relief=RIDGE)
        DataFrameRight.pack(side=RIGHT, padx=20)
    
    #____________________________________________Labels & Entries___________________________________________________________________
        self.lbEmpId= Label(DataFrameLeft, text="Employee ID:", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpId.grid(row=0, column=0, sticky=W)
        
        self.txtEmpId= Entry(DataFrameLeft, textvariable=empID, font=("Arial,", 10), width=30)
        self.txtEmpId.grid(row=0, column=1, sticky=W)
        
        self.lbEmpName= Label(DataFrameLeft, text="Employee Name:", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpName.grid(row=1, column=0, sticky=W)
        
        self.txtEmpName= Entry(DataFrameLeft, textvariable=empName, font=("Arial,", 10), width=30)
        self.txtEmpName.grid(row=1, column=1, sticky=W)
        
        self.lbEmpDesig= Label(DataFrameLeft, text="Employee Designation", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpDesig.grid(row=2, column=0, sticky=W)
        
        self.txtDesig= Entry(DataFrameLeft, textvariable=empDesig, font=("Arial,", 10), width=30)
        self.txtDesig.grid(row=2, column=1, sticky=W)
        
        self.lbEmpDOB= Label(DataFrameLeft, text="Employee DoB", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpDOB.grid(row=3, column=0, sticky=W)
        
        self.txtEmpDOB= Entry(DataFrameLeft, textvariable=empDOB, font=("Arial,", 10), width=30)
        self.txtEmpDOB.grid(row=3, column=1, sticky=W)
        
        self.lbEmpJoining= Label(DataFrameLeft, text="Employee Join Date:", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpJoining.grid(row=4, column=0, sticky=W)
        
        self.txtEmpJoining= Entry(DataFrameLeft, textvariable=empJoining, font=("Arial,", 10), width=30)
        self.txtEmpJoining.grid(row=4, column=1, sticky=W)
        
        self.lbEmpPhone= Label(DataFrameLeft, text="Employee Phone Number:", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpPhone.grid(row=5, column=0, sticky=W)
        
        self.txtEmpPhone= Entry(DataFrameLeft, textvariable=empPhone, font=("Arial,", 10), width=30)
        self.txtEmpPhone.grid(row=5, column=1, sticky=W)
        
        self.lbEmpEmail= Label(DataFrameLeft, text="Employee Email", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpEmail.grid(row=6, column=0, sticky=W)
        
        self.txtEmpEmail= Entry(DataFrameLeft, textvariable=empEmail, font=("Arial,", 10), width=30)
        self.txtEmpEmail.grid(row=6, column=1, sticky=W)
        
        self.lbEmpSalary= Label(DataFrameLeft, text="Basic Salary:", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpSalary.grid(row=7, column=0, sticky=W)
        
        self.txtEmpSalary= Entry(DataFrameLeft, textvariable=empSalary, font=("Arial,", 10), width=30)
        self.txtEmpSalary.grid(row=7, column=1, sticky=W)
        
        self.lbEmpAllowance= Label(DataFrameLeft, text="Allowance:", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpAllowance.grid(row=8, column=0, sticky=W)
        
        self.txtEmpAllowance= Entry(DataFrameLeft, textvariable=empAllowance, font=("Arial,", 10), width=30)
        self.txtEmpAllowance.grid(row=8, column=1, sticky=W)
        
        self.lbEmpMedical= Label(DataFrameLeft, text="Medical Expense: ", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpMedical.grid(row=9, column=0, sticky=W)
        
        self.txtEmpMedical= Entry(DataFrameLeft, textvariable=empMedicExp, font=("Arial,", 10), width=30)
        self.txtEmpMedical.grid(row=9, column=1, sticky=W)
        
        self.lbEmpTax= Label(DataFrameLeft, text="Tax: ", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpTax.grid(row=10, column=0, sticky=W)
        
        self.txtEmpTax= Entry(DataFrameLeft, textvariable=empTax, font=("Arial,", 10), width=30)
        self.txtEmpTax.grid(row=10, column=1, sticky=W)
        
        self.lbEmpLeave= Label(DataFrameLeft, text="Leave: ", font=("Arial,", 10), bg="snow3", pady=2,padx=2)
        self.lbEmpLeave.grid(row=11, column=0, sticky=W)
        
        self.txtEmpLeave= Entry(DataFrameLeft, textvariable=empLeave, font=("Arial,", 10), width=30)
        self.txtEmpLeave.grid(row=11, column=1, sticky=W)
        #____________________________________________ListBox & ScrollBar___________________________________________________________________
        scroll= Scrollbar(DataFrameRight)
        scroll.grid(row=0,column=1, sticky='ns')
        
        empList= Listbox(DataFrameRight, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=scroll.set)
        empList.bind('<<ListboxSelect>>', empRec)
        empList.grid(row=0,column=0, padx=8)
        
        scroll.config(command= empList.yview())
        #____________________________________________Button___________________________________________________________________

        self.btnAddDate=Button(buttonFrame, command=addData, text="Add New", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=0)
        
        self.btnAddDate=Button(buttonFrame, command=DisplayData, text="Display", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=1)
        
        self.btnAddDate=Button(buttonFrame, command=deleteData ,text="Delete", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=2)
        
        self.btnAddDate=Button(buttonFrame, command= searchDB,text="Search", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=3)
        
        self.btnAddDate=Button(buttonFrame, command=update, text="Update", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=4)
        
        self.btnAddDate=Button(buttonFrame,command=clearData, text="Clear", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=5)
        
        self.btnAddDate=Button(buttonFrame, command=sendSlip, text="Send Salary", font=("arial",10,"bold"), height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=6)
        
        self.btnAddDate=Button(buttonFrame, text="Log Out", font=("arial",10,"bold"), command=iexit,height=1, width=10, bd=4)
        self.btnAddDate.grid(row=0, column=7)
        
if __name__=='__main__':
    main()