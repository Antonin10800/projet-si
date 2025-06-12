from datetime import date
from typing import List, Optional


class Livre:
    def __init__(self, id_livre: int, titre: str, auteur: str, genre: str,
                 format_: str, prix: float):
        self.id_livre = id_livre
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.format = format_
        self.prix = prix

    def afficher_details(self):
        return f"{self.titre} par {self.auteur}, genre: {self.genre}, format: {self.format}, prix: {self.prix} €"


class Coordonnees:
    def __init__(self, adresse: str, telephone: str):
        self.adresse = adresse
        self.telephone = telephone


class Client:
    def __init__(self, id_client: int, nom: str, email: str, mot_de_passe: str,
                 preference_genre: List[str], coordonnees: Coordonnees, inscrit_newsletter: bool):
        self.id_client = id_client
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.preference_genre = preference_genre
        self.coordonnees = coordonnees
        self.historique_achats: List[Commande] = []
        self.inscrit_newsletter = inscrit_newsletter

    def consulter_catalogue(self):
        pass

    def ajouter_au_panier(self, livre: Livre):
        pass

    def payer_commande(self, commande):
        commande.valider_paiement()

    def mettre_a_jour_preferences(self, genres: List[str]):
        self.preference_genre = genres

    def poster_commentaire(self, commentaire):
        pass


class Commande:
    def __init__(self, id_commande: int, client: Client, livres: List[Livre], date_commande: date,
                 frais_livraison: float, status: str):
        self.id_commande = id_commande
        self.client = client
        self.livres = livres
        self.date_commande = date_commande
        self.frais_livraison = frais_livraison
        self.status = status

    def calculer_total(self):
        return sum(livre.prix for livre in self.livres) + self.frais_livraison

    def valider_paiement(self):
        self.status = "Payée"


class Commentaire:
    def __init__(self, id_commentaire: int, livre: Livre, client: Client, contenu: str, date_: date):
        self.id_commentaire = id_commentaire
        self.livre = livre
        self.client = client
        self.contenu = contenu
        self.date = date_


class Recommandation:
    def __init__(self, id_recommandation: int, client: Client, livres_recommandes: List[Livre], date_generation: date):
        self.id_recommandation = id_recommandation
        self.client = client
        self.livres_recommandes = livres_recommandes
        self.date_generation = date_generation

    def generer(self):
        pass

    def modifier_preferences_lecture(self):
        pass


class Newsletter:
    def __init__(self, id_newsletter: int, types_contenus: List[str], client: Client, date_generation: date):
        self.id_newsletter = id_newsletter
        self.types_contenus = types_contenus
        self.client = client
        self.date_generation = date_generation

    def envoyer_automatiquement(self):
        pass


class ResponsableMarketing:
    def __init__(self, id_responsable: int, nom: str):
        self.id_responsable = id_responsable
        self.nom = nom

    def emettre_recommandation(self):
        pass

    def planifier_email_cible(self, client_segment: List[Client]):
        pass

    def personnaliser_campagnes(self):
        pass


class DataAnalyst:
    def __init__(self, id_analyst: int, nom: str, email: str):
        self.id_analyst = id_analyst
        self.nom = nom
        self.email = email

    def analyser_genres_preferes(self):
        pass

    def creer_tableaux_de_bord(self):
        pass

    def optimiser_algorithme_recommandation(self):
        pass

    def exporter_rapports(self):
        pass
