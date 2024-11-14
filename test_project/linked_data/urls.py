from dal import autocomplete

from django.urls import path

from .models import TModel


class LinkedDataView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = super(LinkedDataView, self).get_queryset()
        owner = self.forwarded.get('owner', None)

        if owner:
            qs = qs.filter(owner_id=owner)

        return qs


urlpatterns = [
    path(
        'linked_data/',
        LinkedDataView.as_view(model=TModel),
        name='linked_data'
    ),
]
