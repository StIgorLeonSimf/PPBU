from django.shortcuts import render

from .models import Book

# books = [
#     {'id':1, 'title':'Собачье сердце', 'author':'M. Булгаков'},
#     {'id':2, 'title':'Мартышка и очки', 'author':'И.А. Крылов'},
# ]

def index(request):
    temlate = 'book/index.html'
    objs = Book.objects.all()
    context = {'page_obj': objs}
    return render(request, temlate, context)
