from django import forms
from django.core.mail import send_mail
from Senchnko_tms_project import settings
from crm_main_page.models import Employee, Task


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

    def mail(self):
        subject = self.cleaned_data['subject']
        to_email = self.cleaned_data['to_email']
        message = self.cleaned_data['message']

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
        pass
