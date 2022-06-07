
from django.urls import path
from . import views


urlpatterns = [
    
    path('hello/', views.display),
    path('datetime/',views.displayDateTime),
    
]
 