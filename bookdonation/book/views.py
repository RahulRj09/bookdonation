from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Book,Profile,Book_request
from .forms import UserForm,BookForm,AdduserForm
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings



def email(request):
        subject = 'Request for book'
        message = 'Hi'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rahuljoshi.rj726@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
        return redirect('home')


@login_required
def Home(request):
    posts = Book.objects.all()
    return render(request, 'home.html', {'posts': posts})
@login_required
@transaction.atomic


def Logout(request):
    logout(request)	
    return HttpResponseRedirect('/')


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('mybook')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_edit.html', {'form': form})


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


def Mybook(request):
    # my = Book.objects.filter(user__username =request.user)
    print("ab me yaha hun")
    my = Book.objects.filter(email = request.user.email)
    return render(request, 'mybook.html', {'my':my })


def book_remove(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('mybook')