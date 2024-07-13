from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chore-list/', views.chore_list, name='chore_list'),
    path('add-chore/', views.add_chore, name='add_chore'),
    path('complete-chore/<int:chore_id>/', views.complete_chore, name='complete_chore'),
    path('delete-chore/<int:chore_id>/', views.delete_chore, name='delete_chore'),
    path('register/', views.index, name='register'),
]