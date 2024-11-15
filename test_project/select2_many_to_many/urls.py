from dal import autocomplete

from django.urls import path
from django.views import generic

from .forms import TForm
from .models import TModel


urlpatterns = [
    path(
        'test-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            model=TModel,
            create_field='name',
        ),
        name='select2_many_to_many_autocomplete',
    ),
    path(
        'test/<int:pk>/',
        generic.UpdateView.as_view(
            model=TModel,
            form_class=TForm,
        )
    ),
]
