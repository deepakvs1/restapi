from .import views
from django.urls import path 
from .views import Employeedetail

# mapping of URLs to corresponding views or class-based views 

urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register,name='register'),
    path('login', views.loginn,name='login'),
    path('usr',Employeedetail.as_view()),
]

