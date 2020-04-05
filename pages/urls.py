from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.participant_dashboard, name="dashboard"),
    path("scoring/", views.scoring_dashboard, name="scoring"),
    path("submission/", views.submission1, name="submission"),
    path("about/", views.about, name="about")
]

