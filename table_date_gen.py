import pandas as pd

# Définition des dates de début et de fin
start_date = "2022-01-01 00:00:00"
end_date = "2024-12-31 23:59:00"

# Générer la table de dates avec un intervalle de 1 minute
date_range = pd.date_range(start=start_date, end=end_date, freq="T")

# Création de la DataFrame avec les différentes colonnes de date et heure
date_df = pd.DataFrame({
    "timestamps": date_range,
    "année": date_range.year,
    "mois": date_range.month,
    "jour": date_range.day,
    "jour_de_la_semaine": date_range.dayofweek,
    "semaine": date_range.isocalendar().week,
    "heure": date_range.hour,
    "minute": date_range.minute
})

# Exporter la DataFrame en CSV
csv_path = "data_csv/table_date.csv"
date_df.to_csv(csv_path, index=False)


