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

from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from some_app.views import home_page, del_task, create_task, add_task, create_employee, \
    add_employee, access_denied, send, create_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('home/', home_page, name='home'),
    url(r'^(?P<a_id>\d+)/del', del_task, name='del_view'),
    path('create_task/', create_task, name='create_task'),
    path('add_task', add_task, name='add_task'),
    path('create_employee/', create_employee, name='create_employee'),
    path('add_employee', add_employee, name='add_employee'),
    path('access_denied/', access_denied, name='access_denied'),
    path('send/', send, name='send'),
    path('create_message', create_message, name='create_message'),
]
