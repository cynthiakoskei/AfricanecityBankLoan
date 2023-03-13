from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('register', views.register, name='register'),
    path('login',views.login_request,name='login'),
    path('logout',views.logout_request,name='logout')
=======
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login')
>>>>>>> 1cfee3a4e650a86b1fb7fed577f70c79d11a5d05
]