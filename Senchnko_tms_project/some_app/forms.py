from django import forms
from some_app.models import Employee, Task


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'age', 'position')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'deadline', 'employee_id', 'project_budget')


class ContactForm(forms.Form):
    to_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(label='Message', required=True)