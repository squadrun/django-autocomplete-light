from dal import autocomplete

from django.urls import path

from taggit.models import Tag


urlpatterns = [
    path(
        'test-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=Tag.objects.all(),
        ),
        name='select2_taggit',
    ),
]
