from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Emprunt
from livres.models import Livre

def liste_emprunts(request):
    query = request.GET.get('q', '')
    if query:
        emprunts = Emprunt.objects.filter(emprunteur__icontains=query) | Emprunt.objects.filter(livre__titre__icontains=query)
    else:
        emprunts = Emprunt.objects.all()
    return render(request, 'emprunts/emprunts.html', {'emprunts': emprunts})


def ajouter_emprunt(request):
    livres = Livre.objects.filter(exemplaires__gt=0) 
    if request.method == 'POST':
        emprunteur = request.POST.get('emprunteur')
        livre_id = request.POST.get('livre')
        date_retour = request.POST.get('date_retour')

        livre = get_object_or_404(Livre, id=livre_id)
        emprunt = Emprunt(emprunteur=emprunteur, livre=livre, date_retour=date_retour)
        try:
            emprunt.save()
            livre.exemplaires -= 1
            livre.save()
            return redirect('liste_emprunts')
        except ValidationError as e:
            return render(request, 'emprunts/ajouter_emprunt.html', {'livres': livres, 'error_message': e.message})

    return render(request, 'emprunts/ajouter_emprunt.html', {'livres': livres})


def modifier_emprunt(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)
    livres = Livre.objects.all()
    if request.method == 'POST':
        emprunt.emprunteur = request.POST.get('emprunteur')
        livre_id = request.POST.get('livre')
        emprunt.livre = get_object_or_404(Livre, id=livre_id)
        emprunt.date_retour = request.POST.get('date_retour')
        emprunt.save()
        return redirect('liste_emprunts')
    return render(request, 'emprunts/modifier_emprunt.html', {'emprunt': emprunt, 'livres': livres})

def supprimer_emprunt(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)
    if request.method == 'POST':
        emprunt.livre.exemplaires += 1
        emprunt.livre.save()
        emprunt.delete()
        return redirect('liste_emprunts')
    return render(request, 'emprunts/supprimer_emprunt.html', {'emprunt': emprunt})
