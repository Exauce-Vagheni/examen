class Soldat:
    def __init__(self,nom,postnom,matricule,age,solde=0,etat_de_vie="vivant",grade="caporal",fonction="en fonction"):
        self.nom=nom
        self.postnom=postnom
        self.matricule=matricule
        self.solde=solde
        self.etat_de_vie=etat_de_vie
        self.grade=grade
        self.age=age
        self.fonction=fonction
    def payer(self,montant):
        self.solde=self.solde+montant
    def monter_grade(self,grade):
        self.grade=grade
    def mourir(self,etat_de_vie="décedé"):
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
    def __init__(self, nom, postnom, matricule, age, solde=0, etat_de_vie="vivant", grade="caporal",
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

    """Notion sur la polymorphisme"""
    def monter_grade(self, grade):
        print(f"Un retraité ne peut pas monter de grade")
class Handicape(Soldat):
    def __init__(self, nom, postnom, matricule, age, solde=0, etat_de_vie="vivant", grade="caporal",
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

    """Notion sur la polymorphisme"""
    def monter_grade(self,grade):
        print(f"Un handicapé ne peut pas monter de grade")
