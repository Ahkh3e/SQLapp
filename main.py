import streamlit as st
import cx_Oracle
import pandas as pd
from PIL import Image
import getpass
import os
from dotenv import load_dotenv

load_dotenv()
ORCL_USER = os.getenv('ORCL_USER')
ORCL_PASSWD = os.getenv('ORCL_PASSWD')

dsnStr = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
conn = cx_Oracle.connect(ORCL_USER,ORCL_PASSWD, dsn=dsnStr)
print (conn.version)

loggedin= False

st.title("Emergency Management System")
cur = conn.cursor()

def employee():
    cur.execute("""
    select * from EMPLOYEE
    """)

    pull = cur.fetchall()

    Employeedf = pd.DataFrame(pull, columns = ['FULLNAME','SIN','EMPLOYEEID','EMPLOYEETYPE'])
    print(Employeedf)
    return(Employeedf)

def logic():
    cur.execute("""
    select * from LOGISTICS
    """)
    pull = cur.fetchall()

    Logicdf = pd.DataFrame(pull, columns = ['NUMPATIENT', 'NUMDOCTOR', 'NUMNURSE', 'NUMBEDS', 'LOGISTICSDATE'])
    print(Logicdf)
    return (Logicdf)

def account():
    cur.execute("""
    select * from ACCOUNT
    """)
    pull = cur.fetchall()

    Accountdf = pd.DataFrame(pull, columns = ['USERNAME', 'PASSWORD', 'EMP_PRIVILEGE', 'EMPLOYEEID'])
    print(Accountdf)
    return(Accountdf)

def bed():
    cur.execute("""
    select * from BED
    """)
    pull = cur.fetchall()

    Beddf = pd.DataFrame(pull, columns = ['BED_ID', 'PATIENTID', 'OCCUPIED'])
    print(Beddf)
    return(Beddf)

def date_admit():
    cur.execute("""
    select * from DATE_ADMITTED
    """)
    pull = cur.fetchall()

    Date_admitdf = pd.DataFrame(pull, columns = ['DATE_RELEASED', 'LOGISTICSDATE', 'PATIENTID'])
    print(Date_admitdf)
    return(Date_admitdf)
    
def doctor():
    cur.execute("""
    select * from DOCTORS
    """)
    pull = cur.fetchall()

    Doctorsdf = pd.DataFrame(pull, columns = ['SPECIALIZATION', 'EMPLOYEEID'])
    print(Doctorsdf)
    return (Doctorsdf)

def emergency():
    cur.execute("""
    select * from EMERGENCY_CONTACT
    """)
    pull = cur.fetchall()

    Emergencydf = pd.DataFrame(pull, columns = ['FULLNAME', 'RELATION', 'TEL_NUMBER', 'ADDRESS', 'PATIENTID'])
    print(Emergencydf)
    return(Emergencydf)

def law():
    cur.execute("""
    select * from LAW_ENFORCEMENT
    """)
    pull = cur.fetchall()

    Lawdf = pd.DataFrame(pull, columns = ['PROFESSION', 'EMPLOYEEID'])
    print(Lawdf)
    return(Lawdf)

def medicine():
    cur.execute("""
    select * from MEDICINE
    """)
    pull = cur.fetchall()

    Medicinedf = pd.DataFrame(pull, columns = ['MEDICINE_ID', 'NAME', 'DESCRIPTION', 'INVENTORY'])
    print(Medicinedf)
    return(Medicinedf)

def medicinepre():
    cur.execute("""
    select * from MEDICINE_PRESCRIPTION
    """)
    pull = cur.fetchall()

    MedicinePredf = pd.DataFrame(pull, columns = ['MEDICINE_ID', 'PATIENTID', 'DOSAGE', 'CONSUMPTION_CYCLE'])
    print(MedicinePredf)
    return(MedicinePredf)

def nurse():
    cur.execute("""
    select * from NURSES
    """)
    pull = cur.fetchall()

    Nursesdf = pd.DataFrame(pull, columns = ['EMPLOYEEID', 'SPECIALIZATION'])
    print(Nursesdf)
    return(Nursesdf)

def op_staff():
    cur.execute("""
    select * from OPERATIONS_STAFF
    """)
    pull = cur.fetchall()

    OpStaffdf = pd.DataFrame(pull, columns = ['JOB_TITLE', 'EMPLOYEEID'])
    print(OpStaffdf)
    return(OpStaffdf)

def patients():
    cur.execute("""
    select * from PATIENTS
    """)
    pull = cur.fetchall()

    Patientsdf = pd.DataFrame(pull, columns = ['PATIENTID', 'FULLNAME', 'AGE', 'GENDER', 'SIN', 'HEALTH_CN', 'SYMPTOMS'])
    print(Patientsdf)
    return(Patientsdf)

