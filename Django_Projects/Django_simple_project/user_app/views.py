from django.shortcuts import render
from django.http import HttpResponse
from user_app.models import Author_class, Book_class, Book_published

# Create your views here.
def user_page(request):
    book_list = Book_published.objects.order_by('book_date_published')
    date_dict = { 'book_records': book_list }
    return render(request,'user_app/user.html',context=date_dict)
