from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = BookForm()
        context = {
            'form': form
        }
    return render(request, 'upload_image.html', context)
