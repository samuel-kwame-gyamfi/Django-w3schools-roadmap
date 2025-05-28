from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.details, name='details'),  # Just the ID here
    path('hello/', views.greet),
]