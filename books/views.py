from django.shortcuts import render , redirect
from .models import Book , ISBN
from .forms import BookForm , ISBNForm
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request , 'Books/index.html' ,{
        "books":books
    })
def show(request , id):
  book = Book.objects.get(pk=id)
  return render (request , "Books/details.html" , {
      "book":book
  }) 
def destroy(request , id):
    book = Book.objects.get(pk=id)
    book.delete()  
    return redirect('index')   

def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index') 
       

    return render (request , "Books/create.html" , {
      "form":form
  }) 

def edit(request , id):
    book =Book.objects.get(pk=id)
    form = BookForm(request.POST or None , instance=book)
    if form.is_valid():
        form.save()
        return redirect('index') 

    return render (request , "Books/create.html" , {
      "form":form
  }) 

def createIsbn(request):
    form = ISBNForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index') 

    return render (request , "Books/CreateISBN.html" , {
      "form":form
  }) 

