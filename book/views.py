from django.shortcuts import render, get_object_or_404
from book.models import Book
from django.http import HttpResponse
from . import models 
from django.core.paginator import Paginator
from django.db.models import F

def book_search_view(request):
        query = request.GET.get('q', '')
        if query:
                book = models.Book.objects.filter(title__icontains=query)
        else:
                return HttpResponse('Книга не найдено')
        return render(request, 'book_list,html', {'book': book})



def my_favourite_writer_view(request):
        return HttpResponse('<h1>Мой любимый писатель<h1><p>Мой любимый писатель - Александр Пушкин.<p>')


def facts_about_writer_view(request):
        return HttpResponse('<h1>Факты о писателе<h1><p>Он родился в 1799 году и написал более 400 произведений.<p>')


def my_opinion_about_writer_viev(request):
        return HttpResponse('<h1>Мое мнение<h1>Я считаю, что его слог является эталоном русского языка.<p>')

def book_list_view(request):
        if request.method == 'GET':
                book = models.Book.objects.all()
                paginator_book = Paginator(book, 2)
                page = request.GET.get('page')
                page_obj = paginator_book.get_page(page)
        return render(request, 'book_list.html', {'books': book})

        
def book_detail_view(request, id):
        if request.method == 'GET':
                book_id =get_object_or_404(Book, id=id)
                views_book = request.session.get('viewed_book', [])
                if id not in views_book:
                        book_id.views = F('views') + 1
                        book_id.save()
                        book_id.refresh_from_db()
                views_book.append(id)
                request.session['viewed_book'] = views_book
        return render(request, 'book_detail.html', {'book_id':book_id})


        