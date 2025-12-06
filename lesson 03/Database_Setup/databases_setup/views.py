from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()  # Use plural variable name for clarity
    context = {'students': students}  # Match variable name in template
    return render(request, 'student/index.html', context)
