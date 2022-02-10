from logging import PlaceHolder
from django import forms
from django.forms import ModelForm, models
from . import models
class stageForm(ModelForm):
    class Meta:
        model=models.stage
        fields='__all__'
        widgets={ 
       'code':forms.TextInput(attrs={'class':'form-control'}),
       'titre':forms.TextInput(attrs={'class':'form-control '}),
       'type':forms.Select(attrs={'class':'form-control '}),
       'description':forms.Textarea(attrs={'class':'form-control'}),
       'Convention':forms.Select(attrs={'class':'form-control '}),
       'annee':forms.TextInput(attrs={'class':'form-control','placeholder':' / '}),
       'stagiaires':forms.SelectMultiple(attrs={'class':'form-control '}),
       'entreprise':forms.Select(attrs={'class':'form-control'}),
       'encadreurs':forms.Select(attrs={'class':'form-control'}),
       'promoteurs':forms.Select(attrs={'class':'form-control'}),
       'Id_soutenance':forms.Select(attrs={'class':'form-control'}),
       'mention':forms.Select(attrs={'class':'form-control'})
       }
        
class stagiaireForm(ModelForm):
    class Meta:
        model=models.stagiaire
        fields=('matricule','nom','prenom','specialite','section','annee','date_naissance')
        widgets={
            'matricule':forms.TextInput(attrs={'class':'form-control '}),
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'prenom':forms.TextInput(attrs={'class':'form-control'}),
            'date_naissance':forms.TextInput(attrs={'class':'form-control','label':'Date De Naissancs'}),
            'annee':forms.Select(attrs={'class':'form-control'}),
            'specialite':forms.Select(attrs={'class':'form-control'}),
            'section':forms.TextInput(attrs={'class':'form-control'})
        }

class entrepriseForm(ModelForm):
    class Meta:
        model=models.entreprise
        fields='__all__'
        widgets={
            'id_entreprise':forms.TextInput(attrs={'class':'form-control','labels':'Id'}),
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.EmailInput(attrs={'class':'form-control'}),
            'adresseEnt':forms.TextInput(attrs={'class':'form-control'}),
            'TypeEnt':forms.TextInput(attrs={'class':'form-control'})
        }


class rapportForm(ModelForm):
    class Meta:
        model=models.rapport
        fields='__all__'
        widgets={
            'id_rapport':forms.TextInput(attrs={'class':'form-control'}),
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'nbrpages':forms.TextInput(attrs={'class':'form-control'}),
            'stage':forms.Select(attrs={'class':'form-control'}),
            'file':forms.FileInput(attrs={'class':''})
        }


class conventionForm(ModelForm):
    class Meta:
        model=models.convention
        fields='__all__'
        widgets={
            'id_convention':forms.TextInput(attrs={'class':'form-control'}),
            'numStage':forms.Select(attrs={'class':'form-control'})
        }


class promoteurForm(ModelForm):
    class Meta:
        model=models.promoteur
        fields='__all__'
        widgets={
            'id_promoteur':forms.TextInput(attrs={'class':'form-control'}),
            'nom_prom':forms.TextInput(attrs={'class':'form-control'}),
            'prenom_prom':forms.TextInput(attrs={'class':'form-control'}),
            'email_prom':forms.TextInput(attrs={'class':'form-control'}),
            'numtel_prom':forms.TextInput(attrs={'class':'form-control'}),
            'nom_entreprise':forms.Select(attrs={'class':'form-control'})
        }

class encadreurForm(ModelForm):
    class Meta:
        model=models.encadreur
        fields='__all__'
        widgets={
            'id_encadreur':forms.TextInput(attrs={'class':'form-control'}),
            'nom_encad':forms.TextInput(attrs={'class':'form-control'}),
            'prenom_encad':forms.TextInput(attrs={'class':'form-control'}),
            'email_encad':forms.TextInput(attrs={'class':'form-control'}),
            'numtel_encad':forms.TextInput(attrs={'class':'form-control'}),
            'email_prom':forms.TextInput(attrs={'class':'form-control'})
            
        }

class ficheSuivForm(ModelForm):
    class Meta:
        model=models.ficheSuivi
        fields='__all__'
        widgets={
            'id_ficheSuivi':forms.TextInput(attrs={'class':'form-control'}),
            'Encadreur':forms.Select(attrs={'class':'form-control'}),
            'date_depot':forms.TextInput(attrs={'class':'form-control'})
        }

class ficheEvForm(ModelForm):
    class Meta:
        model=models.ficheEvaluation
        fields='__all__'
        widgets={
            'id_ficheEvaluation':forms.TextInput(attrs={'class':'form-control'}),
            'Stage':forms.Select(attrs={'class':'form-control'}),
            'remarques':forms.Textarea(attrs={'class':'form-control'})
        }

class soutenanceForm(ModelForm):
    class Meta:
        model=models.soutenance
        fields='__all__'
        widgets={
            'id_soutenance':forms.TextInput(attrs={'class':'form-control'}),
            'jury':forms.SelectMultiple(attrs={'class':'form-control'}),
            'date_soutenance':forms.SelectDateWidget(attrs={'class':'form-control'})

        }
