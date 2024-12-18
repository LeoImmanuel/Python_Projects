from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic_class, Web_page_class, Web_Access_Record

# Create your views here.
def index(request):
    web_page_list = Web_Access_Record.objects.order_by('access_date')
    date_dict = {'access_records':web_page_list}
    return render(request,'first_app/index.html',context=date_dict)
