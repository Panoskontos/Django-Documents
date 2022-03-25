from .models import Book
from .forms import UploadBook
from django.shortcuts import render, redirect
import uuid
# Uploading a book


def uniqueName(name):
    name = name + '-' + str(uuid.uuid1())
    return name


def upload_book(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = UploadBook(request.POST, request.FILES)
        if form.is_valid():

            formFile = request.FILES['book']

            # It is good practice to have uuid with files
            formFile.name = uniqueName(formFile.name)

            formTitle = request.POST.get('title')
            formAuthor = request.POST.get('author')
            # Save in books
            book = Book(title=formTitle, book=formFile, author=formAuthor)
            book.save()

            return redirect('thankyou')
    else:
        form = UploadBook()
    context = {
        'form': form,
        'books': books,
    }
    return render(request, 'dishes/books.html', context)
