class Soldat:
    def __init__(self,nom,postnom,matricule,age,solde=0,etat_de_vie="vivant",grade="caporal"):
        self.__nom=nom
        self.__postnom=postnom
        self.__matricule=matricule
        self.__solde=solde
        self.__etat_de_vie=etat_de_vie
        self.__grade=grade
        self.__age=age
    def payer(self,montant):
        self.solde=self.solde+montant
    def monter_grade(self,grade):
        self.grade=grade
    def mourir(self,etat_de_vie="décedé"):
        self.etat_de_vie=etat_de_vie
    def afficher_soldat(self):
        print(f"Nom: {self.nom}")
        print(f"Postnom: {self.postnom}")
        print(f"Matricule: {self.matricule}")
        print(f"Solde: {self.solde}")
        print(f"Etat de vie: {self.etat_de_vie}")
        print(f"Grade: {self.grade}")