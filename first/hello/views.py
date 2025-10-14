from django.shortcuts import render
from .models import *
from django.db.models import Avg, Min, Max, Count
# Create your views here.

# Задание 1.

# Создайте функцию, которая должна: 

#     получить все книги, которые в наличии и отсортируйте их по названию в алфавитном порядке,
#     передать список книг в шаблон.
     
# В шаблоне: 

#     отобразите заголовок «Книги в наличии»,
#     выведите таблицу с колонками: Название, Автор, Год издания, Цена (формат 2 знака после запятой используя фильтр),
#     если книг нет — покажите сообщение: «Нет доступных книг».
     
# Подсказка: {% empty %} - если нет данных
# def index(request):
#     books = Book.objects.filter(is_available=True).order_by('title') 

#     context = {
#         'books': books,
#     }

#     return render(request, 'index.html', context)


# Задание 2

# Создайте функцию, которая должна: 

#     получить автора по author_id,
#     получить все книги этого автора, отсортированные по году издания (от новых к старым),
#     передать в шаблон самого автора и его книги.
     
# В шаблоне: 

#     отобразите заголовок: «Книги автора: author»,
#     выведите список книг в виде нумерованного списка,
#     для каждой книги укажите: название, год издания и цену,
#     если у автора нет книг — напишите: «У этого автора пока нет книг в каталоге».
 
# Подсказка: Для получения всех книг автора можно обращаться по id Book.objects.filter(author=author_id).
# def index(request):
#     author_id = 1
#     author = Author.objects.get(id=author_id)
#     author_books = Book.objects.filter(author=author_id).order_by('-publication_year')

#     context = {
#         'author': author,
#         'author_books': author_books,
#     }

#     return render(request, 'index.html', context)


# Задание 3

# Создайте функцию, которая должна с помощью агрегатных функций и аннотаций получить: 

#     Общее количество книг в каталоге.
#     Среднюю цену всех книг (округлена до 2 знаков).
#     Самый ранний и самый поздний год издания.
#     Список авторов, у которых более одной книги, с указанием количества их книг.
     
# В шаблоне : 

#     отобразите раздел «Общая статистика»:
#         «Всего книг: X»
#         «Средняя цена: Y»
#         «Годы издания: от A до B»
         
#     ниже — раздел «Авторы с несколькими книгами»:
#         если таких авторов нет — напишите «Таких авторов нет»,
#         иначе выведите таблицу: Имя автора | Количество книг.

# Подсказка: используйте from django.db.models import Count, Avg, Min, Max.
# Для пункта 4 методы сравнения: value__cond, где value - переменная, cond - оператор
# Самые популярные операторы:
# gt - больше чем
# gte- больше чем и равно
# lt - меньше чем
# lte - меньше чем и равно
# def index(request):
#     books_amount = Book.objects.aggregate(total_books = Count('id'))
#     price_avg = Book.objects.aggregate(avg = Avg('price'))
#     max_year = Book.objects.aggregate(max = Max('publication_year'))
#     min_year = Book.objects.aggregate(min = Min('publication_year'))
#     author_amount = Author.objects.annotate(books_count = Count('book')).filter(books_count__gt=1)

#     context = {
#         'books_amount': books_amount['total_books'],
#         'price_avg': price_avg['avg'],
#         'max_year': max_year['max'],
#         'min_year': min_year['min'],
#         'author_amount': author_amount,
#     }

#     return render(request, 'index.html', context)


# Задание 4

# Создайте функцию, которая должна: 

#     выбрать книги, которые одновременно:
#         дороже 1000 рублей,
#         опубликованы до 1980 года,     
#     отсортировать их по убыванию цены,
     
# В шаблоне: 

#     заголовок: «Дорогие старые книги»,
#     таблица с колонками: Название, Автор, Год, Цена
#     если таких книг нет — сообщение: «Не найдено дорогих старых книг».
def index(request):

    books_list = Book.objects.filter(price__gt=1000).filter(publication_year__lt=1980).order_by('-price')

    context = {
        'books_list': books_list,
    }

    return render(request, 'index.html', context)