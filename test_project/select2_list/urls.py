from django.urls import path

from .views import Select2ListViewAutocomplete


urlpatterns = [
    path(
        'test-autocomplete/',
        Select2ListViewAutocomplete.as_view(),
        name='select2_list',
    ),
]
