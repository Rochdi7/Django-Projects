from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre
from auteurs.models import Auteur
from django.db.models import Q

def liste_livres(request):
    query = request.GET.get('q', '')
    if query:
        livres = Livre.objects.filter(
            Q(titre__icontains=query) | Q(genre__icontains=query)
        )
    else:
        livres = Livre.objects.all()
    return render(request, 'livres/livres.html', {'livres': livres, 'query': query})

def ajouter_livre(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        auteur_id = request.POST['auteur'] 
        date_publication = request.POST['date_publication']
        genre = request.POST['genre']
        exemplaires = request.POST['exemplaires']

        auteur = get_object_or_404(Auteur, id=auteur_id)
        Livre.objects.create(
            titre=titre,
            auteur=auteur,
            date_publication=date_publication,
            genre=genre,
            exemplaires=exemplaires
        )
        return redirect('liste_livres')
    auteurs = Auteur.objects.all()
    return render(request, 'livres/ajouter_livre.html', {'auteurs': auteurs})

def modifier_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == 'POST':
        livre.titre = request.POST['titre']
        auteur_id = request.POST['auteur']
        livre.auteur = get_object_or_404(Auteur, id=auteur_id)
        livre.date_publication = request.POST['date_publication']
        livre.genre = request.POST['genre']
        livre.exemplaires = request.POST['exemplaires']
        livre.save()
        return redirect('liste_livres')
    auteurs = Auteur.objects.all()
    return render(request, 'livres/modifier_livre.html', {'livre': livre, 'auteurs': auteurs})

def supprimer_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livres')
    return render(request, 'livres/supprimer_livre.html', {'livre': livre})
