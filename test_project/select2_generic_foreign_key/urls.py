from dal import autocomplete

from django.urls import path
from django.contrib.auth.models import Group
from django.views import generic

from .forms import TForm
from .models import TModel


urlpatterns = [
    path(
        'test/<int:pk>/',
        generic.UpdateView.as_view(
            model=TModel,
            form_class=TForm,
        )
    ),
]
urlpatterns.extend(TForm.as_urls())
