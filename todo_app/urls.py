from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addtask/', views.addtask, name="addtask"),
    path('delete/<int:pk>/', views.deletetask, name="delete"),
    path('update/<int:pk>', views.update, name="update"),
    path('updatetask/<int:pk>/', views.updatetask, name="updatetask"),
]