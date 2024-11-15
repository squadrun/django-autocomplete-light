import django
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin

import views


urlpatterns = [
    path('', views.IndexView.as_view()),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/', views.LoginView.as_view()),

    path('secure_data/', include('secure_data.urls')),
    path('linked_data/', include('linked_data.urls')),
    path('rename_forward/', include('rename_forward.urls')),
    path('forward_different_fields/',
        include('forward_different_fields.urls')),
    path('select2_nestedadmin/', include('select2_nestedadmin.urls')),

    path('select2_foreign_key/', include('select2_foreign_key.urls')),
    path('select2_list/', include('select2_list.urls')),
    path('select2_generic_foreign_key/',
        include('select2_generic_foreign_key.urls')),
    path('select2_many_to_many/',
        include('select2_many_to_many.urls')),
    path('select2_one_to_one/', include('select2_one_to_one.urls')),

    path('select2_outside_admin/', include('select2_outside_admin.urls')),
    path('select2_taggit/', include('select2_taggit.urls')),
    path('nested_admin/', include('nested_admin.urls')),
]

if django.VERSION < (2, 0, 0):
    # pending upstream support
    urlpatterns += [
        path('select2_tagging/', include('select2_tagging.urls')),
        path('select2_gm2m/', include('select2_gm2m.urls')),
        path('select2_generic_m2m/', include('select2_generic_m2m.urls')),
    ]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
