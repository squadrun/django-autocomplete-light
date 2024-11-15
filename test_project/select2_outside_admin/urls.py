from django.urls import path

from .views import UpdateView


urlpatterns = [
    path(
        '',
        UpdateView.as_view(),
        name='select2_outside_admin',
    ),
]
