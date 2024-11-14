from dal import autocomplete

from django.urls import path

from tagging.models import Tag


urlpatterns = [
    path(
        'test-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=Tag.objects.all(),
        ),
        name='select2_tagging',
    ),
]
