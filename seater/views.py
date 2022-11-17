from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import student
from .forms import studentForm
 
def index(request):
    data = student.objects.all()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = studentForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'seater/index.html', context)
