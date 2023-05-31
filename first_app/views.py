from django.shortcuts import render
from . forms import contactForm, Student_Data

# Create your views here.


def home(request):
    return render(request, 'first_app/home.html')


def about(request):
    if request.method == 'POST':
        print("Hello: ", request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        ratings = request.POST.get('ratings')

        return render(request, 'first_app/about.html', {"name": name, "email": email, "ratings": ratings})
    return render(request, 'first_app/about.html')


def form(request):
    return render(request, 'first_app/form.html')


def django_forms(request):
    if (request.method == 'POST'):
        form = Student_Data(request.POST, request.FILES)  # for file uploads
        if form.is_valid():  # check if form is valid
            # file = form.cleaned_data['file']
            # with open('./first_app/uploads/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'first_app/django_form.html', {"form": form})
    else:
        form = Student_Data()
    return render(request, 'first_app/django_form.html', {"form": form})
