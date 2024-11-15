import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from simulation_function import temp_exterieur,temperature_produit


# Paramètres globaux
products = list(range(1, 51))
physico_chemy = [
    {'ID': 1, 'Nom du produit': 'PackEasy 500', 'Densité': 0.85, 'Viscosité (mPa.s)': 138.7, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.015},
    {'ID': 2, 'Nom du produit': 'EcoWrap Plus', 'Densité': 0.95, 'Viscosité (mPa.s)': 64.06, 'Ratio': 0, 'Tension superficielle (N/m)': 0.028, 'Teneur en particules (ratio)': 0.008, 'Teneur en gaz (ratio)': 0.012},
    {'ID': 3, 'Nom du produit': 'FlexiSeal Pro', 'Densité': 1.15, 'Viscosité (mPa.s)': 10.77, 'Ratio': 0, 'Tension superficielle (N/m)': 0.034, 'Teneur en particules (ratio)': 0.014, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 4, 'Nom du produit': 'UltraShield', 'Densité': 1.28, 'Viscosité (mPa.s)': 111.47, 'Ratio': 0, 'Tension superficielle (N/m)': 0.033, 'Teneur en particules (ratio)': 0.009, 'Teneur en gaz (ratio)': 0.020},
    {'ID': 5, 'Nom du produit': 'WrapTech 3000', 'Densité': 0.94, 'Viscosité (mPa.s)': 140.19, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.013},
    {'ID': 6, 'Nom du produit': 'QuickPack Max', 'Densité': 1.36, 'Viscosité (mPa.s)': 41.46, 'Ratio': 0, 'Tension superficielle (N/m)': 0.029, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.011},
    {'ID': 7, 'Nom du produit': 'BioGuard X', 'Densité': 0.86, 'Viscosité (mPa.s)': 62.86, 'Ratio': 0, 'Tension superficielle (N/m)': 0.027, 'Teneur en particules (ratio)': 0.015, 'Teneur en gaz (ratio)': 0.014},
    {'ID': 8, 'Nom du produit': 'SmartWrap', 'Densité': 0.86, 'Viscosité (mPa.s)': 77.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.032, 'Teneur en particules (ratio)': 0.013, 'Teneur en gaz (ratio)': 0.017},
    {'ID': 9, 'Nom du produit': 'ProFlex Lite', 'Densité': 0.92, 'Viscosité (mPa.s)': 76.96, 'Ratio': 0, 'Tension superficielle (N/m)': 0.026, 'Teneur en particules (ratio)': 0.008, 'Teneur en gaz (ratio)': 0.012},
    {'ID': 10, 'Nom du produit': 'EcoPack Pro', 'Densité': 1.0, 'Viscosité (mPa.s)': 57.1, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.014, 'Teneur en gaz (ratio)': 0.016},
    {'ID': 11, 'Nom du produit': 'SafeWrap Elite', 'Densité': 1.29, 'Viscosité (mPa.s)': 13.73, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.010},
    {'ID': 12, 'Nom du produit': 'MaxiGuard', 'Densité': 0.97, 'Viscosité (mPa.s)': 102.96, 'Ratio': 0, 'Tension superficielle (N/m)': 0.033, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.019},
    {'ID': 13, 'Nom du produit': 'SpeedSeal', 'Densité': 1.2, 'Viscosité (mPa.s)': 7.17, 'Ratio': 0, 'Tension superficielle (N/m)': 0.028, 'Teneur en particules (ratio)': 0.007, 'Teneur en gaz (ratio)': 0.015},
    {'ID': 14, 'Nom du produit': 'EcoFlex 800', 'Densité': 0.9, 'Viscosité (mPa.s)': 103.46, 'Ratio': 0, 'Tension superficielle (N/m)': 0.032, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.017},
    {'ID': 15, 'Nom du produit': 'UltraPack One', 'Densité': 1.14, 'Viscosité (mPa.s)': 82.92, 'Ratio': 0, 'Tension superficielle (N/m)': 0.029, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 16, 'Nom du produit': 'SecureWrap X', 'Densité': 1.32, 'Viscosité (mPa.s)': 83.55, 'Ratio': 0, 'Tension superficielle (N/m)': 0.027, 'Teneur en particules (ratio)': 0.013, 'Teneur en gaz (ratio)': 0.014},
    {'ID': 17, 'Nom du produit': 'GreenWrap', 'Densité': 1.09, 'Viscosité (mPa.s)': 19.91, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.009, 'Teneur en gaz (ratio)': 0.013},
    {'ID': 18, 'Nom du produit': 'FlexiPack Pro', 'Densité': 0.9, 'Viscosité (mPa.s)': 54.75, 'Ratio': 0, 'Tension superficielle (N/m)': 0.034, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.016},
    {'ID': 19, 'Nom du produit': 'EcoLock', 'Densité': 1.37, 'Viscosité (mPa.s)': 58.71, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.017},
    {'ID': 20, 'Nom du produit': 'PackMaster 360', 'Densité': 1.32, 'Viscosité (mPa.s)': 49.95, 'Ratio': 0, 'Tension superficielle (N/m)': 0.033, 'Teneur en particules (ratio)': 0.008, 'Teneur en gaz (ratio)': 0.015},
    {'ID': 21, 'Nom du produit': 'MegaWrap', 'Densité': 1.21, 'Viscosité (mPa.s)': 61.3, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 22, 'Nom du produit': 'EcoPlus Secure', 'Densité': 0.99, 'Viscosité (mPa.s)': 112.9, 'Ratio': 0, 'Tension superficielle (N/m)': 0.034, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.013},
    {'ID': 23, 'Nom du produit': 'UltraShield 2.0', 'Densité': 1.28, 'Viscosité (mPa.s)': 127.5, 'Ratio': 0, 'Tension superficielle (N/m)': 0.028, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.020},
    {'ID': 24, 'Nom du produit': 'WrapGuard', 'Densité': 1.05, 'Viscosité (mPa.s)': 85.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.032, 'Teneur en particules (ratio)': 0.009, 'Teneur en gaz (ratio)': 0.014},
    {'ID': 25, 'Nom du produit': 'BioSeal Premium', 'Densité': 1.12, 'Viscosité (mPa.s)': 98.2, 'Ratio': 0, 'Tension superficielle (N/m)': 0.029, 'Teneur en particules (ratio)': 0.014, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 26, 'Nom du produit': 'FlexSecure', 'Densité': 0.96, 'Viscosité (mPa.s)': 74.2, 'Ratio': 0, 'Tension superficielle (N/m)': 0.033, 'Teneur en particules (ratio)': 0.013, 'Teneur en gaz (ratio)': 0.011},
    {'ID': 27, 'Nom du produit': 'QuickWrap', 'Densité': 1.15, 'Viscosité (mPa.s)': 58.5, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.016},
    {'ID': 28, 'Nom du produit': 'SealGuard X', 'Densité': 1.33, 'Viscosité (mPa.s)': 90.1, 'Ratio': 0, 'Tension superficielle (N/m)': 0.027, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.019},
    {'ID': 29, 'Nom du produit': 'EcoGuard 500', 'Densité': 1.04, 'Viscosité (mPa.s)': 67.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.014},
    {'ID': 30, 'Nom du produit': 'SmartSeal', 'Densité': 1.25, 'Viscosité (mPa.s)': 40.3, 'Ratio': 0, 'Tension superficielle (N/m)': 0.028, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.017},
    {'ID': 31, 'Nom du produit': 'PackGuard X', 'Densité': 0.89, 'Viscosité (mPa.s)': 102.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.032, 'Teneur en particules (ratio)': 0.014, 'Teneur en gaz (ratio)': 0.012},
    {'ID': 32, 'Nom du produit': 'UltraSecure', 'Densité': 1.31, 'Viscosité (mPa.s)': 75.8, 'Ratio': 0, 'Tension superficielle (N/m)': 0.029, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.020},
    {'ID': 33, 'Nom du produit': 'EcoFlex Shield', 'Densité': 1.10, 'Viscosité (mPa.s)': 95.3, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.008, 'Teneur en gaz (ratio)': 0.015},
    {'ID': 34, 'Nom du produit': 'WrapSafe', 'Densité': 0.99, 'Viscosité (mPa.s)': 107.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.014},
    {'ID': 35, 'Nom du produit': 'GreenShield Max', 'Densité': 1.07, 'Viscosité (mPa.s)': 29.5, 'Ratio': 0, 'Tension superficielle (N/m)': 0.034, 'Teneur en particules (ratio)': 0.013, 'Teneur en gaz (ratio)': 0.013},
    {'ID': 36, 'Nom du produit': 'EcoMaster', 'Densité': 1.18, 'Viscosité (mPa.s)': 122.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.027, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 37, 'Nom du produit': 'UltraFlex', 'Densité': 1.24, 'Viscosité (mPa.s)': 49.7, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.016},
    {'ID': 38, 'Nom du produit': 'QuickShield', 'Densité': 1.11, 'Viscosité (mPa.s)': 66.2, 'Ratio': 0, 'Tension superficielle (N/m)': 0.033, 'Teneur en particules (ratio)': 0.008, 'Teneur en gaz (ratio)': 0.015},
    {'ID': 39, 'Nom du produit': 'EcoSeal Pro', 'Densité': 1.30, 'Viscosité (mPa.s)': 93.8, 'Ratio': 0, 'Tension superficielle (N/m)': 0.029, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.017},
    {'ID': 40, 'Nom du produit': 'SecureMax', 'Densité': 1.34, 'Viscosité (mPa.s)': 37.6, 'Ratio': 0, 'Tension superficielle (N/m)': 0.032, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.013},
    {'ID': 41, 'Nom du produit': 'GreenWrap Pro', 'Densité': 1.02, 'Viscosité (mPa.s)': 51.8, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.013, 'Teneur en gaz (ratio)': 0.011},
    {'ID': 42, 'Nom du produit': 'UltraWrap X', 'Densité': 1.19, 'Viscosité (mPa.s)': 83.6, 'Ratio': 0, 'Tension superficielle (N/m)': 0.028, 'Teneur en particules (ratio)': 0.009, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 43, 'Nom du produit': 'ShieldMaster', 'Densité': 1.09, 'Viscosité (mPa.s)': 88.7, 'Ratio': 0, 'Tension superficielle (N/m)': 0.027, 'Teneur en particules (ratio)': 0.011, 'Teneur en gaz (ratio)': 0.015},
    {'ID': 44, 'Nom du produit': 'EcoSeal X', 'Densité': 1.27, 'Viscosité (mPa.s)': 65.4, 'Ratio': 0, 'Tension superficielle (N/m)': 0.030, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.016},
    {'ID': 45, 'Nom du produit': 'GreenTech Wrap', 'Densité': 1.17, 'Viscosité (mPa.s)': 113.5, 'Ratio': 0, 'Tension superficielle (N/m)': 0.031, 'Teneur en particules (ratio)': 0.009, 'Teneur en gaz (ratio)': 0.020},
    {'ID': 46, 'Nom du produit': 'PackLite', 'Densité': 0.88, 'Viscosité (mPa.s)': 77.2, 'Ratio': 0, 'Tension superficielle (N/m)': 0.032, 'Teneur en particules (ratio)': 0.014, 'Teneur en gaz (ratio)': 0.013},
    {'ID': 47, 'Nom du produit': 'EcoFlex One', 'Densité': 0.97, 'Viscosité (mPa.s)': 94.5, 'Ratio': 0, 'Tension superficielle (N/m)': 0.029, 'Teneur en particules (ratio)': 0.013, 'Teneur en gaz (ratio)': 0.017},
    {'ID': 48, 'Nom du produit': 'MaxiWrap', 'Densité': 1.22, 'Viscosité (mPa.s)': 57.3, 'Ratio': 0, 'Tension superficielle (N/m)': 0.028, 'Teneur en particules (ratio)': 0.010, 'Teneur en gaz (ratio)': 0.018},
    {'ID': 49, 'Nom du produit': 'QuickPack One', 'Densité': 1.05, 'Viscosité (mPa.s)': 48.9, 'Ratio': 0, 'Tension superficielle (N/m)': 0.034, 'Teneur en particules (ratio)': 0.009, 'Teneur en gaz (ratio)': 0.016},
    {'ID': 50, 'Nom du produit': 'UltraTech', 'Densité': 1.15, 'Viscosité (mPa.s)': 85.9, 'Ratio': 0, 'Tension superficielle (N/m)': 0.027, 'Teneur en particules (ratio)': 0.012, 'Teneur en gaz (ratio)': 0.017}
]

