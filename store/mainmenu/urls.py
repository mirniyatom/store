from django.urls import path
from . import views

urlpatterns = [
    path('<str:main_menu>', views.get_main_menu, name='main_menu'),
]