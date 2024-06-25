from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, homepage

app_name = CatalogConfig.name

urlpatterns = [
    path("", homepage, name="homepage"),
    path("contacts/", contacts, name="contacts"),
]
