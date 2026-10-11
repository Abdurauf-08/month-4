from django.urls import path
from . import views

urlpatterns = [
    path('create_anketa/', views.create_anketa_view),
    path('anketa_list/<int:id>/update/', views.update_anketa_view),
    path('anketa_list/<int:id>/delete/', views.delete_anketa_view),
    path('anketa_list/', views.read_anketa_view),
]