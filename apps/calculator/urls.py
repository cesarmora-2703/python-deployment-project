from django.urls import path

from . import views

urlpatterns = [
    path('divide/', views.divide, name='divide'),
]
