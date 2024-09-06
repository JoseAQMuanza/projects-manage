from django.urls import path, include
from costs import views

urlpatterns = [  
  path('costs/', include('costs.urls')), 
]
