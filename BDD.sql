CREATE TABLE Livre (
    IdLivre INT PRIMARY KEY,
    Titre VARCHAR(255),
    Auteur VARCHAR(255),
    Genre VARCHAR(100),
    Format VARCHAR(50),
    Prix DECIMAL(10,2)
);

CREATE TABLE Coordonnees (
    IdCoordonnees INT PRIMARY KEY AUTO_INCREMENT,
    Adresse VARCHAR(255),
    Telephone VARCHAR(20)
);

CREATE TABLE Client (
    IdClient INT PRIMARY KEY,
    Nom VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    MotDePasse VARCHAR(255),
    IdCoordonnees INT,
    InscritNewsletter BOOLEAN,
    FOREIGN KEY (IdCoordonnees) REFERENCES Coordonnees(IdCoordonnees)
);

CREATE TABLE PreferenceGenre (
    IdClient INT,
    Genre VARCHAR(100),
    PRIMARY KEY (IdClient, Genre),
    FOREIGN KEY (IdClient) REFERENCES Client(IdClient)
);

CREATE TABLE Commande (
    IdCommande INT PRIMARY KEY,
    IdClient INT,
    DateCommande DATE,
    MontantTotal DECIMAL(10,2),
    FraisLivraison DECIMAL(10,2),
    Status VARCHAR(50),
    FOREIGN KEY (IdClient) REFERENCES Client(IdClient)
);

CREATE TABLE CommandeLivre (
    IdCommande INT,
    IdLivre INT,
    PRIMARY KEY (IdCommande, IdLivre),
    FOREIGN KEY (IdCommande) REFERENCES Commande(IdCommande),
    FOREIGN KEY (IdLivre) REFERENCES Livre(IdLivre)
);

CREATE TABLE Commentaire (
    IdCommentaire INT PRIMARY KEY,
    IdLivre INT,
    IdClient INT,
    Contenu TEXT,
    Date DATE,
    FOREIGN KEY (IdLivre) REFERENCES Livre(IdLivre),
    FOREIGN KEY (IdClient) REFERENCES Client(IdClient)
);

CREATE TABLE Recommandation (
    IdRecommandation INT PRIMARY KEY,
    IdClient INT,
    DateGeneration DATE,
    FOREIGN KEY (IdClient) REFERENCES Client(IdClient)
);

CREATE TABLE RecommandationLivre (
    IdRecommandation INT,
    IdLivre INT,
    PRIMARY KEY (IdRecommandation, IdLivre),
    FOREIGN KEY (IdRecommandation) REFERENCES Recommandation(IdRecommandation),
    FOREIGN KEY (IdLivre) REFERENCES Livre(IdLivre)
);

CREATE TABLE Newsletter (
    IdNewsletter INT PRIMARY KEY,
    IdClient INT,
    DateGeneration DATE,
    FOREIGN KEY (IdClient) REFERENCES Client(IdClient)
);

CREATE TABLE TypesContenusNewsletter (
    IdNewsletter INT,
    TypeContenu VARCHAR(100),
    PRIMARY KEY (IdNewsletter, TypeContenu),
    FOREIGN KEY (IdNewsletter) REFERENCES Newsletter(IdNewsletter)
);

CREATE TABLE ResponsableMarketing (
    IdResponsable INT PRIMARY KEY,
    Nom VARCHAR(100)
);

CREATE TABLE DataAnalyst (
    IdAnalyst INT PRIMARY KEY,
    Nom VARCHAR(100),
    Email VARCHAR(100)
);

-- Relations "Utilise les recommandations" entre ResponsableMarketing et Recommandation
CREATE TABLE ResponsableRecommandation (
    IdResponsable INT,
    IdRecommandation INT,
    PRIMARY KEY (IdResponsable, IdRecommandation),
    FOREIGN KEY (IdResponsable) REFERENCES ResponsableMarketing(IdResponsable),
    FOREIGN KEY (IdRecommandation) REFERENCES Recommandation(IdRecommandation)
);

-- Relation d’analyse : DataAnalyst -> Client
CREATE TABLE AnalyseClient (
    IdAnalyst INT,
    IdClient INT,
    PRIMARY KEY (IdAnalyst, IdClient),
    FOREIGN KEY (IdAnalyst) REFERENCES DataAnalyst(IdAnalyst),
    FOREIGN KEY (IdClient) REFERENCES Client(IdClient)
);
