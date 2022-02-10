import email
from operator import mod
from pickle import TRUE
from pyexpat import model
from statistics import mode
from django.db import models
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.core.validators import MaxLengthValidator, MaxValueValidator,MinValueValidator

types=(
    ("OUVRIER","Stage OUVRIER"),
    ("PFE","Stage PFE"),
    ("TECH","Stage TECHNIQUE")
)
etudes=(
    ("1cp","1 er cycle preparatoire"),
    ("2cp","2eme cycle preparatoire"),
    ("1cs","1 er cycle superieur"),
    ("2cs","2 eme cycle superieur"),
    ("3cs","3 eme cycle superieur"),
)
specialites=(
    ("SIT","systeme d'information"),
    ("SIL","Systeme d'informations et logiciels "),
    ("SIQ","systeme informatique"),
    ("SID","Intelligence artifficielle"),
)
mentions=(
    ("Bien","Bien"),
    ("TBien","Tres Bien"),
    ("Excellent","Excellent"),
)

class stage(models.Model):
    code=models.CharField(max_length=12,primary_key=True)
    titre=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=types,default='PFE')
    description=models.CharField(max_length=100,default="")
    Convention=models.OneToOneField("convention",on_delete=CASCADE,blank=True,null=True)
    annee = models.CharField(max_length=10,null=True,blank=True)
    stagiaires=models.ManyToManyField('stagiaire',null=True)
    entreprise=models.ForeignKey('entreprise',on_delete=CASCADE)
    encadreurs=models.ForeignKey('encadreur',on_delete=CASCADE,null=True,blank=True)
    promoteurs=models.ForeignKey('promoteur',on_delete=CASCADE)
    Id_soutenance=models.ForeignKey('soutenance',null=True,blank=True,on_delete=CASCADE)
    mention=models.CharField(max_length=50,choices=mentions,default='None')
    def __str__(self):
        return self.code

#+++++++++++++++++++++++++++++++++++Stagiaire
class stagiaire(models.Model):
    matricule=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance=models.DateField()
    annee=models.CharField(max_length=3,choices=etudes,default="1cp")
    specialite=models.CharField(max_length=5,choices=specialites,default="section 1")
    section=models.CharField(max_length=10,default="section 1")
    def __int__(self):
        return self.matricule
#+++++++++++++++++++++++++++++++++++++Entreprise
class entreprise(models.Model):
    id_entreprise=models.CharField(max_length=12,primary_key=True)
    nom = models.CharField(max_length=30)
    numero=models.IntegerField(null=True)
    mail=models.EmailField(null=True)
    adresseEnt=models.CharField(max_length=30,null=True,blank=True)
    TypeEnt=models.TextField(null=True)
    def __str__(self):
        return self.nom
#++++++++++++++++++++++++++++++++++++++++++Rapport    
class rapport(models.Model):
    id_rapport=models.CharField(max_length=12,primary_key=True)
    titre = models.CharField(max_length=50)
    nbrpages=models.IntegerField(validators=[MaxValueValidator(120),MinValueValidator(6)])
    stage=models.ForeignKey('stage',on_delete=CASCADE,null=True)
    file=models.FileField(upload_to='media/rapports',null=True)
    def __str__(self):
        return self.titre
       
#+++++++++++++++++++++++++++++++++++++++++Convention
class convention (models.Model):
    id_convention = models.CharField(max_length=12,primary_key=True)
    numStage = models.OneToOneField('stage',on_delete=CASCADE,null=True)
    def __str__(self):
        return self.id_convention

#+++++++++++++++++++++++++++++++++++++++++++Promoteur
class promoteur (models.Model):
    id_promoteur=models.CharField(primary_key=True,max_length=12)
    nom_prom=models.CharField(max_length=30)
    prenom_prom=models.CharField(max_length=30)
    email_prom = models.EmailField(blank=True)
    numtel_prom=models.IntegerField(blank=True)
    nom_entreprise=models.ForeignKey('entreprise',on_delete=CASCADE)
    def __str__(self):
        return self.id_promoteur
#+++++++++++++++++++++++++++++++++++++++++Encadreur
class encadreur (models.Model):
    id_encadreur=models.CharField(primary_key=True,max_length=12)
    nom_encad=models.CharField(max_length=30)
    prenom_encad=models.CharField(max_length=30)
    email_encad = models.EmailField(blank=True)
    numtel_encad=models.IntegerField(blank=True)
    
    def __str__(self):
        return self.id_encadreur

#++++++++++++++++++++++++++++++++++++++++Fiche DE Suivie
class ficheSuivi (models.Model):
    id_ficheSuivi = models.CharField(max_length=12,primary_key=True)
    Encadreur = models.ForeignKey('encadreur',on_delete=CASCADE,null=True)
    date_depot = models.DateField()
    def __str__(self):
        return self.id_ficheSuivi
#+++++++++++++++++++++++++++++++++++++++++Fiche Evaluation
class ficheEvaluation (models.Model):
    id_ficheEvaluation = models.CharField(max_length=12,primary_key=True)
    Stage = models.OneToOneField('stage',on_delete=CASCADE)
    remarques=models.CharField(max_length=100)
    def __str__(self):
        return self.id_ficheEvaluation

#++++++++++++++++++++++++++++++++++++++++Soutenance
class soutenance(models.Model):
    id_soutenance= models.CharField(max_length=12,primary_key=True)
    date_soutenance= models.DateField()
    jury=models.ManyToManyField('encadreur')
    def __str__(self):
        return self.id_soutenance
        



