from django.contrib import admin
from crm_main_page.models import Employee, Task


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    last_display = 'name'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    last_display = 'description'