def schedule():
    cur.execute("""
    select * from SCHEDULE
    """)
    pull = cur.fetchall()

    Scheduledf = pd.DataFrame(pull, columns = ['WORKDATE', 'CLOCK_IN', 'CLOCK_OUT', 'EMPLOYEEID'])
    print(Scheduledf)
    return(Scheduledf)

def Query1():
    cur.execute("""
    SELECT e.fullName, e.employeeID, e.employeeType, n.specialization
FROM Nurses n, Employee e
WHERE e.EmployeeID = n.EmployeeID
UNION
SELECT e.fullName, e.employeeID, e.employeeType, d.specialization
FROM Doctors d, Employee e
WHERE e.EmployeeID = d.EmployeeID
ORDER BY fullName ASC
    """)
    pull = cur.fetchall()

    query1 = pd.DataFrame(pull,columns = ['FULLNAME','EMPLOYEE ID','EMPLOYEE TYPE','SPECIALIZATION'])
    print(query1)
    return(query1)

def Query2():
    cur.execute("""
    SELECT p.fullname, p.patientId, m.name, m.medicine_ID, m.description, mp.dosage, mp.consumption_cycle
FROM Patients p, Medicine_prescription mp, Medicine m
WHERE p.PatientID = mp.PatientID AND mp.Medicine_ID = m.Medicine_ID
    """)
    pull = cur.fetchall()

    query2 = pd.DataFrame(pull,columns = ['FULL NAME','PATIENTID','MEDICINE NAME','MEDICINE ID','DESCRIPTION','USAGE','CONSUMPTION CYCLE'])
    print(query2)
    return(query2)

def Query3():
    cur.execute("""
    SELECT DISTINCT p.fullName, b.Bed_ID, b.Occupied, l.LogisticsDate, da.date_released, (da.date_released - l.logisticsDate) AS NumDays
FROM Bed b, Patients p, Logistics l, Date_admitted da
WHERE p.patientID = b.patientID AND p.patientID = da.patientID AND da.LOGISTICSDATE = l.LOGISTICSDATE
ORDER BY occupied ASC
    """)
    pull = cur.fetchall()

    query3 = pd.DataFrame(pull,columns = ['FULL NAME','BED ID','OCCUPIED','LOGISTIC DATE','DATE RELEASED','DAYS ADMITTED'])
    print(query3)
    return(query3)

def Query4():
    cur.execute("""
    SELECT DISTINCT emp.Employeetype, emp.fullname, acc.username, acc.password, acc.EMP_privilege
FROM Employee emp, Account acc
WHERE acc.employeeID = emp.employeeID
ORDER BY emp_privilege DESC
    """)
    pull = cur.fetchall()

    query4 = pd.DataFrame(pull,columns = ['EMPLOYEE TYPE','FULL NAME','USERNAME','PASSWORD','PRIVILEGE'])
    print(query4)
    return(query4)

def Query5():
    cur.execute("""SELECT *
    FROM Patients
    MINUS
    SELECT *
    FROM PATIENTS
    WHERE Symptoms = 'Nausea'
    """)
    pull = cur.fetchall()

    query5 = pd.DataFrame(pull, columns =['PATIENT ID', 'FULLNAME','AGE','GENDER','SIN','HEALTH CARD','SYMPTOMS'] )
    print(query5)
    return(query5)

def Query6():
    cur.execute("""SELECT DISTINCT *
FROM Medicine
    """)
    pull = cur.fetchall()

    query6 = pd.DataFrame(pull, columns =['MEDICINE ID','MEDICINE NAME','DESCRIPTION','INVENTORY'] )
    print(query6)
    return(query6)

def Query7():
    cur.execute("""SELECT p.PatientID, p.FullName, p.Symptoms, ec.fullname AS Emergency_Contact_Name, ec.relation, ec.tel_number
From Patients p, Emergency_Contact ec
WHERE p.Age <= 21 AND p.PatientID = ec.PatientID
    """)
    pull = cur.fetchall()

    query7 = pd.DataFrame(pull, columns =['PATIENT ID','FULL NAME','SYMPTOMS','EMERGENCY CONTACT','RELATION','TELEPHONE NUMBER'] )
    print(query7)
    return(query7)

