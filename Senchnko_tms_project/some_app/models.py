from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.position}'


class Task(models.Model):
    description = models.CharField(max_length=255)
    deadline = models.CharField(max_length=255)
    employee_id = models.ForeignKey('Employee', null=True, on_delete=models.CASCADE, related_name='name_id',)
    project_budget = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.description} | {self.deadline} | {self.project_budget} $'
