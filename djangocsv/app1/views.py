from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import InputForm
from app1.models import Student

import csv

def export_to_txt(request):
    response=HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=sports.txt'
    response.write('Cricket\n')
    response.write('Football')
    return response

def export_to_csv(request):
    students=Student.objects.all()
    response=HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=student_export1.txt'
    writer =csv.writer(response)
    student_fields = students.values_list('fname')
    for i in student_fields:
        writer.writerow(i)
    return response

def home(request):
    if request.method=="POST":
        form1=InputForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app1/index.html',{'form':form1, 'param1':'Success'})
    else:
        form1=InputForm()
    return render(request, 'app1/index.html',{'form':form1})