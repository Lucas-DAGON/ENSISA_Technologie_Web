from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = 'welcome-view'),
    path('test_f', views.test_filter, name = 'test'),
    path('test_l', views.test_list, name = 'test list'),
    path('test_c_l', views.test_cond_list, name = 'test condition list'),
    path ('<int:question_id>/', views.detail, name = 'detail'),
    path ('<int:question_id>/results/', views.results, name ='results'),
    path ('<int:question_id>/vote/', views.vote, name ='vote'),
    ]