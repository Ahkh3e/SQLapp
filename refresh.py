
import streamlit as st
import cx_Oracle
import pandas as pd

dsnStr = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
conn = cx_Oracle.connect(, dsn=dsnStr)
print (conn.version)


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
    return(Medecinedf)

def medecinepre():
    cur.execute("""
    select * from MEDICINE_PRESCRIPTION
    """)
    pull = cur.fetchall()

    MedicinePredf = pd.DataFrame(pull, columns = ['MEDICINE_ID', 'PATIENTID', 'DOSAGE', 'CONSUMPTION_CYCLE'])
    print(MedicinePredf)

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

options = st.selectbox('Select Table to display',(
        'Employee', 'Logistics', 'Account', 'Bed Information',
        'Date of Admittance', 'List of Doctors','Emergency Contacts',
        'List of Law Enforcement','Medicine Inventory',
        'Medicine Prescriptions','List of Nurses','Operations Staff','Patients','Schedule'))

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
if options == 'Schedule':
    source = schedule

st.table(source())