# importation des données produits
df_products = pd.read_csv('data_csv/products_list_gpt.csv')



# Nb de conditionnement généré
nb_condi_gen = 3000

container_sizes = [500, 1000, 3000, 5000]  # en litres
nominal_cadences = {500: 60, 1000: 70, 3000: 35, 5000: 30}  # cadences nominales en bidons par minute
quantities_to_produce = {product: random.randint(3000, 15000) for product in range(nb_condi_gen)}  # en litres
changeover_time = {"products" : 60, "container_size" : 25, "products&container_size" : 65, "Neant" : 0 } 
steps = [0, 1, 2, 3, 4]
steps_name = {0 : 'run', 1 : 'Neant', 2 : 'products', 3: 'container_size', 4: 'products&container_size'}
# Horaires de production
# Lundi 5h
# Vendredi 21h

# Date de début de génération 
start_date = datetime(2022, 1, 1)



def generate_production_labels_csv(num_entries: int = 100,file_path: str = "data_csv/production_labels.csv"):
    """
    Génère un fichier CSV contenant des libellés de production associés à un ID.

    Parameters:
    - file_path (str): Chemin où sauvegarder le fichier CSV.
    - num_entries (int): Nombre d'entrées à générer (par défaut 100).
    
    Returns:
    - str: Chemin du fichier CSV généré.
    """
    # Créer des ID de production
    production_ids = range(1, num_entries + 1)

    # Créer des libellés de production associés
    production_labels = [f"Prod n{i}" for i in production_ids]

    # Créer une DataFrame avec les IDs et les libellés correspondants
    production_df = pd.DataFrame({
        "production_id": production_ids,
        "libellé_production": production_labels
    })

    # Exporter la DataFrame en CSV
    production_df.to_csv(file_path, index=False)
    
    return file_path




