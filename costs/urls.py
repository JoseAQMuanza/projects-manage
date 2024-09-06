from costs import views
from django.urls import path

urlpatterns = [
  path('', views.home, name='home'),  
  path('contact/', views.contact, name='contact'),  
  path('projects/', views.projects, name='projects'),
  path('enterprise/', views.enterprise, name='enterprise'),
  path('projects/errorpage/', views.errorpage, name='errorpage'),  
  path('project/<int:id>/', views.edit, name='edit'),
  path('createproject', views.createproject, name='createproject'),  
  path('project/delete/<int:id>/', views.delete, name='delete'),
  path('project/<int:id>/edit', views.projectedit, name='projectedit'),
  path('project/<int:id>/service/<int:ids>/', views.deleteservice, name='deleteservice')
]  