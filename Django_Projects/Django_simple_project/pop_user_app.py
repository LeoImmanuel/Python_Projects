import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Sample_Django_Project.settings')

import django
django.setup()

import random
from faker import Faker
from user_app.models import Author_class, Book_class, Book_published

fake = Faker()
authors_list = ['Immanuel','Janani']

def add_author_name():
    a = Author_class.objects.get_or_create(author_name=random.choice(authors_list))[0]
    a.save()
    return a

def populate_data(num=2):
    for entry in range(num):
        auth = add_author_name()

        fakedate = fake.date()
        fakebook = fake.company()

        book_collection = Book_class.objects.get_or_create(book_author_name=auth, book_name=fakebook)[0]

        pub_date = Book_published.objects.get_or_create(book_name=book_collection, book_date_published=fakedate)[0]

if __name__ == '__main__':
    print("Populating...")
    populate_data(30)
    print("Completed..")