"""Senchnko_tms_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin
from crm_main_page.views import HomePageView, DeleteTaskView, CreateTaskView, AddTaskView, CreateEmployeeView, \
    AddEmployeeView, AccessDenied, SendEmailView, CreateMessageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('home/', HomePageView.as_view(), name='home'),
    path('<pk>/remove', DeleteTaskView.as_view(), name='del_view'),
    path('create_task/', CreateTaskView.as_view(), name='create_task'),
    path('add_task', AddTaskView.as_view(), name='add_task'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('add_employee', AddEmployeeView.as_view(), name='add_employee'),
    path('access_denied/', AccessDenied.as_view(), name='access_denied'),
    path('send/', SendEmailView.as_view(), name='send'),
    path('create_message', CreateMessageView.as_view(), name='create_message'),
    # path('more_to_less', SortMoreToLess.as_view(), name='more_to_less'),
    # path('less_to_more', SortLessToMore.as_view(), name='less_to_more'),
]
