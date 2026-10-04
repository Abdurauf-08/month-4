from django.shortcuts import render, get_object_or_404
from book.models import Book
from django.http import HttpResponse

def my_favourite_writer_view(request):
        return HttpResponse('<h1>Мой любимый писатель<h1><p>Мой любимый писатель - Александр Пушкин.<p>')


def facts_about_writer_view(request):
        return HttpResponse('<h1>Факты о писателе<h1><p>Он родился в 1799 году и написал более 400 произведений.<p>')


def my_opinion_about_writer_viev(request):
        return HttpResponse('<h1>Мое мнение<h1>Я считаю, что его слог является эталоном русского языка.<p>')

def book_list_view(request):
        if request.method == 'GET':
                books = Book.objects.all()
                return render(request, 'book_list.html', {'books': books})

        
def book_detail_view(request, id):
        if request.method == 'GET':
                book =get_object_or_404(Book, id=id)
                return render(request, 'book_detail.html', {'book':book})


        