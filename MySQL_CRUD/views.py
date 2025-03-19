import logging
from inspect import Parameter
from django.shortcuts import redirect, render
from .forms import MyRegisterForm
from .models import RegisterForm
from django.contrib.auth.models import User

logger = logging.getLogger('django')

def home(request):
    data=RegisterForm.objects.all()
    if(data!=''):
        return render(request,"home.html",{'data':data})
    else:
        return render(request,"home.html")

def insert(request):
    if request.method=='POST':
        form= MyRegisterForm(request.POST)
        if form.is_valid(): 
            try:
                form.save()
                return redirect("home")
            except:
                pass 
    else:
        form= MyRegisterForm()
    return render(request,"register.html",{'form':form})

def update(request, id):
    data = RegisterForm.objects.get(id=id)
    if request.method == 'POST':
        Studyname = request.POST.get('Studyname')
        study_description = request.POST.get('study_description')
        study_phase = request.POST.get('study_phase')
        sponsor_name = request.POST.get('sponsor_name')

        data.Studyname = Studyname
        data.study_description = study_description
        data.study_phase = study_phase
        data.sponsor_name = sponsor_name

        data.save()
        return redirect("home")

    return render(request, "update.html", {'data': data})

def view(request, id):
    data = RegisterForm.objects.get(id=id)
    return render(request, "view.html",{'data':data})

def delete_selected(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_studies')

        if selected_ids:  
            RegisterForm.objects.filter(id__in=selected_ids).delete()

    return redirect("home")

def my_view(request):
    logger.info("Testing the logger")  # General log message
    
    try:
        user = User.objects.get(pk=1)  # Example: Fetch user with primary key 1
        logger.debug(f"User found: {user.username}")  # Debug log if found
    except User.DoesNotExist:
        logger.error("User with ID 1 does not exist")  # Log error if user is missing

    return render(request, "home.html")