def Query8():
    cur.execute("""
SELECT e.fullName, e.employeeID, e.employeeType, n.specialization
FROM Nurses n, Employee e
WHERE e.EmployeeID = n.EmployeeID
UNION
SELECT e.fullName, e.employeeID, e.employeeType, d.specialization
FROM Doctors d, Employee e
WHERE e.EmployeeID = d.EmployeeID
UNION
SELECT e.fullName, e.employeeID, e.employeeType, os.job_title
FROM Operations_Staff os, Employee e
WHERE e.EmployeeID = os.EmployeeID
UNION
SELECT e.fullName, e.employeeID, e.employeeType, le.profession
FROM Law_enforcement le, Employee e
WHERE e.EmployeeID = le.EmployeeID
ORDER BY employeeType ASC
    """)
    pull = cur.fetchall()

    query8 = pd.DataFrame(pull, columns =['FULL NAME','EMPLOYEE ID','EMPLOYEE TYPE','SPECIALIZATION'] )
    print(query8)
    return(query8)
#SchoolDb	m534khan@//oracle.scs.ryerson.ca:1521/orcl
base = st.selectbox('Select Demo Function',('Create All Tables','Drop all Tables','Fill All Tables','GUI DEMO'))

if base == 'Create All Tables':
    if st.button('Submit'):
        cur.execute("""
CREATE TABLE Logistics (
NumPatient NUMBER(10) NOT NULL,
NumDoctor NUMBER(10) NOT NULL,
NumNurse NUMBER(10) NOT NULL,
NumBeds NUMBER(10) NOT NULL ,
LogisticsDate DATE NOT NULL,
PRIMARY KEY(LogisticsDate)
)""")

        cur.execute("""
CREATE TABLE Employee(
FullName VARCHAR2(25) NOT NULL,
SIN NUMBER(7,0),
EmployeeID NUMBER(10) NOT NULL,
EmployeeType VARCHAR2(20) NOT NULL CHECK (EmployeeType IN ('doctor', 'nurses', 'law enforcement', 'operations staff')),
PRIMARY KEY(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE account (
Username VARCHAR2(20) PRIMARY KEY,
Password VARCHAR2(20) NOT NULL,
Emp_Privilege CHAR(1) NOT NULL,
EmployeeID NUMBER(10),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE schedule (
WorkDate DATE,
Clock_In TIMESTAMP NOT NULL,
Clock_Out TIMESTAMP NOT NULL,
EmployeeID NUMBER(10),
PRIMARY KEY (WorkDate),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE doctors (
Specialization VARCHAR2(20) NOT NULL,
EmployeeID Number(10),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE nurses (
EmployeeID NUMBER(10),
Specialization VARCHAR2(40) NOT NULL,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE Law_Enforcement (
Profession VARCHAR2(20) NOT NULL,
EmployeeID Number(10),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE Operations_Staff (
Job_title VARCHAR2(40) NOT NULL,
EmployeeID NUMBER(10),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)""")

        cur.execute("""
CREATE TABLE Patients (
PatientID NUMBER(10) NOT NULL,
FullName VARCHAR2(200) NOT NULL,
Age NUMBER(5) NOT NULL,
Gender CHAR NOT NULL,
SIN NUMBER(5) NOT NULL,
Health_CN NUMBER(14,0) NOT NULL,
Symptoms VARCHAR2(200)NOT NULL,
PRIMARY KEY (PatientID)
)""")

        cur.execute("""
CREATE TABLE Date_Admitted (
Date_released DATE DEFAULT NULL,
LogisticsDate DATE NOT NULL,
PatientID NUMBER(10)NOT NULL,
FOREIGN KEY (LogisticsDate) REFERENCES Logistics(LogisticsDate),
FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
)""")

        cur.execute("""
CREATE TABLE Bed(
Bed_ID NUMBER(5) ,
PatientID NUMBER(10) NOT NULL,
Occupied CHAR DEFAULT 'N',
PRIMARY KEY (Bed_ID),
FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
)""")

        cur.execute("""
CREATE TABLE Medicine(
Medicine_ID NUMBER (20,0) PRIMARY KEY,
Name VARCHAR2(20) NOT NULL,
Description VARCHAR2(100)NOT NULL,
Inventory NUMBER(20,0)NOT NULL
)""")

        cur.execute("""
CREATE TABLE Emergency_Contact(
FullName VARCHAR2(200) NOT NULL,
Relation VARCHAR2(200) NOT NULL,
Tel_Number NUMBER(10) NOT NULL,
Address VARCHAR2 (50) NOT NULL,
PatientID NUMBER(10),
FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
)""")

        cur.execute("""
CREATE TABLE Medicine_Prescription(
Medicine_ID NUMBER (20,0) NOT NULL,
PatientID NUMBER(10) NOT NULL,
Dosage VARCHAR2(20)NOT NULL,
Consumption_Cycle VARCHAR2 (100) NOT NULL,
FOREIGN KEY (Medicine_ID) REFERENCES Medicine(Medicine_ID),
FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
)
""")

