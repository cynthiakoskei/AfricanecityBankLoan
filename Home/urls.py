from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name="index"),
    path('Test/', views.loan_create, name="test"),
]