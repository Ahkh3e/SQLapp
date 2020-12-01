import streamlit as st
import cx_Oracle
import pandas as pd
from PIL import Image

dsnStr = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
conn = cx_Oracle.connect('', dsn=dsnStr)
print (conn.version)

loggedin= False


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

#def Query1():

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

#def Query3():

#def Query4():

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

#def Query8():

#SchoolDb	m534khan@//oracle.scs.ryerson.ca:1521/orcl

image = Image.open('hospital.jpg')

st.title("Emergency Management System")
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
        'Medicine Prescriptions','List of Nurses','Operations Staff','Patients'))

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
'''%(Bed_id)) 

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
        'Medicine Prescriptions','Patients','Query2','Query5','Query6','Query7'))

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
    if options == 'Query2':
        source = Query2
    if options == 'Query5':
        source = Query5
    if options == 'Query6':
        source = Query6
    if options == 'Query7':
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
        
            




