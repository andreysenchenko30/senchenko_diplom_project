
# Create your views here
from django.shortcuts import redirect
from crm_main_page.forms import TaskForm, EmployeeForm, ContactForm
from crm_main_page.models import Employee, Task
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        employees = Employee.objects.all()
        context = super(HomePageView, self).get_context_data(**kwargs)
        tasks = Task.objects.all()
        tasks_number = Task.count_tasks()
        total_budget = Task.count_total_budget()
        context['employees'] = employees
        context['tasks'] = tasks
        context['total_budget'] = total_budget
        context['tasks_number'] = tasks_number
        return context


class AccessDenied(TemplateView):
    template_name = 'access_denied.html'


class CreateTaskView(TemplateView):
    model = Employee
    template_name = 'create_task.html'

    def get_context_data(self, *args, **kwargs):
        employees = Employee.objects.all()
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        context['employees'] = employees
        return context


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'


class AddEmployeeView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'create_employee.html'


class NameCheck:
    @staticmethod
    def name_check(user):
        return user.email.endswith('@gmail.com')


class CreateEmployeeView(TemplateView):
    model = Employee
    template_name = 'create_employee.html'

    @method_decorator(user_passes_test(NameCheck.name_check, login_url='/access_denied'))
    def dispatch(self, *args, **kwargs):
        return super(CreateEmployeeView, self).dispatch(*args, **kwargs)


class DeleteTaskView(DeleteView):
    model = Task

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')

    @method_decorator(user_passes_test(NameCheck.name_check, login_url='/access_denied'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteTaskView, self).dispatch(*args, **kwargs)


class SendEmailView(FormView):
    form_class = ContactForm
    success_url = '/create_message'

    def form_valid(self, form):
        form.mail()
        return super().form_valid(form)


class CreateMessageView (TemplateView):
    model = ContactForm
    template_name = 'email_form.html'


# class SortLessToMore(TemplateView):
#     model = Task
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(SortLessToMore, self).get_context_data(**kwargs)
#         sorted_list_1 = Task.order_less_to_more()
#         context['sorted_list_1'] = sorted_list_1
#         return context
#
#
# class SortMoreToLess(TemplateView):
#     model = Task
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(SortMoreToLess, self).get_context_data(**kwargs)
#         sorted_list_2 = Task.order_more_to_less()
#         context['sorted_list_2'] = sorted_list_2
#         return context
