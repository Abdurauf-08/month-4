from django.urls import path
from . import views

urlpatterns = [
    path('my_favourite_writer/', views.my_favourite_writer_view, name='favourite_writer'),
    path('facts_about_writer/',views.facts_about_writer_view, name='writer_facts'),
    path('facts_about_writer/', views.facts_about_writer_view, name='writer_opinion')
]