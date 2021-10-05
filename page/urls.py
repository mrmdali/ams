from django.urls import path
from .views import home

app_name = 'page'

urlpatterns = [
    path('', home, name='home'),

]
