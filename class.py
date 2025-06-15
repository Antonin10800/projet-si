from datetime import date
from typing import List, Optional
import pandas as pd
import os
import matplotlib.pyplot as plt

def afficher_top_livres(self, top_n: int = 10):
    top = self.top_livres_plus_vendus(top_n)
    plt.figure(figsize=(10, 6))
    plt.barh(top["titre"], top["nb_ventes"])
    plt.xlabel("Nombre de ventes")
    plt.title(f"Top {top_n} des livres les plus vendus")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


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


class ConnecteurBibliotheque:
    def __init__(self, fichier_excel: str = "BDD.xlsx"):
        if not os.path.isfile(fichier_excel):
            raise FileNotFoundError(f"Fichier non trouvé : {fichier_excel}")
        self.fichier_excel = fichier_excel
        self.donnees = {}

    def charger_donnees(self):
        self.donnees = pd.read_excel(self.fichier_excel, sheet_name=None)

    def get_table(self, nom_table: str) -> pd.DataFrame:
        if not self.donnees:
            self.charger_donnees()
        if nom_table not in self.donnees:
            raise ValueError(f"Table {nom_table} non trouvée.")
        return self.donnees[nom_table]

    def lister_tables(self):
        if not self.donnees:
            self.charger_donnees()
        return list(self.donnees.keys())

    # Méthodes orientées objet

    def get_client_par_id(self, id_client: int) -> pd.Series:
        clients = self.get_table("Clients")
        resultat = clients[clients["id_client"] == id_client]
        if resultat.empty:
            raise ValueError(f"Aucun client avec l'ID {id_client}")
        return resultat.iloc[0]

    def get_commandes_par_client(self, id_client: int) -> pd.DataFrame:
        commandes = self.get_table("Commandes")
        return commandes[commandes["id_client"] == id_client]

    def get_livres_par_commande(self, id_commande: int) -> pd.DataFrame:
        commandes = self.get_table("Commandes")
        livres = self.get_table("Livres")
        commande = commandes[commandes["id_commande"] == id_commande]
        if commande.empty:
            raise ValueError(f"Aucune commande avec l'ID {id_commande}")
        liste_ids = commande.iloc[0]["livres"].split("|")
        ids = list(map(int, liste_ids))
        return livres[livres["id_livre"].isin(ids)]

    def get_commentaires_par_livre(self, id_livre: int) -> pd.DataFrame:
        commentaires = self.get_table("Commentaires")
        return commentaires[commentaires["id_livre"] == id_livre]

    def get_clients_ayant_achete_livre(self, id_livre: int) -> pd.DataFrame:
        commandes = self.get_table("Commandes")
        clients = self.get_table("Clients")
        commandes_contenant_livre = commandes[
            commandes["livres"].apply(lambda x: str(id_livre) in x.split("|"))
        ]
        ids_clients = commandes_contenant_livre["id_client"].unique()
        return clients[clients["id_client"].isin(ids_clients)]

    def rechercher_livres_par_mot_cle(self, mot_cle: str) -> pd.DataFrame:
        livres = self.get_table("Livres")
        mot_cle = mot_cle.lower()
        return livres[livres["titre"].str.lower().str.contains(mot_cle)]

    def chiffre_affaires_par_mois(self) -> pd.DataFrame:
        commandes = self.get_table("Commandes")
        livres = self.get_table("Livres")

        # Exploser les livres par commande
        lignes = []
        for _, row in commandes.iterrows():
            for id_livre in row["livres"].split("|"):
                lignes.append({
                    "id_commande": row["id_commande"],
                    "date": pd.to_datetime(row["date_commande"]),
                    "id_livre": int(id_livre),
                    "frais_livraison": row["frais_livraison"] / len(row["livres"].split("|"))
                })
        df = pd.DataFrame(lignes)

        # Fusion avec les livres
        df = df.merge(livres, on="id_livre", how="left")
        df["mois"] = df["date"].dt.to_period("M")
        df["total"] = df["prix"] + df["frais_livraison"]

        return df.groupby("mois")["total"].sum().reset_index()
    
    def genres_preferes_vs_achats(self) -> pd.DataFrame:
        clients = self.get_table("Clients")
        commandes = self.get_table("Commandes")
        livres = self.get_table("Livres")

        stats = []

        for _, client in clients.iterrows():
            commandes_client = commandes[commandes["id_client"] == client["id_client"]]
            livres_achetes_ids = commandes_client["livres"].str.split("|").explode().dropna().astype(int)
            livres_achetes = livres[livres["id_livre"].isin(livres_achetes_ids)]
            genres_achetes = livres_achetes["genre"].value_counts()
            genres_pref = client["preference_genre"].split("|")
            pourcentage_pref = sum(genres_achetes.get(g, 0) for g in genres_pref) / max(1, len(livres_achetes))
            stats.append({
                "id_client": client["id_client"],
                "nom": client["nom"],
                "total_livres": len(livres_achetes),
                "correspondance_genres (%)": round(pourcentage_pref * 100, 1)
            })

        return pd.DataFrame(stats).sort_values("correspondance_genres (%)", ascending=False)

    def engagement_newsletter_vs_commandes(self) -> pd.DataFrame:
        clients = self.get_table("Clients")
        commandes = self.get_table("Commandes")

        commandes_par_client = commandes["id_client"].value_counts()
        clients["nb_commandes"] = clients["id_client"].map(commandes_par_client).fillna(0).astype(int)
        return clients.groupby("inscrit_newsletter")["nb_commandes"].agg(["mean", "count"])
        
if __name__ == "__main__":
    connecteur = ConnecteurBibliotheque()
    connecteur.charger_donnees()

    # Afficher les infos du client n°1
    client = connecteur.get_client_par_id(1)
    print("Client :", client["nom"])

    # Commandes passées par ce client
    commandes = connecteur.get_commandes_par_client(1)
    print("Commandes du client 1 :", commandes)

    # Livres de la première commande du client
    if not commandes.empty:
        id_commande = commandes.iloc[0]["id_commande"]
        livres = connecteur.get_livres_par_commande(id_commande)
        print("Livres de la commande :", livres[["titre", "auteur"]])

    print("🔍 Recherche de livres contenant 'python' :")
    resultats = connecteur.rechercher_livres_par_mot_cle("python")
    print(resultats[["id_livre", "titre"]])

    print("\n👥 Clients ayant acheté le livre ID 3 :")
    clients = connecteur.get_clients_ayant_achete_livre(3)
    print(clients[["id_client", "nom"]])

   
