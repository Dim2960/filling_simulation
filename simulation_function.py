import numpy as np
from datetime import datetime
import math

# Définition de la fonction température extérieur en fonction de la date
def temp_exterieur(date: datetime, bruit_de_fond: float = 3.0) -> float:
    """
    Calcule une température extérieure simulée en fonction du jour et du mois, 
    avec un bruit de fond aléatoire pour simuler des variations naturelles.

    Cette fonction utilise une fonction sinus pour générer une température
    qui varie périodiquement en fonction de la date (jour et mois). La
    température varie autour d'une valeur moyenne de 15°C avec une amplitude
    de 10°C. Un bruit de fond est ajouté pour simuler des fluctuations naturelles.

    Paramètres :
    - jour (int) : Le jour du mois (1 à 31).
    - mois (int) : Le mois de l'année (1 à 12).
    - bruit_de_fond (float) : Amplitude du bruit de fond aléatoire (en °C), par défaut 1.0.

    Retourne :
    - float : La température simulée pour le jour et le mois spécifiés, avec bruit ajouté.

    Exemple :
    >>> temp_exterieur(15, 6)
    25.7
    """

    mois = date.month
    jour = date.day
    
    x = mois + jour / 32
    temperature_base = 10 * np.sin((np.pi / 5.5) * x - np.pi / 1.5) + 15
    bruit = np.random.normal(0, bruit_de_fond)  # Bruit de fond aléatoire autour de zéro
    
    return round(temperature_base + bruit, 2)




def temperature_produit(temp_exterieur: float, bruit_de_fond: float = 0.2) -> float:
    """
    Calcule la température d'un produit dans une pièce en fonction de la température extérieure,
    en utilisant la fonction y = (1/300) * (temp_exterieur - 20)^3 + 20,
    avec un bruit de fond pour simuler des variations naturelles.

    Paramètres :
    - temp_exterieur (float) : La température extérieure.
    - bruit_de_fond (float) : Intensité du bruit de fond (écart-type), par défaut 0.5°C.

    Retourne :
    - float : La température du produit dans la pièce, avec bruit ajouté.
    """
    # Calcul de la température du produit sans bruit avec la nouvelle fonction mathématique
    temperature_base = (1 / 800) * (temp_exterieur - 15) ** 3 + 20
    #temperature_base = 1 * (temp_exterieur) + 20
    
    # Ajout d'un bruit de fond aléatoire
    bruit = np.random.normal(0, bruit_de_fond)
    
    temp_produit = round(temperature_base + bruit, 2)

    # Limitation des températures entre 0°C et 50°C
    # La température finale avec bruit ajouté
    temp_produit_corrige = max(0, min(temp_produit, 50))

    return temp_produit_corrige








def ratio_cadence(densite: float, viscosite: float, tension_surface: float = 72.8, teneur_particule: float = 0, teneur_gaz: float = 0) -> float:
    """
    Calcule un ratio de réduction de cadence compris entre 0 et 1 basé sur les caractéristiques 
    physiques d'un fluide. Ce ratio peut être utilisé pour ajuster une cadence nominale en fonction 
    des propriétés du fluide, telles que la densité, la viscosité, la teneur en particules solides, 
    la tension de surface et la teneur en gaz dissous.

    Parameters:
    - densite (float): La densité du fluide, valeur entre 0 et 1.
    - viscosite (float): La viscosité du fluide en mPa.s, valeur entre 0 et 100.
    - tension_surface (float): La tension de surface du fluide en mN/m, avec une valeur par défaut de 72.8 (eau).
    - teneur_particule (float): La teneur en particules solides, valeur entre 0 et 1.
    - teneur_gaz (float): La teneur en gaz dissous, valeur entre 0 et 1.

    Returns:
    - float: Un ratio de réduction de cadence compris entre 0 et 1.
    """
    
    # Normalisation des paramètres
    densite_normalisee = (densite - 0) / (1 - 0)  # Normalisée entre 0 et 1
    viscosite_normalisee = (viscosite - 0) / (100 - 0)  # Normalisée entre 0 et 1
    tension_surface_normalisee = (tension_surface - 20) / (150 - 20)  # Normalisée entre 0 et 1
    teneur_particule_normalisee = teneur_particule  # Déjà entre 0 et 1
    teneur_gaz_normalisee = teneur_gaz  # Déjà entre 0 et 1

    # Calcul des contributions individuelles
    y_densite = -1.633 * (densite - 1.1) ** 2 + 1
    y_viscosite = -0.4 * ((viscosite - 50) / 50) ** 2 + 1
    y_tension_surface = 0.1193 * math.log(tension_surface + 1) + 0.5
    y_teneur_gaz = -3.906 * teneur_gaz ** 4 + 1
    y_teneur_particule = -1000 * teneur_particule ** 4 + 1
    
    # Poids pour chaque contribution, ajustables en fonction de leur importance relative
    w_densite = 0.1
    w_viscosite = 0.7
    w_tension_surface = 0.05
    w_teneur_gaz = 0.05
    w_teneur_particule = 0.1
    
    # Calcul du ratio final en combinant les contributions pondérées
    ratio = (
        w_densite * y_densite +
        w_viscosite * y_viscosite +
        w_tension_surface * y_tension_surface +
        w_teneur_gaz * y_teneur_gaz +
        w_teneur_particule * y_teneur_particule
    )
    
    # S'assurer que le ratio est bien entre 0 et 1
    ratio = max(0, min(ratio, 1))
    
    return ratio

