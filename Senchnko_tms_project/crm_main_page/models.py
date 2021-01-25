from django.db import models
from django.db.models import Sum
from crm_main_page.mydbfields import EuDateField

# Create your models here.
from django.urls import reverse


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.position}'

    @staticmethod
    def get_absolute_url():
        return reverse('home')


class Task(models.Model):
    description = models.CharField(max_length=255)
    deadline = EuDateField()
    employee_id = models.ForeignKey('Employee', null=True, on_delete=models.CASCADE, related_name='name_id',)
    project_budget = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.description} | {self.deadline} | {self.project_budget} $'

    @staticmethod
    def count_tasks() -> object:
        number_of_tasks = Task.objects.count()
        return number_of_tasks

    @staticmethod
    def count_total_budget():
        total_budget_dict = Task.objects.aggregate(Sum('project_budget'))
        total_budget = total_budget_dict['project_budget__sum']
        return total_budget

    @staticmethod
    def get_absolute_url():
        return reverse('home')

    @staticmethod
    def order_more_to_less():
        sorted_list = Task.objects.order_by('-project_budget')
        return sorted_list

    @staticmethod
    def order_less_to_more():
        sorted_list = Task.objects.order_by('project_budget')
        return sorted_list
