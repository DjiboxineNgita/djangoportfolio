from django.shortcuts import render
from django.template import loader
from myapp.models import *
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')

def presentation(request):
    return render(request, 'presentation.html')

def realisation(request):
    return render(request, 'realisation.html')

def competence(request):
    return render(request, 'competence.html')

def contact(request):
    return render(request, 'contact.html')

def loisirs(request):
    return render(request, 'loisirs.html')

def observation(request):
    observation = Observation.objects.all()
    return render(request, 'observation.html', {'observations': observation})

def details_personne(request):
    if request.method == 'POST':
        #utilisation du forms
        ajout = PersonneFroms(request.POST)

        #validation
        if ajout.is_valid():
            #acceder aux données
            nom = ajout.cleaned_data.get('nom')
            age = ajout.cleaned_data.get('age')

            #enregistrement
            Personne.objects.create(nom=nom,age=age)
        #vider la form
        ajout = PersonneFroms()
    else:
        ajout = PersonneFroms()
    #recuperation
    personnes = Personne.objects.all()
    return render(request, 'appli.html',{'personnes':personnes,'form':ajout})

def logout(request):
    #return render(request,'registration/login.html')
    return redirect('registration:login')




