from django.shortcuts import render , redirect
from .models import Book , ISBN
from .forms import BookForm , ISBNForm
from django.contrib.auth.decorators import login_required ,permission_required

# Create your views here.
@login_required()   
@permission_required(['books.view_book'], raise_exception=True)
def index(request):
    books = Book.objects.all()
    return render(request , 'Books/index.html' ,{
        "books":books
    })
@login_required()    
def show(request , id):
  book = Book.objects.get(pk=id)
  return render (request , "Books/details.html" , {
      "book":book
  }) 
@login_required()     
def destroy(request , id):
    book = Book.objects.get(pk=id)
    book.delete()  
    return redirect('index')   
@login_required()   
def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        # author=form.cleaned_data.get('Author')
        # isbn_create=ISBN(Author_name=author)
        isbn_create.save()
        book = Book.objects.create(
            title=form.cleaned_data.get('title'),
            Description=form.cleaned_data.get('Description'),
            price=form.cleaned_data.get('price'),
            Publishment_date=form.cleaned_data.get('Publishment_date'),
            Author=form.cleaned_data.get('Author'),
           
            tag=form.cleaned_data.get('tag'),
            
        )
        book.Category.set(form.cleaned_data.get('Category'))
        
        return redirect('index') 
       

    return render (request , "Books/create.html" , {
      "form":form
  }) 
@login_required()   
def edit(request , id):
    book =Book.objects.get(pk=id)
    form = BookForm(request.POST or None , instance=book)
    if form.is_valid():
        form.save()
        return redirect('index') 

    return render (request , "Books/create.html" , {
      "form":form
  }) 

       

# def createIsbn(request):
#     form = ISBNForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('create') 

#     return render (request , "Books/CreateISBN.html" , {
#       "form":form
#   }) 


