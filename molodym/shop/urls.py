from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<category_slug>', product_list, name='product_list_by_category'),
    path('<id>/<slug>/', product_detail, name='product_detail'),
    path('contact/',contact,name='contact')
]