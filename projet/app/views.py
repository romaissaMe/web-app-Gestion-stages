from asyncio.windows_events import NULL
from datetime import datetime, timedelta
from itertools import count
from operator import countOf
from time import strftime, timezone
from django.core import serializers
from django.forms.widgets import HiddenInput
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from app.form import stagiaireForm , stageForm
from .models import convention, encadreur, entreprise, ficheEvaluation, ficheSuivi, promoteur, soutenance, stage,stagiaire,rapport
from . import models
from . import form
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from collections import Counter, OrderedDict

# Create your views here.


#ajouter stage 
def addStage(request):
    if (request.method=="GET"):
        form=stageForm()
        return render(request,'stage.html',{"form":form})
    elif (request.method=="POST"):
        form = stageForm(data=request.POST)
        type=request.POST.get('type')
        listeStagiaires=request.POST.getlist('stagiaires')
        if type=="PFE":
          if len(listeStagiaires)>=1 and len(listeStagiaires)<=2:
             if form.is_valid():
                form.save()
                form=stageForm()
                return redirect('afficherStage')
             else: 
                return render(request,'stage.html',{"form":form})
          else:
             message="veuillez selectionner entre 1 et 2 stagiaires!"
             return render(request,'stage.html',{"form":form,"message":message})
        elif type=="TECH":
          if len(listeStagiaires)>=1 and len(listeStagiaires)<=4:
             if form.is_valid():
                form.save()
                form=stageForm()
                return redirect('afficherStage')
             else: 
                return render(request,'stage.html',{"form":form})
          else:
             message="veuillez selectionner entre 1 et 4 stagiaires!"
             return render(request,'stage.html',{"form":form,"message":message})         
        elif type=="OUVRIER":
          if len(listeStagiaires)>=1 and len(listeStagiaires)<=2:
             if form.is_valid():
                form.save()
                form=stageForm()
                return redirect('afficherStage')
             else: 
                return render(request,'stage.html',{"form":form})
          else:
             message="veuillez selectionner entre 1 et 2 stagiaires!"
             return render(request,'stage.html',{"form":form,"message":message})
        
    


#ajouter un stagiaire
def addstagiaire(request):
   forme=stagiaireForm()  
   if (request.method=='POST'):
       forme=stagiaireForm(data=request.POST)
       if forme.is_valid():
           forme.save()
           forme=stagiaireForm()
           return redirect('afficherStagiaire')
       else:
            forme=stagiaireForm()
            return render(request,'stagiaires.html',{"form":forme})

   else:
        return render(request,'stagiaires.html',{"form":forme})
      
        
#ajouter entreprise 
def addEntreprise(request):
    if request.method=='POST':
        forme = form.entrepriseForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherEntreprise')
        else:
            forme=form.entrepriseForm()
            return render(request,'entreprise.html',{'form':forme})
    else:
     forme=form.entrepriseForm()
     return render(request,'entreprise.html',{'form':forme})

 #ajouter encadreur 
def addEncadreur(request):
    if request.method=='POST':
        forme = form.encadreurForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherEncadreur')
        else:
            forme=form.encadreurForm()
            return render(request,'encadreur.html',{'form':forme})
    else:
     forme=form.encadreurForm()
     return render(request,'encadreur.html',{'form':forme})        
    
 #ajouter promoteur
def addPromoteur(request):
    if request.method=='POST':
        forme = form.promoteurForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherPromoteur')
        else:
            forme=form.promoteurForm()
            return render(request,'promoteur.html',{'form':forme})
    else:
     forme=form.promoteurForm()
     return render(request,'promoteur.html',{'form':forme})

#ajouter convention
def addConvention(request):
    if request.method=='POST':
        forme = form.conventionForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherConvention')
        else:
            forme=form.conventionForm()
            return render(request,'convention.html',{'form':forme})
    else:
     forme=form.conventionForm()
     return render(request,'convention.html',{'form':forme})

#ajouter soutenance
def addSoutenance(request):
    if request.method=='POST':
        forme = form.soutenanceForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherSoutenance')
        else:
            forme=form.soutenanceForm()
            return render(request,'soutenance.html',{'form':forme})
    else:
     forme=form.soutenanceForm()
     return render(request,'soutenance.html',{'form':forme})

#ajouter fiheSuivi
def addFicheSuivi(request):
    if request.method=='POST':
        forme = form.ficheSuivForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherFicheSuivi')
        else:
            forme=form.ficheSuivForm()
            return render(request,'fichesuiv.html',{'form':forme})
    else:
     forme=form.ficheSuivForm()
     return render(request,'fichesuiv.html',{'form':forme})