if base == 'Drop all Tables':
    if st.button('Submit'):
        cur.execute("DROP TABLE Employee CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE account CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE schedule CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE doctors CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE nurses CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Date_Admitted CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Law_Enforcement CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Operations_Staff CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Logistics CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Patients CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Bed CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Medicine CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Emergency_Contact CASCADE CONSTRAINTS")
        cur.execute("DROP TABLE Medicine_Prescription CASCADE CONSTRAINT")
    
if base == 'Fill All Tables':
    if st.button('Submit'):
        cur.execute("""
INSERT INTO LOGISTICS
VALUES(1,2,4,100,TO_DATE('26/10/2020','DD/MM/YYYY'))""")

        cur.execute("""
INSERT INTO LOGISTICS
VALUES(3,2,4,100,TO_DATE('28/10/2020','DD/MM/YYYY'))""")

        cur.execute("""
INSERT INTO LOGISTICS
VALUES(2,2,4,100,TO_DATE('10/11/2020','DD/MM/YYYY'))""")

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Ahmed Khan', '12345','00001','doctor')""")

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Jules Gammad', '01234','00002','doctor')""")

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Jane Doe', '12334','00003','nurses')""")
      
        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('John Doe', '12445','00004','nurses')""")

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Tatiana Mesau', '12355','00005','nurses')""") 

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Constantino Mello', '11345','00006','nurses')""") 

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Christopher Jielo ', '11340','00007','operations staff')""") 

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Melani Tot', '10045','00008','operations staff')""") 

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Teo Mani', '00345','00009','law enforcement')""")

        cur.execute("""
INSERT INTO EMPLOYEE
VALUES('Ian Refut', '11305','00010','law enforcement')""")

        cur.execute("""
INSERT INTO account
VALUES('admin', 'cusadmin', 'A', '00007')""")

        cur.execute("""
INSERT INTO account
VALUES('admin2', 'cusadmin2', 'A', '00008')""")

        cur.execute("""
INSERT INTO account
VALUES('akhan', 'admin', 'B', '00001')""")

        cur.execute("""
INSERT INTO account
VALUES('jgammad', 'admin', 'B', '00002')""")

        cur.execute("""
INSERT INTO doctors
VALUES('General Surgery', '00001')""")

        cur.execute("""
INSERT INTO doctors
VALUES('Neurosurgery', '00002')""")

        cur.execute("""
INSERT INTO nurses
VALUES('00003', 'Registered Nurse')""")

        cur.execute("""
INSERT INTO nurses
VALUES('00004', 'Medical-surgical Nurse')""")

        cur.execute("""
INSERT INTO nurses
VALUES('00005', 'Intensive Care Unit Registered Nurse')""")

        cur.execute("""
INSERT INTO nurses
VALUES('00006', 'Nursing Assistant')""")

        cur.execute("""
INSERT INTO Law_Enforcement
VALUES('Police', '00009')""")

        cur.execute("""
INSERT INTO Law_Enforcement
VALUES('Fireman', '00010')""")

        cur.execute("""
INSERT INTO Operations_Staff
VALUES('Front-desk Specialist', '00007')""")

        cur.execute("""
INSERT INTO Operations_Staff
VALUES('Operations Manager', '00008')""")

        cur.execute("""
INSERT INTO Patients
VALUES('1','Dominique Rodriguez', '20', 'M', '12312', '78012','Nausea')""")

        cur.execute("""
INSERT INTO Patients
VALUES('2','Allyson Teofima', '32', 'F', '11312', '32012','Nausea')""")

        cur.execute("""
INSERT INTO Patients
VALUES('3','Merci Tefioux', '26', 'M', '12332', '18542','Flu')""")

        cur.execute("""
INSERT INTO Patients
VALUES('4','Anderson Silva', '29', 'M', '13222', '53902','Internal Bleeding')""")

        cur.execute("""
INSERT INTO Patients
VALUES('5','Monica Mercedes', '16', 'F', '12312', '98012','Flu')""")

        cur.execute("""
INSERT INTO Patients
VALUES('6','Brook Lopez', '20', 'M', '15512', '23012','Flu')""")

        cur.execute("""
INSERT INTO Bed
VALUES('1','1', DEFAULT)""")

        cur.execute("""
INSERT INTO Bed
VALUES('2','2', DEFAULT)""")

        cur.execute("""
INSERT INTO Bed
VALUES('3','3', 'Y')""")

        cur.execute("""
INSERT INTO Bed
VALUES('4','4', 'Y')""")

        cur.execute("""
INSERT INTO Bed
VALUES('5','5', DEFAULT)""")

        cur.execute("""
INSERT INTO Bed
VALUES('6','6', 'Y')""")

        cur.execute("""
INSERT INTO MEDICINE
VALUES('1','Ibuprofen','Painkiller','200')""")

        cur.execute("""
INSERT INTO MEDICINE
VALUES('2','Zofran','Anti-nausea','50')""")

        cur.execute("""
INSERT INTO MEDICINE
VALUES('3','Zanamivir','Flu medicine', '2000')""")

        cur.execute("""
INSERT INTO Emergency_Contact
VALUES('Dayane Silva', 'Wife', '416322091','1532 John Street', '4')""")

        cur.execute("""
INSERT INTO Emergency_Contact
VALUES ('Rafael Lopez', 'Brother', '3123244500','1420 Leli Drive', '6')""")

        cur.execute("""
INSERT INTO Emergency_Contact
VALUES('Melina Mercedes', 'Mother', '415900213','501 Shelby Drive', '5')""")

        cur.execute("""
INSERT INTO Emergency_Contact
VALUES('Dwayne Rodriguez', 'Father', '516321021','151 Toute Ave', '1')""")

        cur.execute("""
INSERT INTO Medicine_Prescription
VALUES('1','4','3 times a day', '3 months')""")

        cur.execute("""
INSERT INTO Medicine_Prescription
VALUES('2','1','1 times a day', '1 week')""")

        cur.execute("""
INSERT INTO Medicine_Prescription
VALUES('3','3','2 times a day', '1 month')""")

        cur.execute("""
INSERT INTO Date_Admitted
VALUES(TO_DATE('26/11/2020','DD/MM/YYYY'), TO_DATE('26/10/2020','DD/MM/YYYY'), '1')""")

        cur.execute("""
INSERT INTO Date_Admitted
VALUES(TO_DATE('15/11/2020','DD/MM/YYYY'), TO_DATE('28/10/2020','DD/MM/YYYY'), '2')""")

        cur.execute("""
INSERT INTO Date_Admitted
VALUES(DEFAULT, TO_DATE('28/10/2020','DD/MM/YYYY'), '3')""")

        cur.execute("""
INSERT INTO Date_Admitted
VALUES(DEFAULT, TO_DATE('28/10/2020','DD/MM/YYYY'), '4')""")

        cur.execute("""
INSERT INTO Date_Admitted
VALUES(TO_DATE('12/12/2020','DD/MM/YYYY'), TO_DATE('10/11/2020','DD/MM/YYYY'), '5')""")

        cur.execute("""
INSERT INTO Date_Admitted
VALUES(DEFAULT, TO_DATE('10/11/2020','DD/MM/YYYY'), '6')""")

