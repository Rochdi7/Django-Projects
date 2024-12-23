from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_emprunts, name='liste_emprunts'),
    path('ajouter/', views.ajouter_emprunt, name='ajouter_emprunt'),
    path('<int:id>/modifier/', views.modifier_emprunt, name='modifier_emprunt'),
    path('<int:id>/supprimer/', views.supprimer_emprunt, name='supprimer_emprunt'),
]
