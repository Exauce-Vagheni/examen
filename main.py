"""Notion sur l' abstraction"""
from abc import ABC
class militaire(ABC):
    def enguerre(self):
        print("Ce soldant est en guerre")
class Soldat(militaire):
    def __init__(self,nom,postnom,matricule,age,solde=0,etat_de_vie="vivant",grade="caporal",fonction="en fonction"):
        """Notion sur l'abstraction"""
        self.__nom=nom
        self.__postnom=postnom
        self.__matricule=matricule
        self.__solde=solde
        self.__etat_de_vie=etat_de_vie
        self.__grade=grade
        self.__age=age
        self.__fonction=fonction
    def payer(self,montant):
        self.solde=self.solde+montant
    def monter_grade(self,grade):
        self.grade=grade
    def mourir(self,etat_de_vie="décedé en tant que soldat"):
        self.etat_de_vie=etat_de_vie
        self.fonction="pas en fonction"
    def afficher_soldat(self):
        print(f"Nom: {self.nom}")
        print(f"Postnom: {self.postnom}")
        print(f"Matricule: {self.matricule}")
        print(f"Age: {self.age}")
        print(f"Solde: {self.solde}")
        print(f"Etat de vie: {self.etat_de_vie}")
        print(f"Grade: {self.grade}")
        print(f"Fonction: {self.fonction}")

"""Notion d'heritage"""
class Veteran(Soldat):
    def __init__(self, nom, postnom, matricule, age, solde=0, etat_de_vie="vivant en retraite", grade="caporal",
                 fonction="Veteran"):
        self.nom = nom
        self.postnom = postnom
        self.matricule = matricule
        self.solde = solde
        self.etat_de_vie = etat_de_vie
        self.grade = grade
        self.age = age
        self.fonction = fonction
    def payer_frais_pension(self):
        self.solde = self.solde + (self.solde / 4)

    """Notion sur la surchage"""
    def mourir(self):
        super().mourir(etat_de_vie="Mort en etant vétéran")

class Handicape(Soldat):
    def __init__(self, nom, postnom, matricule, age, solde=0, etat_de_vie="vivant avec handicap", grade="caporal",
                 fonction="Handicape"):
        self.nom = nom
        self.postnom = postnom
        self.matricule = matricule
        self.solde = solde
        self.etat_de_vie = etat_de_vie
        self.grade = grade
        self.age = age
        self.fonction = fonction
    def payer_frais_pension(self):
        self.solde = self.solde + (self.solde / 2)

    """Notion sur la surchage"""
    def mourir(self):
        super().mourir(etat_de_vie="Mort avec handicap")

soldat= Veteran("Exauce","Vagheni",4422,20)
soldat.enguerre()
soldat.mourir()
soldat.afficher_soldat()