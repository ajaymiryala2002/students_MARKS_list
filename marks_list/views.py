from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q

from marks_list.models import student
from marks_list.forms import studentFORM

    
def search_student(request):
    data1 = request.GET.get('src')
    
    if data1:
        std1 = student.objects.filter(Hallticket_NO=data1)
        if not std1.exists():
            messages.error(request, 'Invalid hall ticket number.')
            # std1 = student.objects.all()  # Show all or empty list, depending on your goal
    else:
        std1 = student.objects.filter(Hallticket_NO=None)  # Or whatever fallback you want
        
    context = {
        'std1': std1
    }
    return render(request,'frontend/results.html',context)


def home(request):
    return render(request,'frontend/table.html')
    



    