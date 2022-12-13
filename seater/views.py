from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import student
from .forms import studentForm

def createStudent(variables):
    newStud = student()
    newStud.fName = variables[0]
    newStud.lName = variables[1]

    if variables[2] == "T" :
        newStud.front = True
    else :
        newStud.front = False

    newStud.save()
        

def index(request):
    data = student.objects.all()
    if request.method == 'POST':
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        frontVar = request.POST.get('front')
        variables = [fName, lName, frontVar]

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

    rest = restriction.objects.filter(studentID = stud_id)
    if rest :
        currRests = restriction.objects.get(studentID = stud_id)
    else :
        currRests = None

    context = {
        'student' : stud,
        'rest' : currRests,
    }
    return render(request, 'seater/edit.html', context)

def editSingleStudentPageView(request, stud_id) :

    editStud = student.objects.get(studentID = stud_id)

    editStud.fName = request.POST.get('fName')
    editStud.lName = request.POST.get('lName')
    frontVal = request.POST.get('front')

    if frontVal == "T" :
        editStud.front = True
    else :
        editStud.front = False
    
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

    rest = restriction.objects.filter(studentID = stud_id)
    allBads = student.objects.all()

    context = {
        'student' : stud,
        'rest' : rest,
        'allRests' : allBads
    }
    return render(request, 'seater/restrictions.html', context)

def saveRestsPageView(request, stud_id) :


    rest = restriction.objects.filter(studentID = stud_id)
    if rest :
        changeRest = restriction.objects.get(studentID = request.POST.get('bads'))
        tryRest = student.objects.get(studentID = stud_id)
        tryBad = student.objects.get(studentID = request.POST.get('bads'))
        changeRest.badID = tryBad
        changeRest.studentID = tryRest

        changeRest.save()
    else :
        currRest = restriction()
        tryRest = student.objects.get(studentID = stud_id)
        tryBad = student.objects.get(studentID = request.POST.get('bads'))
        currRest.badID = tryBad
        currRest.studentID = tryRest
        
        currRest.save()

    stud = student.objects.get(studentID = stud_id)
    newRest = student.objects.get(studentID = request.POST.get('bads'))

    context = {
        'student' : stud,
        'rest' : newRest,
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
