from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

import mysql.connector as db

conn = db.connect(host="localhost", user="root", passwd="5321Han5321!", database="assignment")
print("Success")
curr = conn.cursor()

def home(request):
    return render(request, 'home.html')

def list(request):
    curr.execute("SELECT * FROM Users")
    data = curr.fetchall()
    return render(request, 'view.html', {'users': data})

def delete(request, email):
    curr.execute("DELETE FROM Users WHERE email = '{}'".format(email))
    conn.commit()
    return redirect(list)

def edit(request, email):
    print(email)
    curr.execute("SELECT * FROM Users WHERE email = '{}'".format(email))
    data = curr.fetchone()
    curr.execute("SELECT cname FROM Country")
    data2 = curr.fetchall()
    return render(request, 'edit.html', {'users': data, 'cnames': data2})

def update(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        name = request.POST['txt2']
        surname = request.POST['txt3']
        salary = request.POST['num1']
        phone = request.POST['txt4']
        cname = request.POST['txt5']
        curr.execute("UPDATE Users SET name ='{}', surname='{}' , salary={}, phone='{}', cname='{}' WHERE email = '{}'".format(name, surname, salary, phone, cname, email))
        conn.commit()
        return redirect(list)
    else:
        return redirect(list)

def create(request):
    curr.execute("SELECT cname FROM Country")
    data = curr.fetchall()
    return render(request, 'create.html', {'code': data})

def add(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        name = request.POST['txt2']
        surname = request.POST['txt3']
        salary = request.POST['num1']
        phone = request.POST['txt4']
        cname = request.POST['txt5']
        curr.execute("INSERT INTO Users(email, name, surname, salary, phone, cname) VALUES ('{}', '{}', '{}', {}, '{}', '{}')".format(email, name, surname, salary, phone, cname))
        conn.commit()
        return redirect(list)
    else:
        return redirect(list)

#disease_type
def listDT(request):
    curr.execute("SELECT * FROM DiseaseType")
    data = curr.fetchall()
    return render(request, 'viewDT.html', {'disease_type': data})

def deleteDT(request, id):
    curr.execute("DELETE FROM DiseaseType WHERE id = {}".format(id))
    conn.commit()
    return redirect(listDT)

def editDT(request, id):
    curr.execute("SELECT * FROM DiseaseType WHERE id = '{}'".format(id))
    data = curr.fetchone()
    return render(request, 'editDT.html', {'disease_type': data})

def updateDT(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['txt1']
        description = request.POST['txt2']
        curr.execute("UPDATE DiseaseType SET description='{}' WHERE id = {}".format(description, id))
        conn.commit()
        return redirect(listDT)
    else:
        return redirect(listDT)

def createDT(request):
    return render(request, 'createDT.html')

def addDT(request):
    if request.method == 'POST':
        print(request.POST)
        description = request.POST['txt1']
        curr.execute("INSERT INTO DiseaseType(description) VALUES ('{}')".format(description))
        conn.commit()
        return redirect(listDT)
    else:
        return redirect(listDT)

#Country
def listCountry(request):
    curr.execute("SELECT * FROM Country")
    data = curr.fetchall()
    return render(request, 'viewCountry.html', {'country': data})

def deleteCountry(request, cname):
    curr.execute("DELETE FROM Country WHERE cname = '{}'".format(cname))
    conn.commit()
    return redirect(listCountry)

def editCountry(request, cname):
    curr.execute("SELECT * FROM Country WHERE cname = '{}'".format(cname))
    data = curr.fetchone()
    return render(request, 'editCountry.html', {'country': data})

def updateCountry(request):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['txt1']
        population = request.POST['num1']
        curr.execute("UPDATE Country SET population={} WHERE cname='{}'".format(population, cname))
        conn.commit()
        return redirect(listCountry)
    else:
        return redirect(listCountry)

def createCountry(request):
    return render(request, 'createCountry.html')

def addCountry(request):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['txt1']
        population = request.POST['num1']
        curr.execute("INSERT INTO Country(cname, population) VALUES ('{}', {})".format(cname, population))
        conn.commit()
        return redirect(listCountry)
    else:
        return redirect(listCountry)

#Disease
def listDisease(request):
    curr.execute("SELECT * FROM Disease")
    data = curr.fetchall()
    return render(request, 'viewDisease.html', {'disease': data})

def deleteDisease(request, disease_code):
    curr.execute("DELETE FROM Disease WHERE disease_code = '{}'".format(disease_code))
    conn.commit()
    return redirect(listDisease)

def editDisease(request, disease_code):
    curr.execute("SELECT * FROM Disease WHERE disease_code = '{}'".format(disease_code))
    data = curr.fetchone()
    curr.execute("SELECT id FROM DiseaseType")
    data2 = curr.fetchall()
    return render(request, 'editDisease.html', {'disease': data, 'data2': data2})

def updateDisease(request):
    if request.method == 'POST':
        print(request.POST)
        disease_code = request.POST['txt1']
        pathogen = request.POST['txt2']
        description = request.POST['txt3']
        curr.execute("UPDATE Disease SET pathogen='{}', description='{}' WHERE disease_code='{}'".format(pathogen, description, disease_code))
        conn.commit()
        return redirect(listDisease)
    else:
        return redirect(listDisease)

def createDisease(request):
    curr.execute("SELECT id FROM DiseaseType")
    data = curr.fetchall()
    return render(request, 'createDisease.html', {'code': data})

def addDisease(request):
    if request.method == 'POST':
        print(request.POST)
        disease_code = request.POST['txt1']
        pathogen = request.POST['txt2']
        description = request.POST['txt3']
        id = request.POST['num1']
        curr.execute("INSERT INTO Disease(disease_code, pathogen, description, id) VALUES ('{}', '{}', '{}', {})".format(disease_code, pathogen, description, id))
        conn.commit()
        return redirect(listDisease)
    else:
        return redirect(listDisease)

#Servant
def listServant(request):
    curr.execute("SELECT * FROM PublicServant")
    data = curr.fetchall()
    return render(request, 'viewServant.html', {'servant': data})

def deleteServant(request, email):
    curr.execute("DELETE FROM PublicServant WHERE email = '{}'".format(email))
    conn.commit()
    return redirect(listServant)

def editServant(request, email):
    curr.execute("SELECT * FROM PublicServant WHERE email = '{}'".format(email))
    data = curr.fetchone()
    return render(request, 'editServant.html', {'servant': data})

def updateServant(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        department = request.POST['txt2']
        curr.execute("UPDATE PublicServant SET department='{}' WHERE email='{}'".format(department, email))
        conn.commit()
        return redirect(listServant)
    else:
        return redirect(listServant)

def createServant(request):
    curr.execute("SELECT email FROM Users WHERE email NOT IN (SELECT email FROM Doctor) AND email NOT IN (SELECT email FROM PublicServant)")
    data = curr.fetchall()
    return render(request, 'createServant.html', {'code': data})

def addServant(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        department = request.POST['txt2']
        curr.execute("INSERT INTO PublicServant(email, department) VALUES ('{}', '{}')".format(email, department))
        conn.commit()
        return redirect(listServant)
    else:
        return redirect(listServant)

#Doctor
def listDoctor(request):
    curr.execute("SELECT * FROM Doctor")
    data = curr.fetchall()
    return render(request, 'viewDoctor.html', {'doctor': data})

def deleteDoctor(request, email):
    curr.execute("DELETE FROM Doctor WHERE email = '{}'".format(email))
    conn.commit()
    return redirect(listDoctor)

def editDoctor(request, email):
    curr.execute("SELECT * FROM Doctor WHERE email = '{}'".format(email))
    data = curr.fetchone()
    return render(request, 'editDoctor.html', {'doctor': data})

def updateDoctor(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        degree = request.POST['txt2']
        curr.execute("UPDATE Doctor SET degree='{}' WHERE email='{}'".format(degree, email))
        conn.commit()
        return redirect(listDoctor)
    else:
        return redirect(listDoctor)

def createDoctor(request):
    curr.execute("SELECT email FROM Users WHERE email NOT IN (SELECT email FROM PublicServant) AND email NOT IN (SELECT email FROM Doctor)")
    data = curr.fetchall()
    return render(request, 'createDoctor.html', {'code': data})

def addDoctor(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        degree = request.POST['txt2']
        curr.execute("INSERT INTO Doctor(email, degree) VALUES ('{}', '{}')".format(email, degree))
        conn.commit()
        return redirect(listDoctor)
    else:
        return redirect(listDoctor)

#Specialize
def listSpec(request):
    curr.execute("SELECT * FROM Specialize")
    data = curr.fetchall()
    return render(request, 'viewSpec.html', {'spec': data})

def deleteSpec(request, id, email):
    curr.execute("DELETE FROM Specialize WHERE id = '{}' AND email = '{}'".format(id, email))
    conn.commit()
    return redirect(listSpec)

def editSpec(request, id, email):
    curr.execute("SELECT * FROM Specialize WHERE id = '{}' AND email = '{}'".format(id, email))
    data = curr.fetchone()
    curr.execute("SELECT id FROM DiseaseType")
    data1 = curr.fetchall()
    curr.execute("SELECT email FROM Doctor")
    data2 = curr.fetchall()
    return render(request, 'editSpec.html', {'spec': data, 'data1': data1, 'data2': data2})

def updateSpec(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['num1']
        email = request.POST['txt1']
        curr.execute("UPDATE Specialize SET email='{}', id='{}'".format(email, id))
        conn.commit()
        return redirect(listSpec)
    else:
        return redirect(listSpec)

def createSpec(request):
    curr.execute("SELECT id FROM DiseaseType")
    data1 = curr.fetchall()
    curr.execute("SELECT email FROM Doctor")
    data2 = curr.fetchall()
    return render(request, 'createSpec.html', {'code1': data1, 'code2': data2})

def addSpec(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['num1']
        email = request.POST['txt1']
        curr.execute("INSERT INTO Specialize(id, email) VALUES ({}, '{}')".format(id, email))
        conn.commit()
        return redirect(listSpec)
    else:
        return redirect(listSpec)

#Record
def listRecord(request):
    curr.execute("SELECT * FROM Record")
    data = curr.fetchall()
    return render(request, 'viewRecord.html', {'record': data})

def deleteRecord(request, email, cname, disease_code):
    curr.execute("DELETE FROM Record WHERE email = '{}' AND cname = '{}' AND disease_code = '{}'".format(email, cname, disease_code))
    conn.commit()
    return redirect(listRecord)

def editRecord(request, email, cname, disease_code):
    curr.execute("SELECT * FROM Record WHERE email = '{}' AND cname = '{}' AND disease_code = '{}'".format(email, cname, disease_code))
    data = curr.fetchone()
    curr.execute("SELECT email FROM PublicServant")
    data1 = curr.fetchall()
    curr.execute("SELECT cname FROM Country")
    data2 = curr.fetchall()
    curr.execute("SELECT disease_code FROM Disease")
    data3 = curr.fetchall()
    return render(request, 'editRecord.html', {'record': data, 'data1': data1, 'data2': data2, 'data3': data3})

def updateRecord(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        cname = request.POST['txt2']
        disease_code = request.POST['txt3']
        total_deaths = request.POST['num1']
        total_patients = request.POST['num2']
        curr.execute("UPDATE Record SET email='{}', cname='{}', disease_code='{}', total_deaths={}, total_patients".format(email, cname, disease_code, total_deaths, total_patients))
        conn.commit()
        return redirect(listRecord)
    else:
        return redirect(listRecord)

def createRecord(request):
    curr.execute("SELECT disease_code FROM Disease")
    data1 = curr.fetchall()
    curr.execute("SELECT cname FROM Country")
    data2 = curr.fetchall()
    curr.execute("SELECT email FROM PublicServant")
    data3 = curr.fetchall()
    return render(request, 'createRecord.html', {'code1': data1, 'code2': data2, 'code3': data3})

def addRecord(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['txt1']
        cname = request.POST['txt2']
        disease_code = request.POST['txt3']
        total_deaths = request.POST['num1']
        total_patients = request.POST['num2']
        curr.execute("INSERT INTO Record(email, cname, disease_code, total_deaths, total_patients) VALUES ('{}', '{}', '{}', {}, {})".format(email, cname, disease_code, total_deaths, total_patients))
        conn.commit()
        return redirect(listRecord)
    else:
        return redirect(listRecord)

#Discover
def listDiscover(request):
    curr.execute("SELECT * FROM Discover")
    data = curr.fetchall()
    return render(request, 'viewDiscover.html', {'discover': data})

def deleteDiscover(request, cname, disease_code):
    curr.execute("DELETE FROM Discover WHERE cname = '{}' AND disease_code = '{}'".format(cname, disease_code))
    conn.commit()
    return redirect(listDiscover)

def editDiscover(request, cname, disease_code):
    curr.execute("SELECT * FROM Discover WHERE cname = '{}' AND disease_code = '{}'".format(cname, disease_code))
    data = curr.fetchone()
    curr.execute("SELECT disease_code FROM Disease")
    data1 = curr.fetchall()
    curr.execute("SELECT cname FROM Country")
    data2 = curr.fetchall()
    return render(request, 'editDiscover.html', {'discover': data, 'data1': data1, 'data2':data2})

def updateDiscover(request):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['txt1']
        first_enc_date = request.POST['date1']
        disease_code = request.POST['txt2']
        curr.execute("UPDATE Discover SET cname='{}', first_enc_date='{}', disease_code='{}'".format(cname, first_enc_date, disease_code))
        conn.commit()
        return redirect(listDiscover)
    else:
        return redirect(listDiscover)

def createDiscover(request):
    curr.execute("SELECT cname FROM Country")
    data1 = curr.fetchall()
    curr.execute("SELECT disease_code FROM Disease")
    data2 = curr.fetchall()
    return render(request, 'createDiscover.html', {'code1': data1, 'code2': data2})

def addDiscover(request):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['txt1']
        first_enc_date = request.POST['date1']
        disease_code = request.POST['txt2']
        curr.execute("INSERT INTO Discover(cname, first_enc_date, disease_code) VALUES ('{}', '{}', '{}')".format(cname, first_enc_date, disease_code))
        conn.commit()
        return redirect(listDiscover)
    else:
        return redirect(listDiscover)
