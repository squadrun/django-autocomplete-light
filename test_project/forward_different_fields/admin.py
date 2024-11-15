from django.contrib import admin

from .forms import TForm
from .models import TModel


class TestInline(admin.TabularInline):
    form = TForm
    model = TModel
    fk_name = 'for_inline'


@admin.register(TModel)
class TestAdmin(admin.ModelAdmin):
    form = TForm

