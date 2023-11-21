from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .form import SignUpForm,addRecordForm
from .models import AddRecord

def home(request):
    records = AddRecord.objects.all()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successfull..')
            name = user.get_username()
            return render(request,'records/home.html',{'name':name,'records':records})
        else:
            messages.success(request,'Unable to login, please check your credentials..')
    return render(request,'records/home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,'logout success..')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request, user)
            messages.success(request,'Registration success')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'records/register.html',{'form':form})
    return render(request,'records/register.html',{'form':form})

def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = addRecordForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request,'Record added successfully!')
                return redirect('home')
            
        else:
            form = addRecordForm()
            return render(request,'records/add_record.html',{'form':form})
    else:
        messages.success(request,'You must be logged in..')
        return redirect('home')
    

def view_record(request,pk):
    if request.user.is_authenticated:
        customer = AddRecord.objects.get(id=pk)
        return render(request,'records/view_record.html',{'customer':customer})
    else:
        messages.success(request,'You must be logged in.')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        customer = AddRecord.objects.get(id=pk)
        customer.delete()
        messages.success(request,'Record deleted successfully!')
        return redirect('home')
    else:
        messages.success(request,'You must be logged in.')
        return redirect('home') 

def update_record(request,pk):
    if request.user.is_authenticated:
        customer = AddRecord.objects.get(id=pk)
        form = addRecordForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated successfully!')
            return redirect('home')
        return render(request,'records/update_record.html',{'form':form})
    else:
        messages.success(request,'You must be logged in.')
        return redirect('home')
