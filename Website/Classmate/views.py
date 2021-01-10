from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course, Contact
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q


def Courses(request):
    std = Course.objects.all()
    template = loader.get_template('Classmate/Course.html')
    context = {
        'std': std,
    }

    return HttpResponse(template.render(context, request))


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect('Classmate:home_page')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect("Classmate:home_page")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")

    form = AuthenticationForm()
    return render(request=request, template_name='Classmate/login.html', context={'form': form})


def contact(request):
    if request.method == "POST":
        name = (request.POST.get('name', ''))
        email = (request.POST.get('email', ''))
        phone = (request.POST.get('phone', ''))
        desc = (request.POST.get('desc', ''))
        print(name, email, phone, desc)
        contacts = Contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
    return render(request, 'Classmate/contact.html')



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("Classmate:home_page")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                return render(request=request, template_name="Classmate/register.html", context={'form': form})

    form = UserCreationForm
    return render(request=request, template_name="Classmate/register.html", context={'form': form})


def about(request):
    return render(request, 'Classmate/about.html')


def home(request):
    return render(request, 'Classmate/Course.html')


def blog(request):
    return render(request, 'Classmate/blog.html')

def Details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'Classmate/Details.html', {'course': course})


def yourchoice(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    try:
        selected_Course_type = course.details_set.get(Course_type=request.POST['choice'])
    except (KeyError, Course.DoesNotExist):
        return render(request, 'Classmate/Details.html', {'course': course, 'error_message': "Select a valid option"})
    else:
        selected_Course_type.your_choice = True
        selected_Course_type.save()
        return render(request, 'Classmate/description.html', {'course': course})


def description(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'Classmate/description.html', {'course': course})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(Course_name__icontains=query) | Q(Courses_id__icontains=query) | Q(description__icontains=query)
            results = Course.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'submitbutton': submitbutton
            }
            return render(request, 'Classmate/search.html', context)
        else:
            return render(request, 'Classmate/search.html')
    else:
        return render(request, 'Classmate/search.html')
