# Génération de Données d'une Ligne de Conditionnement Automatisée

## 🌟 Introduction

Ce projet a pour objectif de générer artificiellement des données simulant le fonctionnement d'une ligne de conditionnement automatisée. Grâce à ces données, il est possible de visualiser la performance de la ligne de production et d'analyser les facteurs influençant cette performance.

## 🎯 Objectifs du Projet

- **Simulation de Production :** Reproduire le comportement d'une ligne de conditionnement avec diverses phases (production, changeover, arrêts programmés et non programmés).
- **Analyse des Performances :** Fournir des jeux de données détaillés permettant d'étudier la cadence de production et l'impact des caractéristiques physiques des produits.
- **Étude des Facteurs d'Influence :** Examiner comment des paramètres tels que la densité, la viscosité, et d'autres caractéristiques affectent la cadence réelle de production.

## 🗃️ Structure du Projet

Le projet est organisé selon la structure suivante :

```
├── data/
│    └── processed/                  # Données générées
├── scripts/
│    ├── data_filling_gen.py         # Génère les données de production (détails minute par minute)
│    ├── product_gen.py              # Crée la liste des produits avec leurs caractéristiques et calcule le ratio de cadence
│    ├── simulation_function.py      # Contient les fonctions de simulation (température extérieure, température produit, calcul du ratio)
│    └── table_date_gen.py           # Génère une table de dates à intervalle d'une minute sur la période simulée
├── outputs/
│    └── pwBI/                       # Rapport Power BI
├── .gitignore                   
└── README.md  
```

## 💡 Fonctionnalités Principales

- **Simulation de Production :**
  - Génération d’un fichier CSV contenant les données de production simulées, incluant la cadence, les arrêts et les temps de changeover.
  - Prise en compte des périodes de production et d’arrêt (programmés, non programmés, et de qualité).

- **Gestion des Produits :**
  - Création d’un fichier CSV listant les produits avec leurs caractéristiques physiques (densité, viscosité, tension superficielle, etc.).
  - Calcul d’un ratio de réduction de cadence à partir de ces caractéristiques pour influencer la simulation.

- **Simulation des Conditions Environnementales :**
  - Génération de températures extérieures en fonction de la date et ajout de bruit de fond pour simuler des variations naturelles.
  - Simulation de la température du produit en fonction de la température extérieure.

- **Table de Dates :**
  - Création d’un fichier CSV contenant une table de dates détaillée (année, mois, jour, heure, minute) sur la période de simulation.

## 🛠️ Prérequis

- **Python 3.12**
- **Bibliothèques Python :**
  - [pandas](https://pandas.pydata.org/)
  - [numpy](https://numpy.org/)

Pour installer les dépendances, utilisez par exemple :

```bash
pip install pandas numpy
```

## 🔍 Installation et Utilisation

1. **Cloner le dépôt **  
   Assurez-vous d’avoir tous les fichiers du projet (les scripts Python et l'image de la structure du projet).

2. **Installation des dépendances**  
   Installez les bibliothèques requises en exécutant la commande indiquée dans les pré-requis.

3. **Exécution des Scripts :**  
   - **Génération de la liste des produits :**  
     Lancez `product_gen.py` pour créer le fichier CSV contenant les produits et leurs caractéristiques.
   - **Génération des données de production :**  
     Exécutez `data_filling_gen.py` pour simuler la production et générer le fichier CSV `production_data.csv`.
   - **Génération de la table de dates :**  
     Exécutez `table_date_gen.py` pour créer la table des dates utilisée dans la simulation.

Exemple pour lancer le script de simulation :

```bash
python data_filling_gen.py
```

## 📊 Analyse des Données

Les fichiers CSV générés (notamment `production_data.csv`, `products_list_gpt.csv` et `table_date.csv`) peuvent être exploités avec vos outils d’analyse préférés (Jupyter Notebook, Excel, Power BI, etc.) pour :

- Visualiser les performances de la ligne de conditionnement.
- Étudier l’impact des arrêts programmés et non programmés sur la cadence.
- Analyser l’influence des caractéristiques des produits sur la performance de la production.

🔗 **Accédez à mes exemples de rapport Power BI** :  
- [![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-orange?logo=powerbi)](https://app.powerbi.com/view?r=eyJrIjoiMGFlZjQ3N2EtYjI1ZC00N2Y3LWI1ZmYtMzg4M2FhZmIzMTJiIiwidCI6IjQ0OTFmMGVlLWY1MDMtNDcyNi1hNWViLTFmMGM0ZGFjODJhOSJ9) 
- [![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-orange?logo=powerbi)](https://app.powerbi.com/view?r=eyJrIjoiMjZiNmQ5YWQtNTQxNS00OWY1LWE2ZmItODQyYmJlODg4OGE4IiwidCI6IjQ0OTFmMGVlLWY1MDMtNDcyNi1hNWViLTFmMGM0ZGFjODJhOSJ9) 

## 🛢️ Personnalisation

Vous pouvez adapter le projet en modifiant :

- **Les Paramètres de Simulation :**  
  Dans `data_filling_gen.py`, ajustez le nombre de productions, les cadences nominales, les durées de changeover, etc.

- **Les Caractéristiques des Produits :**  
  Dans `product_gen.py`, modifiez ou ajoutez des produits et ajustez le calcul du ratio de réduction de cadence.

- **Les Fonctions de Simulation :**  
  Dans `simulation_function.py`, personnalisez la manière dont la température extérieure et celle des produits sont simulées, ainsi que le calcul du ratio.

## 🗨️ Conclusion

Ce projet offre une plateforme flexible pour simuler le fonctionnement d’une ligne de conditionnement automatisée. Les données générées permettent de visualiser et d’analyser la performance de la production, tout en étudiant l’impact de divers paramètres sur celle-ci.  
N’hésitez pas à apporter des contributions ou à suggérer des améliorations pour enrichir ce projet.

