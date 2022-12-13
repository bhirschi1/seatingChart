from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import student
from .forms import studentForm

def createStudent(variables):
    newStud = student()
    newStud.fName = variables[0]
    newStud.lName = variables[1]
    newStud.restrictionNum = variables[2]

    newStud.save()
        

def index(request):
    data = student.objects.all()
    if request.method == 'POST':
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        restrictionNum = request.POST.get('restrictionNum')
        variables = [fName, lName, restrictionNum]

        createStudent(variables)


        # stud = student.objects.get(studentID = newStud.studentID)
        # selected = request.POST.get('neighbor')
        # if not selected == 'none':
        #     badid = restriction()
        #     badid.badID = request.POST.get('neighbor')
        #     badid.studentID = stud.studentID
    # destList = []

    # destList = request.POST.getlist('dests')
    # for i in destList :
    #     newCust.restriction.add(student.objects.get(id=i))

            # badid.save()
            
    context = {
        'data': data,
    }
    return render(request, 'seater/index.html', context)

def indexPageView(request):
    return render(request, 'seater/index.html')

def generatePageView(request) :
    data = student.objects.all()

    context = {
        'data' : data
    }
    return render(request, 'seater/new.html', context)

def viewListPageView(request) :
    data = student.objects.all()

    context = {
        'students' : data,
    }
    return render(request, 'seater/viewList.html', context)
    

def editStudPageView(request, stud_id) :
    stud = student.objects.get(studentID = stud_id)

    context = {
        'student' : stud
    }
    return render(request, 'seater/edit.html', context)

def editSingleStudentPageView(request, stud_id) :

    editStud = student.objects.get(studentID = stud_id)

    editStud.fName = request.POST.get('fName')
    editStud.lName = request.POST.get('lName')
    editStud.restrictionNum = request.POST.get('restrictionNum')
    
    editStud.save()

    # splitStudent = student.objects.get(studentID = stud_id)
    # rest = restriction.objects.filter(studentID = stud_id)


    # rest.badID = 

    data = student.objects.all()

    context = {
        'students' : data,
    }
    return render(request, 'seater/viewList.html', context)

def changeRestrictionsPageView(request, stud_id) :
    stud = student.objects.get(studentID = stud_id)

    context = {
        'student' : stud
    }
    return render(request, 'seater/restrictions.html', context)

def saveRestsPageView(request, stud_id) :

    stud = student.objects.get(studentID = stud_id)

    context = {
        'student' : stud
    }
    return render(request, 'seater/edit.html', context)

def deleteStudPageView(request, stud_id) :

    stud = student.objects.get(studentID = stud_id)
    stud.delete()
    data = student.objects.all()
    context = {
        'students' : data
    }
    return render(request, 'seater/viewList.html', context)


def studList(request):
    studs = student.objects.all()
    newList = []
    for stud in studs:
        
        if stud.restrictionNum > 0 :
            newList.append(stud)

    for stud in studs:
        if stud.restrictionNum == 0:
            newList.append(stud)

    context = {
        'studs' : newList
    }

    return render(request, 'seater/test.html', context)


def deleteAll(request):
    data = student.objects.all()
    for stud in data:
        stud.delete()

    return render(request, 'seater/viewList.html')





