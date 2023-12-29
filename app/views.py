from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def htmlforms(request):
    studentname=request.POST[sn]

    return HttpResponse(studentname)


    return render(request,'htmlforms.html')

def Create_school(request):
    sn=request.POST['sn']
    sl=request.POST['sl']
    sp=request.POST['sp']


    SO=school.objects.get_or_create(sname=sn,slocation=sl,sprincipal=sp)
    SO.save()


    return HttpResponse('school data is inserted')


    return render(request,'create_school.html')