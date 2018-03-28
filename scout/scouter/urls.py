from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewall/', views.birds_eye_view, name='Birds-Eye_View'),
    path('survey/', views.get_survey, name='Return Survey'),
]