from django.urls import path
from . import views

app_name = 'clothesapp'

urlpatterns = [
    path('',views.clothesapp_list, name="list" ),
    path('<slug:slug>',views.clothesapp_page, name="page" ),
]