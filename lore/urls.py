from django.urls import path
from . import views

urlpatterns = [
    path('', views.lore_list, name='lore_list'),
    path('<int:pk>/', views.lore_detail, name='lore_detail'),
]