# Étape 1 : Générer le fichier de base de données horaire
def generate_production_data():
    data = []
    id_production = 0
    
    while id_production < nb_condi_gen:
        
        product = random.choice(products)
        container_size = random.choice(container_sizes)
        nominal_cadence = nominal_cadences[container_size]
        actual_cadence = nominal_cadence * random.uniform(0.93, 0.98) * df_products[df_products['ID']==product]['Ratio']
        quantity_to_produce = quantities_to_produce[product]
        total_containers = int(quantity_to_produce / (container_size/1000))
        changeover_time = 0.0

        data.append({
            'id_production': id_production,
            'id_product': product,
            'Container_Size_L': container_size,
            'Nominal_Cadence_per_min': nominal_cadence,
            'Actual_Cadence_per_min': actual_cadence,
            'Quantity_to_Produce_L': quantity_to_produce,
            'Total_Containers': total_containers,
            'Changeover_Time_min': changeover_time,
            'changeover_type' : ''
        })
        id_production += 1 

        
    return pd.DataFrame(data)



#étape 2 : Modifié les changeover_time en fonction des datas généré
def modify_changeover_time(production_data):

    for i in range(len(production_data) - 1):
        # Current and next row details
        current_product = production_data.loc[i, "id_product"]
        next_product = production_data.loc[i + 1, "id_product"]
        current_container_size = production_data.loc[i, "Container_Size_L"]
        next_container_size = production_data.loc[i + 1, "Container_Size_L"]
        
        # Apply conditions
        if current_product == next_product and current_container_size == next_container_size:
            production_data.at[i + 1, "Changeover_Time_min"] = changeover_time["Neant"]
            production_data.at[i + 1, "changeover_type"] = steps[1]
        elif current_product != next_product and current_container_size == next_container_size:
            production_data.at[i + 1, "Changeover_Time_min"] = changeover_time["products"] * (1 + np.random.exponential(0.15))
            production_data.at[i + 1, "changeover_type"] = steps[2]
        elif current_product == next_product and current_container_size != next_container_size:
            production_data.at[i + 1, "Changeover_Time_min"] = changeover_time["container_size"] * (1 + np.random.exponential(0.15))
            production_data.at[i + 1, "changeover_type"] = steps[3]
        else:
            production_data.at[i + 1, "Changeover_Time_min"] = changeover_time["products&container_size"] * (1 + np.random.exponential(0.15))
            production_data.at[i + 1, "changeover_type"] = steps[4]

    return production_data