if base == 'GUI DEMO':
    image = Image.open('hospital.jpg')

    
    st.image(image, use_column_width = True)
    st.title("Login")

    username = st.text_input('Username:', value = "")
    password = st.text_input('Password:', value = "", type = "password")
    stay = st.checkbox('Log In')

    _account = account()
    if username != "" and password != "" and stay:
        for users in  range(len(_account)):
            if _account['USERNAME'][users] == username:
                print('here')
                if _account['PASSWORD'][users] == password:
                    use = users
                    print('here agin')
                    loggedin = True
   
            
    if loggedin == True and stay and _account['EMP_PRIVILEGE'][use]=='A':
    
        options = st.selectbox('Select Table to display',(
            'Employee', 'Logistics', 'Account', 'Bed Information',
            'Date of Admittance', 'List of Doctors','Emergency Contacts',
            'List of Law Enforcement','Medicine Inventory',
            'Medicine Prescriptions','List of Nurses','Operations Staff','Patients','View Doctors and Nurses','Occupied Beds','Employee Accounts','View Emloyees'))

        if options == 'Employee':
            source = employee
        if options == 'Logistics':
            source = logic
        if options == 'Account':
            source = account
        if options == 'Bed Information':
            source = bed
        if options == 'Date of Admittance':
            source = date_admit
        if options == 'List of Doctors':
            source = doctor
        if options == 'Emergency Contacts':
            source = emergency
        if options == 'List of Law Enforcement':
            source = law
        if options == 'Medicine Inventory':
            source = medicine
        if options == 'Medicine Prescriptions':
            source = medicinepre
        if options == 'List of Nurses':
            source = nurse
        if options == 'Operations Staff':
            source = op_staff
        if options == 'Patients':
            source = patients
        if options == 'View Doctors and Nurses':
            source = Query1
        if options == 'Occupied Beds':
            source = Query3
        if options =='Employee Accounts':
            source = Query4
        if options == 'View Emloyees':
            source = Query8
   

        edit = st.checkbox('Enable Editing')
        if edit:
            add = st.radio('Select',('Add Information','Delete Information'))
            if add == 'Add Information':

                if options == 'Employee':
                   Fname = st.text_input('Full Name')
                   SIN = int(st.text_input('SIN',value = '1'))
                   empid = int(st.text_input('Employee ID',value = '1'))
                   Emptype = st.text_input('Employee Type')

                if options == 'Logistics':
                   nump = int(st.text_input('Number of Patients',value = '1'))
                   numd = int(st.text_input('Number of Doctors',value = '1'))
                   numn = int(st.text_input('Number of Nurses',value = '1'))
                   numb = int(st.text_input('Number of Beds',value = '1'))
                   logdate = st.text_input('Logistic Date')

                if options == 'Account':
                    usern = st.text_input('USERNAME')
                    passn = st.text_input('PASSWORD', type = 'password')
                    empp = st.text_input('Employee Privilege')
                    empid = int(st.text_input('Employee ID',value = '1'))

                if options == 'List of Doctors':
                    spec = st.text_input('Specialization')
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'List of Law Enforcement':
                    proff = st.text_input('Profession')
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'List of Nurses':
                    empid = int(st.text_input('Employee Id',value = '1'))
                    spec = st.text_input('Specialization')

                if options == 'Operations Staff':
                    spec = st.text_input('Job Title')
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'Bed Information':
                    Bed_id = st.text_input('Bed Id', value = '1')
                    Bed_id = int(Bed_id)
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
                    occupied = st.text_input('Occupied')

                if options == 'Date of Admittance':
                    datere = st.text_input('Date of Release')
                    logdate = st.text_input('logistic Date')
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
        
                if options == 'Emergency Contacts':
                    Fname = st.text_input('Full name')
                    Relation = st.text_input('Relation')
                    Tnum = st.text_input('Telephone Number', value = '1')
                    address = st.text_input('Address')
                    patid = st.text_input('Patient Id', value = '1')
                    Tnum = int(Tnum)
                    patid = int(patid)

                if options == 'Medicine Inventory':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)
                    Name = st.text_input('Name')
                    Desc = st.text_input('Description of Medication')
                    inv = st.text_input('Inventory', value = '1')
                    inv = int(inv)

                if options == 'Medicine Prescriptions':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
                    dosage = st.text_input('Dosage Prescription')
                    Consumpt = st.text_input('Consumption Cycle')

                if options == 'Patients':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
                    Fname = st.text_input('FUll Name')
                    Age = st.text_input('Age', value = '1')
                    Age = int(Age)
                    gender = st.text_input('Gender')
                    sin = st.text_input('SIN', value = '1')
                    sin = int(sin)
                    Healthcn = st.text_input('Health Card Number', value = '1')
                    Healthcn = int(Healthcn)
                    symtoms = st.text_input('Symptoms')

                if st.button('Submit'):
                    if options == 'Employee':
                        cur.execute('''INSERT INTO EMPLOYEE
    VALUES('%s', '%d','%d','nurses')'''%(Fname,SIN,empid,Emptype))
                
                    if options == 'Logistics':
                        cur.execute('''INSERT INTO LOGISTICS
    VALUES(%d,%d,%d,%d,TO_DATE('%s','DD/MM/YYYY'))'''%(nump,numd,numn,numb,logdate))
               
                    if options == 'Account':
                        cur.execute('''INSERT INTO account
    VALUES('%s', '%s', '%s', '%d')'''%(usern,passn,empp,empid))
                
                    if options == 'List of Doctors':
                        cur.execute('''INSERT INTO doctors
    VALUES('%s', '%d')'''%(spec,empid))
               
                    if options == 'List of Law Enforcement':
                        cur.execute('''INSERT INTO Law_Enforcement
    VALUES('%s', '%d')'''%(proff,empid))

                    if options == 'List of Nurses':
                        cur.execute('''INSERT INTO nurses
    VALUES('%d', '%s')'''%(empid, spec))
               
                    if options == 'Operations Staff':
                        cur.execute('''INSERT INTO Operations_Staff
    VALUES('%s', '%d')'''%(spec,empid))

                    if options == 'Bed Information':
                        cur.execute('''INSERT INTO Bed
        VALUES('%d','%d', '%s')'''%(Bed_id,patid,occupied))    

                    if options == 'Date of Admittance':
                        cur.execute('''INSERT INTO Date_Admitted
        VALUES(TO_DATE('%s','DD/MM/YYYY'), TO_DATE('%s','DD/MM/YYYY'), '%d')'''%(datere,logdate,patid))   
                        
                    if options == 'Emergency Contacts':
                        cur.execute('''INSERT INTO Emergency_Contact
        VALUES('%s', '%s', '%d','%s', '%d')'''%(Fname,Relation,Tnum,address,patid)) 

                    if options == 'Medicine Inventory':
                        cur.execute('''INSERT INTO MEDICINE
        VALUES('%d','%s','%s','%d')'''%(MedId,Name,Desc,inv)) 

                    if options == 'Medicine Prescriptions':
                        cur.execute('''INSERT INTO Medicine_Prescription
        VALUES('%d','%d','%s', '%s')'''%(MedId,patid,dosage,Consumpt)) 

                    if options == 'Patients':
                        cur.execute('''INSERT INTO PATIENTS
        VALUES('%d','%s', '%d', '%s', '%d', '%d','%s')'''%(patid,Fname,Age,gender,sin,Healthcn,symtoms))

            if add == 'Delete Information':
                if options == 'Employee':
                   empid = int(st.text_input('Employee ID',value = '1'))

                if options == 'Logistics':
                   logdate = st.text_input('Logistic Date')

                if options == 'Account':
                    usern = st.text_input('USERNAME')

                if options == 'List of Doctors':
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'List of Law Enforcement':
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'List of Nurses':
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'Operations Staff':
                    empid = int(st.text_input('Employee Id',value = '1'))

                if options == 'Bed Information':
                    Bed_id = st.text_input('Bed Id', value = '1')
                    Bed_id = int(Bed_id)

                if options == 'Date of Admittance':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)

                if options == 'Emergency Contacts':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)

                if options == 'Medicine Inventory':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)
               
                if options == 'Medicine Prescriptions':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)

                if options == 'Patients':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)

                if st.button('Submit'): 
                    if options == 'Employee':
                        cur.execute('''DELETE FROM EMPLOYEE
    WHERE EmployeeID = %d
    '''%(empid)) 

                    if options == 'Logistics':
                       cur.execute('''DELETE FROM LOGISTICS
    WHERE LogisticsDate = TO_DATE('%s','DD/MM/YYYY')'''%(logdate)) 

                    if options == 'Account':
                        cur.execute('''DELETE FROM account
    WHERE Username = %s'''%(usern)) 

                    if options == 'List of Doctors':
                        cur.execute('''DELETE FROM doctors
    WHERE EmployeeID = %d'''%(empid)) 

                    if options == 'List of Law Enforcement':
                        cur.execute('''DELETE FROM Law_Enforcement
    WHERE EmployeeID = %d'''%(empid)) 

                    if options == 'List of Nurses':
                        cur.execute('''DELETE FROM nurses
    WHERE EmployeeID = %d'''%(empid)) 

                    if options == 'Operations Staff':
                        cur.execute('''DELETE FROM Operations_Staff
    WHERE EmployeeID = %d'''%(empid)) 

                    if options == 'Bed Information':
                        cur.execute('''DELETE FROM Bed
    WHERE BED_id = %d'''%(Bed_id))    

                    if options == 'Date of Admittance':
                        cur.execute('''DELETE FROM Date_Admitted
    WHERE PatientID = %d'''%(patid))   
                        
                    if options == 'Emergency Contacts':
                        cur.execute('''DELETE FROM Emergency_Contact
    WHERE PatientID = %d'''%(patid)) 

                    if options == 'Medicine Inventory':
                        cur.execute('''DELETE FROM MEDICINE
    WHERE Medicine_ID = %d'''%(MedId)) 

                    if options == 'Medicine Prescriptions':
                        cur.execute('''DELETE FROM Medicine_Prescription
    WHERE Medicine_ID = %d'''%(MedId)) 

                    if options == 'Patients':
                        cur.execute('''DELETE FROM Patients
    WHERE PatientID = %d'''%(patid))
                
                conn.commit()
    
        st.table(source())

    

    if loggedin == True and stay and _account['EMP_PRIVILEGE'][use]=='B':
    
        options = st.selectbox('Select Table to display',('Bed Information',
            'Date of Admittance','Emergency Contacts','Medicine Inventory',
            'Medicine Prescriptions','Patients','Patient Prescriptions','Patients Without Nausea','Medicine Information','Young Patients'))

        if options == 'Bed Information':
            source = bed
        if options == 'Date of Admittance':
            source = date_admit
        if options == 'Emergency Contacts':
            source = emergency
        if options == 'Medicine Inventory':
            source = medicine
        if options == 'Medicine Prescriptions':
            source = medicinepre
        if options == 'Patients':
            source = patients
        if options == 'Patient Prescriptions':
            source = Query2
        if options == 'Patients Without Nausea':
            source = Query5
        if options == 'Medicine Information':
            source = Query6
        if options == 'Young Patients':
            source = Query7
        edit = st.checkbox('Enable Editing')
        if edit:
            add = st.radio('Select',('Add Information','Delete Information'))
            if add == 'Add Information':
            
                if options == 'Bed Information':
                    Bed_id = st.text_input('Bed Id', value = '1')
                    Bed_id = int(Bed_id)
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
                    occupied = st.text_input('Occupied')

                if options == 'Date of Admittance':
                    datere = st.text_input('Date of Release')
                    logdate = st.text_input('logistic Date')
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
        
                if options == 'Emergency Contacts':
                    Fname = st.text_input('Full name')
                    Relation = st.text_input('Relation')
                    Tnum = st.text_input('Telephone Number', value = '1')
                    address = st.text_input('Address')
                    patid = st.text_input('Patient Id', value = '1')
                    Tnum = int(Tnum)
                    patid = int(patid)

                if options == 'Medicine Inventory':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)
                    Name = st.text_input('Name')
                    Desc = st.text_input('Description of Medication')
                    inv = st.text_input('Inventory', value = '1')
                    inv = int(inv)

                if options == 'Medicine Prescriptions':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
                    dosage = st.text_input('Dosage Prescription')
                    Consumpt = st.text_input('Consumption Cycle')

                if options == 'Patients':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)
                    Fname = st.text_input('FUll Name')
                    Age = st.text_input('Age', value = '1')
                    Age = int(Age)
                    gender = st.text_input('Gender')
                    sin = st.text_input('SIN', value = '1')
                    sin = int(sin)
                    Healthcn = st.text_input('Health Card Number', value = '1')
                    Healthcn = int(Healthcn)
                    symtoms = st.text_input('Symptoms')

                if st.button('Submit'):
                    if options == 'Bed Information':
                        cur.execute('''INSERT INTO Bed
        VALUES('%d','%d', '%s')'''%(Bed_id,patid,occupied))    

                    if options == 'Date of Admittance':
                        cur.execute('''INSERT INTO Date_Admitted
        VALUES(TO_DATE('%s','DD/MM/YYYY'), TO_DATE('%s','DD/MM/YYYY'), '%d')'''%(datere,logdate,patid))   
                        
                    if options == 'Emergency Contacts':
                        cur.execute('''INSERT INTO Emergency_Contact
        VALUES('%s', '%s', '%d','%s', '%d')'''%(Fname,Relation,Tnum,address,patid)) 

                    if options == 'Medicine Inventory':
                        cur.execute('''INSERT INTO MEDICINE
        VALUES('%d','%s','%s','%d')'''%(MedId,Name,Desc,inv)) 

                    if options == 'Medicine Prescriptions':
                        cur.execute('''INSERT INTO Medicine_Prescription
        VALUES('%d','%d','%s', '%s')'''%(MedId,patid,dosage,Consumpt)) 

                    if options == 'Patients':
                        cur.execute('''INSERT INTO PATIENTS
        VALUES('%d','%s', '%d', '%s', '%d', '%d','%s')'''%(patid,Fname,Age,gender,sin,Healthcn,symtoms))

            if add == 'Delete Information':
                if options == 'Bed Information':
                    Bed_id = st.text_input('Bed Id', value = '1')
                    Bed_id = int(Bed_id)

                if options == 'Date of Admittance':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)

                if options == 'Emergency Contacts':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)

                if options == 'Medicine Inventory':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)
               
                if options == 'Medicine Prescriptions':
                    MedId = st.text_input('Medicine Id', value = '1')
                    MedId = int(MedId)

                if options == 'Patients':
                    patid = st.text_input('Patient Id', value = '1')
                    patid = int(patid)

                if st.button('Submit'):
                    if options == 'Bed Information':
                        cur.execute('''DELETE FROM Bed
    WHERE BED_id = %d'''%(Bed_id))    

                    if options == 'Date of Admittance':
                        cur.execute('''DELETE FROM Date_Admitted
    WHERE PatientID = %d'''%(patid))   
                        
                    if options == 'Emergency Contacts':
                        cur.execute('''DELETE FROM Emergency_Contact
    WHERE PatientID = %d'''%(patid)) 

                    if options == 'Medicine Inventory':
                        cur.execute('''DELETE FROM MEDICINE
    WHERE Medicine_ID = %d'''%(MedId)) 

                    if options == 'Medicine Prescriptions':
                        cur.execute('''DELETE FROM Medicine_Prescription
    WHERE Medicine_ID = %d'''%(MedId)) 

                    if options == 'Patients':
                        cur.execute('''DELETE FROM Patients
    WHERE PatientID = %d'''%(patid))
                
                conn.commit()
    
        st.table(source())
          
conn.commit()




