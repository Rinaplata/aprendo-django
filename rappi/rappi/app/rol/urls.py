from django.urls import path
from . import views

urlpatterns = [
    path('api/rol', views.RolView.as_view(),
    name='Rollist'),
    path('api/rol/create/', views.CreateRolView.as_view(),
    name='CreateRollist'),
    path('api/rol/<int:pk>', views.ListIdRolView.as_view(),
    name='ListIdRollist'),
    path('api/rol/update/<int:pk>/', views.UpdateRolView.as_view(),
    name='UpdateIdRollist'), 
    path('api/rol/delete/<int:pk>/', views.DeleteRolView.as_view(),
    name='DeleteIdRollist'), 

]