#ajouter fiheEval
def addFicheEval(request):
    if request.method=='POST':
        forme = form.ficheEvForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherFicheEval')
        else:
            forme=form.ficheEvForm()
            return render(request,'ficheEval.html',{'form':forme})
    else:
     forme=form.ficheEvForm()
     return render(request,'ficheEval.html',{'form':forme})

#ajouter rapport
def addRapport(request):
    if request.method=='POST':
        forme = form.rapportForm(data=request.POST)
        if forme.is_valid:
            forme.save()
            return redirect('afficherRapport')
        else:
            forme=form.rapportForm()
            return render(request,'rapport.html',{'form':forme})
    else:
     forme=form.rapportForm()
     return render(request,'rapport.html',{'form':forme})

# afficher ficheEvaluation
def afficherFicheEval(request):
    if request.method=='GET':
       list=ficheEvaluation.objects.all()
       return render(request,'ficheEvalliste.html',{'list':list})
   

 # afficher rapport
def afficherRapport(request):
    if request.method=='GET':
       list=rapport.objects.all()

       return render(request,'rapportsliste.html',{'list':list})


# afficher Promoteur
def afficherPromoteur(request):
    if request.method=='GET':
       list=promoteur.objects.all()

       return render(request,'promoteurliste.html',{'liste':list})

# afficher Encadreur
def afficherEncadreur(request):
    if request.method=='GET':
       list=encadreur.objects.all()
       return render(request,'encadreurliste.html',{'list':list})


# afficher Soutenance
def afficherSoutenance(request):
    if request.method=='GET':
       list=soutenance.objects.all()

       return render(request,'soutenanceliste.html',{'list':list})

# afficher convention
def afficherConvention(request):
    if request.method=='GET':
       list=convention.objects.all()

       return render(request,'conventionliste.html',{'list':list})


# afficher ficheSuivi
def afficherFicheSuivi(request):
    if request.method=='GET':
       list=ficheSuivi.objects.all()

       return render(request,'fichesuivliste.html',{'list':list})
      
# afficher les stagiaires
def afficherStagiaire(request):
    if request.method=='GET':
       list=stagiaire.objects.all()

       return render(request,'stagiairesliste.html',{'list':list})
      
#afficher les stages
def afficherStages(request):
    if request.method=='GET':
       stages=stage.objects.all()
       return render(request,'stageslist.html',{'stage':stages})
    
#afficher le entreprises
def afficherEntreprise(request):
    if request.method=='GET':
       list=entreprise.objects.all()
       return render(request,'entreprisesliste.html',{'list':list})
       
#chercher un stage
def getStage(request):
    if request.method=='POST':
       searched=request.POST['searched']
       stages=stage.objects.filter(titre__contains=searched)
       if stages:
          return render(request,'stagesliste.html',{'searched':searched,'stage':stages})
       else:
           notfound='aucun resultat ne match votre recherche'
           return render(request,'stagesliste.html',{'notfound':notfound})

    else:
        return render(request,'stagesliste.html')

#chercher un stagiaire
def getStagiaire(request):
     if request.method=='POST':
       searched=request.POST['searched']
       list=stagiaire.objects.filter(nom__contains=searched)
       if list:
          return render(request,'stagiairesliste.html',{'searched':searched,'list':list})
       else:
           notfound='aucun resultat ne match votre recherche'
           return render(request,'stagiairesliste.html',{'notfound':notfound})

     else:
        return render(request,'stagiairesliste.html')


#+++++++++++++++++++++++++++++les fonctions supprimer et modifier
#supprimer un stage
def deleteStage(request,id):
    if request.method=='POST':
        stages=stage.objects.filter(code=id)
        stages.delete()
        return redirect('afficherStage')



#modifier un stage
def updateStage(request, id):
    
    stages = stage.objects.get(code=id)

    form = stageForm(instance=stages)
    if request.method=='POST':
     form = stageForm(request.POST,request.FILES,instance=stages)
     
     if form.is_valid():
            form.save()
            form=stageForm()  
            submited=request.POST['submited']
            if submited:
                return redirect('afficherStage')
            
   
    return render(request,'stage.html',{"form":form})


#supprimer un stagiaire       
def deleteStagiaire(request,id):
    if request.method=='POST':
        Stagiaire=stagiaire.objects.filter(matricule=id)
        Stagiaire.delete()
        return redirect('afficherStagiaire')


#modifier un stagiaire
def updateStagiaire(request,id):
    
    stag = stagiaire.objects.get(matricule=id)

    form = stagiaireForm(instance=stag)
    if request.method=='POST':
     form = stagiaireForm(request.POST,request.FILES,instance=stag)
     
     if form.is_valid():
            form.save()
            form=stagiaireForm()  
            submited=request.POST['submited']
            if submited:
                return redirect('afficherStagiaire')
            
   
    return render(request,'stagiaires.html',{"form":form})

