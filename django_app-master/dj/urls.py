from django.urls import path

from . import views

urlpatterns = [
    path('home_one/',views.test_one,name='test_one'),
    path('home_two/',views.test_two,name='test_two'),
    path('home_three/',views.test_three,name='test_three'),

]
