from django.urls import path
from . import views

urlpatterns = [
    path('', views.affichage, name='affichage'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion')
]