from django.shortcuts import render
from reg_app.forms import NewUserForm

# Create your views here.
def home_page(request):
    return render(request,'home_page/home.html')



def users(request):
    form_ins = NewUserForm()

    if request.method == 'POST':
        form_ins = NewUserForm(request.POST)

        if form_ins.is_valid():
            form_ins.save(commit=True)
            return home_page(request)
        else:
            print("Error")

    return render(request,'reg_app/signup.html',{'form':form_ins})

def login_view(request):
    return render(request, 'reg_app/login.html')





