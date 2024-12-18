# Setup environment path

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sample_Django_Project.settings')

import django
django.setup()

import random
from faker import Faker
from first_app.models import Web_Access_Record, Web_page_class, Topic_class

# Faker populate script
fakegen = Faker()
topics_list = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic_name():
    t = Topic_class.objects.get_or_create(topic_name=random.choice(topics_list))[0]
    t.save()
    return t

def populate_data(num=5):
    for entry in range(num):
        # Get the topic for the entry
        top = add_topic_name()

        # Create the fake data for that entry
        faker_url = fakegen.url()
        faker_date = fakegen.date()
        faker_name = fakegen.company()

        # Create the new webpage entry
        webpage = Web_page_class.objects.get_or_create( webpage_topic=top, webpage_url=faker_url, webpage_name=faker_name)[0]

        # Create the new Web access entry
        web_access = Web_Access_Record.objects.get_or_create(web_access_record_name=webpage, access_date=faker_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate_data(20)
    print("Populating completed!")
