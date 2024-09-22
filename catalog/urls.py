import contact

from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import products_list

app_name = CatalogConfig.name
urlpatterns = [
    path('', products_list),
    # path('', home, name='home'),
    # path('contacts/', contact, name='contacts')
]




# from django.urls import path
# from . import views
#
# urlpatterns = [
#
#     path('', views.index_view, name='index')
# ]