import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Paramètres globaux
products = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
physico_chemy = [
    {'ID': 1, 'Nom du produit': 'PackEasy 500', 'Densité': 0.85, 'Viscosité (mPa.s)': 138.7, 'Ratio': 0.88},
    {'ID': 2, 'Nom du produit': 'EcoWrap Plus', 'Densité': 0.95, 'Viscosité (mPa.s)': 64.06, 'Ratio': 0.80},
    {'ID': 3, 'Nom du produit': 'FlexiSeal Pro', 'Densité': 1.15, 'Viscosité (mPa.s)': 10.77, 'Ratio': 0.72},
    {'ID': 4, 'Nom du produit': 'UltraShield', 'Densité': 1.28, 'Viscosité (mPa.s)': 111.47, 'Ratio': 0.92},
    {'ID': 5, 'Nom du produit': 'WrapTech 3000', 'Densité': 0.94, 'Viscosité (mPa.s)': 140.19, 'Ratio': 0.91},
    {'ID': 6, 'Nom du produit': 'QuickPack Max', 'Densité': 1.36, 'Viscosité (mPa.s)': 41.46, 'Ratio': 0.79},
    {'ID': 7, 'Nom du produit': 'BioGuard X', 'Densité': 0.86, 'Viscosité (mPa.s)': 62.86, 'Ratio': 0.78},
    {'ID': 8, 'Nom du produit': 'SmartWrap', 'Densité': 0.86, 'Viscosité (mPa.s)': 77.4, 'Ratio': 0.80},
    {'ID': 9, 'Nom du produit': 'ProFlex Lite', 'Densité': 0.92, 'Viscosité (mPa.s)': 76.96, 'Ratio': 0.81},
    {'ID': 10, 'Nom du produit': 'EcoPack Pro', 'Densité': 1.0, 'Viscosité (mPa.s)': 57.1, 'Ratio': 0.79},
    {'ID': 11, 'Nom du produit': 'SafeWrap Elite', 'Densité': 1.29, 'Viscosité (mPa.s)': 13.73, 'Ratio': 0.73},
    {'ID': 12, 'Nom du produit': 'MaxiGuard', 'Densité': 0.97, 'Viscosité (mPa.s)': 102.96, 'Ratio': 0.86},
    {'ID': 13, 'Nom du produit': 'SpeedSeal', 'Densité': 1.2, 'Viscosité (mPa.s)': 7.17, 'Ratio': 0.71},
    {'ID': 14, 'Nom du produit': 'EcoFlex 800', 'Densité': 0.9, 'Viscosité (mPa.s)': 103.46, 'Ratio': 0.85},
    {'ID': 15, 'Nom du produit': 'UltraPack One', 'Densité': 1.14, 'Viscosité (mPa.s)': 82.92, 'Ratio': 0.85},
    {'ID': 16, 'Nom du produit': 'SecureWrap X', 'Densité': 1.32, 'Viscosité (mPa.s)': 83.55, 'Ratio': 0.87},
    {'ID': 17, 'Nom du produit': 'GreenWrap', 'Densité': 1.09, 'Viscosité (mPa.s)': 19.91, 'Ratio': 0.73},
    {'ID': 18, 'Nom du produit': 'FlexiPack Pro', 'Densité': 0.9, 'Viscosité (mPa.s)': 54.75, 'Ratio': 0.78},
    {'ID': 19, 'Nom du produit': 'EcoLock', 'Densité': 1.37, 'Viscosité (mPa.s)': 58.71, 'Ratio': 0.83},
    {'ID': 20, 'Nom du produit': 'PackMaster 360', 'Densité': 1.32, 'Viscosité (mPa.s)': 49.95, 'Ratio': 0.80}
]

container_sizes = [500, 1000, 3000, 5000]  # en litres
nominal_cadences = {500: 60, 1000: 70, 3000: 35, 5000: 30}  # cadences nominales en bidons par minute
quantities_to_produce = {product: random.randint(3000, 25000) for product in products}  # en litres
changeover_time = {"products" : 60, "container_size" : 25, "products&container_size" : 65, "Neant" : 0 } 
steps = [0, 1, 2, 3, 4]
steps_name = {0 : 'run', 1 : 'Neant', 2 : 'products', 3: 'container_size', 4: 'products&container_size'}
# Horaires de production
# Lundi 5h
# Vendredi 21h

# Date de début de génération 
start_date = datetime(2022, 1, 1)

# Nb de conditionnement généré
nb_condi_gen = 1953

# Étape 1 : Générer le fichier de base de données horaire
def generate_production_data():
    data = []
    id_production = 0
    
    while id_production < nb_condi_gen:
        
        product = random.choice(products)
        container_size = random.choice(container_sizes)
        nominal_cadence = nominal_cadences[container_size]
        actual_cadence = nominal_cadence * random.uniform(0.75, 0.85) * physico_chemy[product]['Ratio']
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
        id_production += 1 #timedelta(hours=1)
        
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
        total_minutes = int(row['Total_Containers'] / row['Actual_Cadence_per_min'])
        
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
        
        # intégration des temps de transition 
        while remaining_changeover > 0:

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
                'cycle_time_variation': 0
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
            Cadence_temp = int(row['Actual_Cadence_per_min'] * (1 + np.random.normal(0.08, 0.05)))

            # définition du ratio aléatoire pour définiton de la température
            '''
            la température en début de conditionnement est défini selon plusieurs critère:
            - saisons/mois
            - heure au moment du démarrage
            - Variabilité naturelle du jour au jour

            Ensuite au furr et à mesure du conditionnement, la température peut globalement 
            décroitre ou croitre independament d'un éventuel bruit de fond.
            '''

            if  Cadence_temp > cadence_nominal_temp:
                Cadence = cadence_nominal_temp
            else :
                Cadence = Cadence_temp


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
                    cycle_time_variation = int(((int(nominal_cadences[row['Container_Size_L']]) - int(Cadence)) /  int(nominal_cadences[row['Container_Size_L']]))*60)


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
                cycle_time_variation = int(((int(nominal_cadences[row['Container_Size_L']]) - int(Cadence)) /  int(nominal_cadences[row['Container_Size_L']]))*60)

                

            remaining_containers -= containers_per_minute
            minute_data.append({
                'id_minute_data': id_minute_data,
                'Timestamp': current_time,
                'id_production': row['id_production'],
                'id_product': row['id_product'],
                'Container_Size_L': row['Container_Size_L'],
                'Containers_Produced': containers_per_minute,
                'step' : steps[0],
                'run': run,
                'changeover': 0,
                'closed_workshop': closed_workshop,
                'planned_downtime': planned_downtime,
                'unplanned_downtime': unplanned_downtime,
                'quality_downtime': quality_downtime,
                'cycle_time_variation': cycle_time_variation
            })
                
            current_time += timedelta(minutes=1)

            id_minute_data += 1


    return pd.DataFrame(minute_data)




# Générer les données finales
production_data = generate_production_data()

production_data_modified = modify_changeover_time(production_data)

minute_data = generate_minute_data(production_data_modified)



# Sauvegarder le fichier final en CSV
output_path = r'C:\Users\dimle\OneDrive\Bureau\production_data.csv'
minute_data.to_csv(output_path, index=False)

print(f"Fichier 'production_data.csv' généré avec succès dans le répertoire actuel.")