#supprimer soutenance       
def deleteSoutenance(request,id):
    if request.method=='POST':
        S=soutenance.objects.filter(id_soutenance=id)
        S.delete()
        return redirect('afficherSoutenance')


#modifier soutenance
def updateSoutenance(request,id):
    
    S = soutenance.objects.get(id_soutenance=id)

    forme = form.soutenanceForm(instance=S)
    if request.method=='POST':
     forme = form.soutenanceForm(request.POST,request.FILES,instance=S)
     
     if forme.is_valid():
            forme.save()
            forme=form.soutenanceForm() 
            submited=request.POST['submited']
            if submited:
                return redirect('afficherSoutenance')
            
   
    return render(request,'soutenance.html',{"form":forme})
#supprimer un rapport      
def deleteRapport(request,id):
    if request.method=='POST':
        Rapport=rapport.objects.filter(id=id)
        Rapport.delete()
        return redirect('afficherRapport')


#modifier un rapport
def updateRapport(request,id):
    
    Rapport = rapport.objects.get(id=id)

    forme = form.rapportForm(instance=Rapport)
    if request.method=='POST':
     forme = form.rapportForm(request.POST,request.FILES,instance=Rapport)
     
     if forme.is_valid():
            forme.save()
            forme=form.rapportForm() 
            submited=request.POST['submited']
            if submited:
                return redirect('afficherRapport')
            
   
    return render(request,'rapport.html',{"form":forme})

#supprimer un promoteur     
def deletePromoteur(request,id):
    if request.method=='POST':
        Promoteur=promoteur.objects.filter(id_promoteur=id)
        Promoteur.delete()
        return redirect('afficherPromoteur')


#modifier un promoteur
def updatePromoteur(request,id):
    
    Promoteur = promoteur.objects.get(id_promoteur=id)

    forme = form.promoteurForm(instance=Promoteur)
    if request.method=='POST':
     forme = form.promoteurForm(request.POST,request.FILES,instance=Promoteur)
     
     if forme.is_valid():
            forme.save()
            forme=form.promoteurForm() 
            submited=request.POST['submited']
            if submited:
                return redirect('afficherPromoteur')
            
   
    return render(request,'promoteur.html',{"form":forme})
#supprimer un encadreur     
def deleteEncadreur(request,id):
    if request.method=='POST':
        Encadreur=encadreur.objects.filter(id_encadreur=id)
        Encadreur.delete()
        return redirect('afficherEncadreur')


#modifier un promoteur
def updateEncadreur(request,id):
    
    Encadreur = encadreur.objects.get(id_encadreur=id)

    forme = form.encadreurForm(instance=Encadreur)
    if request.method=='POST':
     forme = form.encadreurForm(request.POST,request.FILES,instance=Encadreur)
     
     if forme.is_valid():
            forme.save()
            forme=form.encadreurForm()
            submited=request.POST['submited']
            if submited:
                return redirect('afficherEncadreur')
            
   
    return render(request,'encadreur.html',{"form":forme})

#supprimer entreprise
def deleteEntreprise(request,id):
    if request.method=='POST':
        x=entreprise.objects.filter(nom_entreprise=id)
        x.delete()
        return redirect('afficherEntreprise')


#modifier Entreprise
def updateEntreprise(request,id):
    
    x = entreprise.objects.get(nom=id)

    forme = form.entrepriseForm(instance=x)
    if request.method=='POST':
     forme = form.entrepriseForm(request.POST,request.FILES,instance=x)
     
     if forme.is_valid():
            forme.save()
            forme=form.entrepriseForm()
            submited=request.POST['submited']
            if submited:
                return redirect('afficherEntreprise')
            
   
    return render(request,'entreprise.html',{"form":forme})


#supprimer convention
def deleteConvention(request,id):
    if request.method=='POST':
        x=convention.objects.filter(id_convention=id)
        x.delete()
        return redirect('afficherConvention')


#modifier convention
def updateConvention(request,id):
    
    x = convention.objects.get(id_convention=id)

    forme = form.conventionForm(instance=x)
    if request.method=='POST':
     forme = form.conventionForm(request.POST,request.FILES,instance=x)
     
     if forme.is_valid():
            forme.save()
            forme=form.conventionForm()
            submited=request.POST['submited']
            if submited:
                return redirect('afficherConvention')
            
   
    return render(request,'convention.html',{"form":forme})


