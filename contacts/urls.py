from django.contrib import admin
from django.urls import path
from contacts.views import contact_list_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contacts/', contact_list_create),
]
