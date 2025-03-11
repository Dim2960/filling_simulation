import pandas as pd
from simulation_function import ratio_cadence


products_info = [
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

df_products = pd.DataFrame(products_info)


# Modification de l'ordre des colonnes du df
nouvel_ordre_cols = ['ID', 'Nom du produit', 'Densité', 'Viscosité (mPa.s)', 'Tension superficielle (N/m)', 'Teneur en particules (ratio)', 'Teneur en gaz (ratio)', 'Ratio']
df_products = df_products[nouvel_ordre_cols]


# Clalcul du ratio et intégration au df
df_products["Ratio"] = df_products.apply(
    lambda row: ratio_cadence(
        densite=row["Densité"],  # Notez la majuscule car c'est la colonne du DataFrame
        viscosite=row["Viscosité (mPa.s)"],  # Valeur constante
        teneur_particule=row["Tension superficielle (N/m)"],  # Valeur constante
        tension_surface=row["Teneur en particules (ratio)"],  # Valeur constante
        teneur_gaz=row["Teneur en gaz (ratio)"]  # Valeur constante
    ), 
    axis=1
)


# création du fichier csv pour les données gpt
product_list_gpt = "data/processed/products_list_gpt.csv"
df_products.to_csv(product_list_gpt, index=False)

print(df_products)
