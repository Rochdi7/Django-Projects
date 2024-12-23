from django.shortcuts import render, get_object_or_404, redirect
from .models import Auteur

def liste_auteurs(request):
    query = request.GET.get('q', '')
    if query:
        auteurs = Auteur.objects.filter(nom__icontains=query) | Auteur.objects.filter(nationalite__icontains=query)
    else:
        auteurs = Auteur.objects.all()
    return render(request, 'auteurs/auteurs.html', {'auteurs': auteurs})

def ajouter_auteur(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        nationalite = request.POST.get('nationalite')
        date_naissance = request.POST.get('date_naissance')
        Auteur.objects.create(nom=nom, prenom=prenom, nationalite=nationalite, date_naissance=date_naissance)
        return redirect('liste_auteurs')
    return render(request, 'auteurs/ajouter_auteur.html')

def modifier_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    if request.method == 'POST':
        auteur.nom = request.POST.get('nom')
        auteur.prenom = request.POST.get('prenom')
        auteur.nationalite = request.POST.get('nationalite')
        auteur.date_naissance = request.POST.get('date_naissance')
        auteur.save()
        return redirect('liste_auteurs')
    return render(request, 'auteurs/modifier_auteur.html', {'auteur': auteur})

def supprimer_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    if request.method == 'POST':
        auteur.delete()
        return redirect('liste_auteurs')
    return render(request, 'auteurs/supprimer_auteur.html', {'auteur': auteur})
