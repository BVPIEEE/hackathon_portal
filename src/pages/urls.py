from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.participant_dashboard, name="dashboard"),
    path("scoring/", views.scoring_dashboard, name="scoring"),
    path("submission1/", views.submission1, name="submission1"),
    path("submission2/", views.submission2, name="submission2"),
    path("submission3/", views.submission3, name="submission3"),
    path("submission4/", views.submission4, name="submission4"),
    path("final/", views.final, name="final"),
]

