from django.core.mail import send_mail, BadHeaderError

# Create your views here
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from some_app.forms import TaskForm, EmployeeForm, ContactForm
from some_app.models import Employee, Task
from django.contrib.auth.decorators import user_passes_test


def home_page(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        tasks = Task.objects.all()
        tasks_number = count_tasks()
        total_budget = count_total_budget()
        return render(request, 'home.html', {'employees': employees, 'tasks': tasks, 'tasks_number': tasks_number,
                                             'total_budget': total_budget})


def access_denied(request):
    return render(request, 'access_denied.html',)


def create_task(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        return render(request, 'create_task.html', {'employees': employees})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            description = data.get('description')
            deadline = data.get('deadline')
            employee_id = data.get('employee_id')
            project_budget = data.get('project_budget')
            Task.objects.create(description=description, deadline=deadline, employee_id=employee_id,
                                project_budget=project_budget)
        return redirect('/home/')


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            age = data.get('age')
            position = data.get('position')
            Employee.objects.create(first_name=first_name, last_name=last_name, age=age, position=position)
        return redirect('/home/')


def count_tasks():
    number_of_tasks = Task.objects.count()
    return number_of_tasks


def count_total_budget():
    total_budget_dict = Task.objects.aggregate(Sum('project_budget'))
    total_budget = total_budget_dict['project_budget__sum']
    return total_budget


def name_check(user):
    return user.email.endswith('@gmail.com')


@user_passes_test(name_check, login_url=access_denied)
def create_employee(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        return render(request, 'create_employee.html', {'employees': employees})


@user_passes_test(name_check, login_url=access_denied)
def del_task(request, a_id):
    Task.objects.get(id=a_id).delete()
    return redirect('http://127.0.0.1:8000/home/')


def send(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            to_email = form.cleaned_data['to_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
            except BadHeaderError:
                return HttpResponse('Subject error.')
            return redirect('create_message')
        else:
            return HttpResponse('Wrong request.')
    return render(request, 'email_form.html', {'form': form})


def create_message(request):
    if request.method == 'GET':
        return render(request, 'email_form.html')
