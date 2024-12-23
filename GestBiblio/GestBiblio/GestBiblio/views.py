
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def accueil_page(request):
    return render(request, 'accueil.html')

def Contact_page(request):
    return render(request, 'Contact.html')

def seconnecter_page(request):
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom_utilisateur')
        motdepasse = request.POST.get('motdepasse')
        user = authenticate(username = nom_utilisateur , password = motdepasse)

        if user is not None:
            login(request, user)
            return render(request ,"dashboard.html")
        else:
            print("error signing in")
    return render(request, 'seconnecter.html')

def inscription_page(request):
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        nom_utilisateur = request.POST.get('nom_utilisateur')
        motdepasse = request.POST.get('motdepasse')
        confirmer_motdepasse = request.POST.get('confirmer_motdepasse')

        if motdepasse == confirmer_motdepasse:
            user = User.objects.create_user(
                first_name = prenom,
                last_name = nom,
                username = nom_utilisateur,
                password = motdepasse
            )
            return render(request, 'seconnecter.html')
    return render(request, 'inscription.html')


