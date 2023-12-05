from django.shortcuts import render,redirect
from.forms import MyForm
from django.http import HttpResponse

def index(request):
    form=MyForm
    return render(request,'home.html',{'form':form})



def submit(request):
    if request.method == 'POST':  # Use 'POST' instead of 'post'
        form = MyForm(request.POST)
        if form.is_valid():
            name = request.POST['fullname']  # Use form.cleaned_data to get cleaned data
            email = request.POST['email']
            print('success')
            print(name)
            print(email)
            return HttpResponse("Thank you for submitting this form")
        else:
            print('fail')

    return redirect('index')  # Use quotes around 'index' and fix the indentation


# Create your views here.
