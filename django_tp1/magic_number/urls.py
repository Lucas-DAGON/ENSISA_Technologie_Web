from django.urls import path
from . import views

urlpatterns = [
    path('', views.error_url, name='magic_error-view'),
    path('guess', views.guess_number, name='magic_no_number-view'),
    path('guess/<int:number>', views.guess_number, name='magic_name-view'),
]