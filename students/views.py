from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def register_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'students/register.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    
    return render(request, 'students/student_list.html', {'students': students})