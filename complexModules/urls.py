from django.urls import path

from . import views

urlpatterns = [
    path('updates/', views.update, name="update"),
    path('email/', views.email, name='email')
]
