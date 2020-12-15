import sqlite3
from _overlapped import NULL

from datetime import datetime
import smtplib
from _ast import If
conn = sqlite3.connect('Project.db')

c = conn.cursor()
conn.commit()

#EmployeeSalary
def Salary_Calculation(  Basic_Salary , Allowance   , Medical , Leave , Tax ):
    GrossSalary = (Basic_Salary + Allowance + Medical)
    Expenses = (Tax + Leave )
    Total_Salary = GrossSalary - Expenses
    
    return Total_Salary

def getEmployeeSalary(id):
    
    with conn:
        c.execute("SELECT Basic_Salary FROM EmployeeDetails WHERE ID = ?", (id,))
        basic_salary = c.fetchone()[0]
        c.execute("SELECT Allowance FROM EmployeeDetails WHERE ID = ?", (id,))
        allowance =c.fetchone()[0]
        c.execute("SELECT Medical_Expenses FROM EmployeeDetails WHERE ID = ?", (id,))
        medical =c.fetchone()[0]
        c.execute("SELECT Leaves FROM EmployeeDetails WHERE ID = ?", (id,))
        leave = c.fetchone()[0]
        c.execute("SELECT Tax FROM EmployeeDetails WHERE ID = ?" , (id,))
        tax = c.fetchone()[0]
        
    leaveMinus = ( 500*leave )
    
    total = Salary_Calculation(basic_salary, allowance, medical, leaveMinus, tax)
    return total
    
    
#AddingEmployee
def Add_Employee(id , Name , Designation , DoB , Joindate , PhoneNumber  , mail, BasicSalary, Allowance, MedicalExpens):
    with conn:
        c.execute("SELECT ID From EmployeeDetails ")
    items = c.fetchall()
    checkid = int(id)
    Check = True
    for item in items: 
        if checkid == item[0]:
            Check = False
        
    if Check:
        c.execute("INSERT INTO EmployeeDetails VAlUES ( ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0)", (id , Name , Designation , DoB , Joindate , PhoneNumber , mail, BasicSalary, Allowance, MedicalExpens))
         
#EmployeeAttendace
def Add_Attendance():
    return NULL


#SendingMail Functionality (Done)
def sendEmail(to,msg):
    GMAIL_ID = 'hmanager37@gmail.com'
    GMAIL_PSWD = 'HelloWorld1'
    s= smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to,msg)
    s.quit()
    
def Salary_Slip(id):
    
    
    current_month_text = datetime.now().strftime('%B')
    Subject= f"Salary for the month of {current_month_text} has been sent."
    with conn:
        c.execute("SELECT Name FROM EmployeeDetails WHERE ID = ?" , (id,))
        name = c.fetchone()[0]
        c.execute("SELECT Email FROM EmployeeDetails WHERE ID = ?" , (id,))
        mail = c.fetchone()[0]
    
    Salary = getEmployeeSalary(id)
    body = f"Hello {name}, Your Salary for this month has been Sent. which amounts to a total of = {Salary}/-"
    msg = f'Subject: {Subject}\n\n{body}'
    sendEmail(mail, msg)
    


#updating employee
def Manage_Employee(id , name , designation , DoB , Joindate , PhoneNumber , mail , BasicSalary, Allowance, MedicalExpens , tax , leave):
    with conn:
        c.execute("""UPDATE EmployeeDetails SET Name = ? 
                     , Designation = ? , Date_of_Birth = ? 
                     , Joined_Date = ? , Phone_Number = ? 
                     , Basic_Salary = ? , Allowance = ? 
                     , Medical_Expenses = ? , Tax = ? 
                     , Leaves = ?  , Email = ? 
                     WHERE id = ?""" , ( name , designation , DoB , Joindate , PhoneNumber , BasicSalary, Allowance, MedicalExpens , tax ,leave , mail, id ))
         
#DeleteEmployee
def Delete_Employee(id):
    with conn:
        c.execute("DELETE FROM EmployeeDetails WHERE ID = ?" , (id,))
    
def View_Data():
    with conn:
        c.execute("SELECT * FROM EmployeeDetails")
        row=c.fetchall()
    return row

def Search_Data(empID="", empName="", empDesig="", empDOB="",empJoining="", empPhone="", empSalary="", empAllowance="",empMedicExpense=""):
    with conn:
        c.execute("SELECT * FROM EmployeeDetails WHERE ID=? OR Name=? OR Designation=? OR Date_of_Birth=? OR Joined_Date=? OR Phone_Number=? OR Basic_Salary=? OR Allowance=? OR Medical_Expenses=?",(empID, empName, empDesig, empDOB,empJoining, empPhone, empSalary, empAllowance,empMedicExpense))
        row = c.fetchall()
    return row