# Étape 3 : Générer le fichier minute par minute avec périodes d'arrêt
def generate_minute_data(production_data):
    minute_data = []
    
    current_time = start_date
    previous_downtime = 0
    id_minute_data = 0

    for _, row in production_data.iterrows():
        #total_minutes = int(row['Total_Containers'] / row['Actual_Cadence_per_min'])
        total_minutes = int(row['Total_Containers'] / row['Actual_Cadence_per_min'].iloc[0])

        print(_)
        
        # Génération du nombre de minutes d'arrêt aléatoire -> répartit en arrêt programmé, arrêt non programmé, arrêt qualité
        #définition du nombre de minute d'arrêt programmé pour la production
        total_planned_downtime = int(total_minutes * random.uniform(0.00, 0.15))
        planned_downtime = 0

        #définition du nombre de minute d'arrêt non programmé pour la production
        total_unplanned_downtime =  int(total_minutes * random.uniform(0.00, 0.25))
        unplanned_downtime = 0

        #définition du nombre de minute d'arrêt qualité pour la production
        total_quality_downtime =  int(total_minutes * random.uniform(0.0, 0.0))
        quality_downtime = 0


        # Périodes de production et d'arrêts
        remaining_containers = row['Total_Containers']
        remaining_changeover = row['Changeover_Time_min']

        # arret de la boucle si la date de production est supérieur ou egale à date du jour
        if current_time >= datetime.now():
            break
        
        # intégration des temps de transition 
        while remaining_changeover > 0:


            # définition du ratio aléatoire pour définiton de la température
            '''
            la température en début de conditionnement est défini selon plusieurs critère:
            - saisons/mois
            - heure au moment du démarrage
            - Variabilité naturelle du jour au jour

            Ensuite au furr et à mesure du conditionnement, la température peut globalement 
            décroitre ou croitre independament d'un éventuel bruit de fond.
            '''

            temp = temp_exterieur(current_time)
            temp_prod = temperature_produit(temp)

            remaining_changeover -= 1
            minute_data.append({
                'id_minute_data' : id_minute_data,
                'Timestamp': current_time,
                'id_production': row['id_production'],
                'id_product': row['id_product'],
                'Container_Size_L': row['Container_Size_L'],
                'Containers_Produced': 0,
                'step' : row['changeover_type'], 
                'run' : 0,
                'changeover': 60,
                'closed_workshop': 0,
                'planned_downtime': planned_downtime,
                'unplanned_downtime': unplanned_downtime,
                'quality_downtime': quality_downtime,
                'cycle_time_variation': 0,
                'temperature' : temp_prod
            })

            id_minute_data += 1    
            current_time += timedelta(minutes=1)
        
        while remaining_containers > 0:
            # Production minute par minute

            if previous_downtime != 0:
                probability = 0.78
            else:
                probability = 0.07

            # vérification si en weekend ou en semaine.
            weekend = (current_time.weekday() == 4 and current_time.hour >= 21) or (current_time.weekday() > 4) or (current_time.weekday() == 0 and current_time.hour < 5)

            # reinitialisation cycle_time_variation
            cycle_time_variation = 0

            # définition du ratio de variation/bruit pour la cadence
            cadence_nominal_temp = int(nominal_cadences[row['Container_Size_L']])
            #Cadence_temp = int(row['Actual_Cadence_per_min'] * (1 + np.random.normal(0.08, 0.05)))
            Cadence_temp = int(row['Actual_Cadence_per_min'].iloc[0] * (1 + np.random.normal(0.08, 0.05)))


            # définition du ratio aléatoire pour définiton de la température
            '''
            la température en début de conditionnement est défini selon plusieurs critère:
            - saisons/mois
            - heure au moment du démarrage
            - Variabilité naturelle du jour au jour

            Ensuite au furr et à mesure du conditionnement, la température peut globalement 
            décroitre ou croitre independament d'un éventuel bruit de fond.
            '''

            temp_ext = temp_exterieur(current_time)
            temp_prod = temperature_produit(temp_ext)
            ratio_temp = lambda x : round(0.01 * x + 0.8, 2) if x < 20 else round(-0.01 * x + 1.2, 2)

            if  Cadence_temp > cadence_nominal_temp:
                Cadence = int(cadence_nominal_temp * ratio_temp(temp_prod))
            else :
                Cadence = int(Cadence_temp * ratio_temp(temp_prod))


            if weekend == True:
                containers_per_minute = 0
                total_planned_downtime -= 0
                total_unplanned_downtime -= 0
                total_quality_downtime -= 0
                planned_downtime = 0
                unplanned_downtime = 0
                quality_downtime = 0
                previous_downtime = 0
                run = 0
                closed_workshop = 60

            elif random.uniform(0, 1) < probability : #condition ok si < à 10% probabilité alors temps d'arret
                if previous_downtime == 0:
                    downtime_type_choice = random.choice([1, 2, 3]) # choix du type d'arret
                else:
                    downtime_type_choice = previous_downtime

                if downtime_type_choice == 1 and total_planned_downtime > 0 :
                    containers_per_minute = 0
                    total_planned_downtime -= 1
                    total_unplanned_downtime -= 0
                    total_quality_downtime -= 0
                    planned_downtime = 60
                    unplanned_downtime = 0
                    quality_downtime = 0
                    previous_downtime = 1
                    run = 0
                    closed_workshop = 0
                
                elif downtime_type_choice == 2 and total_unplanned_downtime > 0 :
                    containers_per_minute = 0
                    total_planned_downtime -= 0
                    total_unplanned_downtime -= 1
                    total_quality_downtime -= 0
                    planned_downtime = 0
                    unplanned_downtime = 60
                    quality_downtime = 0
                    previous_downtime = 2
                    run = 0
                    closed_workshop = 0
                
                elif downtime_type_choice == 3 and total_quality_downtime > 0:
                    containers_per_minute = 0
                    total_planned_downtime -= 0
                    total_unplanned_downtime -= 0
                    total_quality_downtime -= 1
                    planned_downtime = 0
                    unplanned_downtime = 0
                    quality_downtime = 60
                    previous_downtime = 3
                    run = 0
                    closed_workshop = 0

                else:
                    containers_per_minute = Cadence
                    total_planned_downtime -= 0
                    total_unplanned_downtime -= 0
                    total_quality_downtime -= 0
                    planned_downtime = 0
                    unplanned_downtime = 0
                    quality_downtime = 0
                    previous_downtime = 0
                    run = 60
                    closed_workshop = 0

                    # calcul de l'ecart de cadence
                    cycle_time_variation = int(((nominal_cadences[row['Container_Size_L']] - Cadence) /  nominal_cadences[row['Container_Size_L']])*60)


            else : 
                containers_per_minute = Cadence
                total_planned_downtime -= 0
                total_unplanned_downtime -= 0
                total_quality_downtime -= 0
                planned_downtime = 0
                unplanned_downtime = 0
                quality_downtime = 0
                previous_downtime = 0
                run = 60
                closed_workshop = 0

                # calcul de l'ecart de cadence
                cycle_time_variation = int(((nominal_cadences[row['Container_Size_L']] - Cadence) /  (nominal_cadences[row['Container_Size_L']])) * 60 )

                

            remaining_containers -= containers_per_minute
            minute_data.append({
                'id_minute_data': id_minute_data,
                'Timestamp': current_time,
                'id_production': row['id_production'],
                'id_product': row['id_product'],
                'Container_Size_L': row['Container_Size_L'],
                'Containers_Produced': containers_per_minute ,
                'step' : steps[0],
                'run': run,
                'changeover': 0,
                'closed_workshop': closed_workshop,
                'planned_downtime': planned_downtime,
                'unplanned_downtime': unplanned_downtime,
                'quality_downtime': quality_downtime,
                'cycle_time_variation': cycle_time_variation,
                'temperature' : temp_prod
            })
                
            current_time += timedelta(minutes=1)

            id_minute_data += 1


    return pd.DataFrame(minute_data)




# Générer les données finales
#génération du fichier labels pour les production
generate_production_labels_csv(nb_condi_gen)

#génération du fichier production
production_data = generate_production_data()

production_data_modified = modify_changeover_time(production_data)

minute_data = generate_minute_data(production_data_modified)



# Sauvegarder le fichier final en CSV
output_path = r'data_csv\production_data.csv'
minute_data.to_csv(output_path, index=False)

print(f"Fichier 'production_data.csv' généré avec succès dans le répertoire actuel.")
