from django import forms
from django.db import models


class EuDateFormField(forms.DateField):
    def __init__(self, *args, **kwargs):
        kwargs.update({'input_formats': ("%d.%m.%Y",)})
        super(EuDateFormField, self).__init__(*args, **kwargs)


class EuDateField(models.DateField):
    def formfield(self, **kwargs):
        kwargs.update({'form_class': EuDateFormField})
        return super(EuDateField, self).formfield(**kwargs)
