from django.shortcuts import render, redirect, get_object_or_404
from database.models import Books
from .forms import BookForm


# List all books
def book_list(request):
    books = Books.objects.all()
    return render(request, "book_list.html", {"books": books})


# Create a new book
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})


# Update an existing book
def book_update(request, book_id, title):
    book = get_object_or_404(Books, book_id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "book_form.html", {"form": form})


# Delete a book
def book_delete(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "book_confirm_delete.html", {"book": book})
