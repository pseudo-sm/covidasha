from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('create-alert',views.create_alert),
    path('create-enquire',views.enquire),
    path('how-it-works',views.how_it_works),
    path('covid-kitchen',views.covid_kitchen),
    path('food-order',views.food_order,name="food_order"),
]