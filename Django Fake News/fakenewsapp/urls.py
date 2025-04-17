from django.urls import path
from . import views  # Adjust if necessary based on your project structure

urlpatterns = [
    # Other URL patterns
    path('', views.predictor, name='predictor'),  # Ensure the predictor view is mapped
    # path('getForminfo/', views.getForminfo, name='getForminfo'), 
     ]
