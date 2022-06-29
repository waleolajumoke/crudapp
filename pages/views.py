from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentForm

# Create your views here.
def index(request):
    data = Students.objects.all()
    return render(request, 'index.html', {'data': data})

def about(request):
    return render(request, 'about.html')


def add(request):
    
    if request.method == 'POST' and request.FILES['Photo']:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        Photo = request.FILES['Photo']
        gender = request.POST['gender']
        is_admitted = request.POST['is_admitted']
        
        form = Students(first_name=first_name, last_name=last_name, phone=phone, Photo=Photo,gender=gender, email=email, is_admitted=is_admitted)
        # if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'add.html')


def delete(request, id):
    data = Students.objects.get(id=id)
    data.delete()
    return redirect('/')

def detail(request, id):
    data = Students.objects.get(id=id)
    return render(request, 'detail.html', {'data': data})


def edit(request, id):
    
    info = Students.objects.get(id=id)
    form = StudentForm(instance=info)
    
    if request.method == 'POST':
        form = StudentForm( request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('/')
    # data = Students.objects.get(id=id)
    return render(request, 'edit.html', {'form': form})