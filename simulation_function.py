import numpy as np

# Définition de la fonction température extérieur en fonction de la date
def temp_exterieur(jour: int, mois: int, bruit_de_fond: float = 5.0) -> float:
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
    
    x = mois + jour / 32
    temperature_base = 10 * np.sin((np.pi / 5.5) * x - np.pi / 1.5) + 15
    bruit = np.random.normal(0, bruit_de_fond)  # Bruit de fond aléatoire autour de zéro
    
    return round(temperature_base + bruit, 2)




def temperature_produit(temp_exterieur: float, bruit_de_fond: float = 0.5) -> float:
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
    
    # Ajout d'un bruit de fond aléatoire
    bruit = np.random.normal(0, bruit_de_fond)
    
    # Température finale avec bruit ajouté
    return round(temperature_base + bruit, 2)


temp_ext = temp_exterieur(1,1)  # Exemple de température extérieure
temp_int = temperature_produit(temp_ext)
print(f"La température produit est de {temp_int}°C pour une température extérieure de {temp_ext}°C.")
