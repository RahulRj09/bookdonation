from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Book,Profile,Userinfo
from .forms import UserForm,BookForm,AdduserForm
from django.core.files.storage import FileSystemStorage
@login_required
def Home(request):
    posts = Book.objects.all()
    # print (posts.image.url)
    
    return render(request, 'home.html', {'posts': posts})
@login_required
@transaction.atomic

def Logout(request):
    logout(request)	
    return HttpResponseRedirect('/')

def addbook(request):

    #Handling the post request data and a form is made
    if request.method =='POST':
        form=BookForm(request.POST, request.FILES)
        print (request.FILES)

        #validating and storing the form for further use
        if form.is_valid():
            form.save()
            return redirect('home')

    #new empty form instance for addbook is created
    else:
        form = BookForm()
    return render(request,'addnewbook.html',{'form':form})

def book_detail(request, pk):
    bookss = get_object_or_404(Book, pk=pk)
    #return render(request, 'book_detail.html', {'bookss': bookss})
    if request.method =='POST':
        form=AdduserForm(request.POST)
        print (request.POST) 

        #validating and storing the form for further use
        if form.is_valid():
            form.save()
            return redirect('home')

    #new empty form instance for addbook is created
    else:
        form = AdduserForm()
    return render(request,'book_detail.html',{'form':form, 'bookss': bookss})

# def Mybook(request):
#     if is_admin(request.user):

#         #filtring the MoneyRequest(atleast three) and facility objects
#         my = Book.objects.all()
#         return render(request, 'mybook.html', {'my':my })
def Mybook(request):
    # profile = Profile.objects.filter(user__username =request.user)
    print("ab me yaha hun")
    my = Book.objects.filter(user__user__username = request.user)
    print(my)
    return render(request, 'mybook.html', {'my':my })