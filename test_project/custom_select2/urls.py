from dal import autocomplete

from django.urls import path

from .models import TModel


urlpatterns = [
    path(
        'test-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(model=TModel),
        name='select2_fk',
    ),
]
