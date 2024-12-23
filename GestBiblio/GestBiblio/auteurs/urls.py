from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_auteurs, name='liste_auteurs'),
    
    path('ajouter/', views.ajouter_auteur, name='ajouter_auteur'),
    path('<int:id>/modifier/', views.modifier_auteur, name='modifier_auteur'),
    path('<int:id>/supprimer/', views.supprimer_auteur, name='supprimer_auteur'),
]