#supprimer ficheEvaluation
def deleteficheEval(request,id):
    if request.method=='POST':
        x=ficheEvaluation.objects.filter(id_ficheEvaluation=id)
        x.delete()
        return redirect('afficherFicheEval')


#modifier ficheEvaluation
def updateficheEval(request,id):
    
    x = ficheEvaluation.objects.get(id_ficheEvaluation=id)

    forme =form.ficheEvForm(instance=x)
    if request.method=='POST':
     forme = form.ficheEvForm(request.POST,request.FILES,instance=x)
     
     if forme.is_valid():
            forme.save()
            forme=form.ficheEvForm()
            submited=request.POST['submited']
            if submited:
                return redirect('afficherFicheEval')
            
   
    return render(request,'ficheEval.html',{"form":forme})


#supprimer ficheSuivi
def deleteficheSuivi(request,id):
    if request.method=='POST':
        x=ficheSuivi.objects.filter(id_ficheSuivi=id)
        x.delete()
        return redirect('afficherFicheSuivi')


#modifier convention
def updateficheSuivi(request,id):
    
    x = ficheSuivi.objects.get(id_ficheSuivi=id)

    forme = form.ficheSuivForm(instance=x)
    if request.method=='POST':
     forme = form.ficheSuivForm(request.POST,request.FILES,instance=x)
     
     if forme.is_valid():
            forme.save()
            forme=form.ficheSuivForm()
            submited=request.POST['submited']
            if submited:
                return redirect('afficherFicheSuivi')
            
   
    return render(request,'ficheSuiv.html',{"form":forme})

# Create your views here.
# Create your views here.
def index(request):
 if request.method=='GET': #ce code pour afficher les statistique de l'annee universitaire courante automatiquemene
  #definir les tableaux a utiliser pour renvoyer les resultats dand le dictionnaire de donnees
  labels=[]   
  data=[]
  data2=[]
  data3=[]
  labels3=[]
  years=stage.objects.order_by().values_list('annee',flat=True).distinct()   #extraire les stages
  for y in years:
      labels3.append(y)  #extraires les annees universitaires de la bdd
  
  #initialiser year par l'annee universitaire courrente
  now= datetime.now()
  date= now - timedelta(days=365) 
  year2=date.strftime('%Y') #l'annee courante
  year1=now.strftime('%Y') #l'annee suivante
  year= year2+'/'+year1 #l'annee universitaire courante

  y=entreprise.objects.all() # extraire les entreprises 
  for an in labels3:         # compter le nombre d'organisme ayant recu des stagiares de stage type PFE pour chaque annee universitraire
    a=stage.objects.filter(type='PFE',annee=an).annotate(Count('entreprise')).count()
    data3.append(a)  #renvoyer les resultats dans un tableau data3



  for x in y:
    labels.append(x.nom) #enregistrer les noms des entreprises dans labels pour les afficher dans le graphe
    z=stage.objects.filter(entreprise=x.id_entreprise,type='PFE',annee=year).count() # le nombre des entreprise ayant recu des stagiaires de PFE de l'annee courante
    w=stage.objects.filter(entreprise=x.id_entreprise,annee=year).annotate(Count('stagiaires')).count() # compter le nombre d'organisme ayant recu des stagiares de stage type PFE pour chaque annee universitraire
    data.append(z)  #enregistrer les resultats dans data et data2 pour les renvoyer dans le dictionnaire
    data2.append(w)
 elif request.method=='POST':  # Ce code s'exectuera quand l'utilisateur fait une recherche sur les annes universitaires
    year = request.POST['search']
    labels=[]
    data=[]
    data2=[]
    data3=[]
    labels3=[]
    years=stage.objects.order_by().values_list('annee',flat=True).distinct() #extraire toutes les annees universitaires precedentes de la bdd
    for y in years:
       labels3.append(y) #les enregistrer deans labels3

    if year: #si year n'est pass vide on execute le meme code precedent mais selon l'annee entre par lutilisateur
        y=entreprise.objects.all()
        for x in y:
          labels.append(x.nom)
          z=stage.objects.filter(entreprise=x.id_entreprise,type='PFE',annee=year).count()
          w=stage.objects.filter(entreprise=x.id_entreprise,annee=year).annotate(Count('stagiaires')).count()
          data.append(z)
          data2.append(w)
        for an in labels3 :
         a=stage.objects.filter(type='PFE',annee=an).annotate(Count('entreprise')).count()
         data3.append(a)

    return render(request,'dashboard.html',{"data":data,"data2":data2,"labels":labels,"data3":data3,"labels3":labels3})

 return render(request,'dashboard.html',{"data":data,"data2":data2,"labels":labels,"data3":data3,"labels3":labels3})


def gethome(request):
     return render(request,'base.html')
     


