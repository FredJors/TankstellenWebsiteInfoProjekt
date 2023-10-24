from datetime import datetime

import pandas as pd
import mysql.connector
from matplotlib import pyplot as plt


def get_fuel_data(start_date, end_date=None):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Hannes1802!",
        database="sql_fuelHelper"
    )
    cursor = db.cursor()

    if end_date is None:
        end_date = datetime.now()

    query = "SELECT * FROM fuel_data WHERE timestamp BETWEEN %s AND %s ORDER BY timestamp ASC"
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()

    data = []
    for row in results:
        data.append({
            "timestamp": row[1],
            "station_id": row[2],
            "diesel": row[3],
            "e10": row[4],
            "e5": row[5]
        })

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")

    cursor.close()
    db.close()

    return df


# Plot für die letzten 24 Stunden
start_date = pd.Timestamp.now() - pd.Timedelta(hours=24)
df = get_fuel_data(start_date)

fig, ax = plt.subplots()
ax.plot(df["diesel"], label="Diesel")
ax.plot(df["e10"], label="E10")
ax.plot(df["e5"], label="E5")
ax.set_xlabel("Zeit")
ax.set_ylabel("Preis")
ax.set_title("Preise für Diesel, E10 und E5 in den letzten 24 Stunden")
ax.legend()

plt.show()

# Plot für die letzte Woche
start_date = pd.Timestamp.now() - pd.Timedelta(days=7)
df = get_fuel_data(start_date)

fig, ax = plt.subplots()
ax.plot(df["diesel"], label="Diesel")
ax.plot(df["e10"], label="E10")
ax.plot(df["e5"], label="E5")
ax.set_xlabel("Zeit")
ax.set_ylabel("Preis")
ax.set_title("Preise für Diesel, E10 und E5 in der letzten Woche")
ax.legend()

plt.show()

# Plot für den letzten Monat
start_date = pd.Timestamp.now() - pd.Timedelta(days=30)
df = get_fuel_data(start_date)

fig, ax = plt.subplots()
ax.plot(df["diesel"], label="Diesel")
ax.plot(df["e10"], label="E10")
ax.plot(df["e5"], label="E5")
ax.set_xlabel("Zeit")
ax.set_ylabel("Preis")
ax.set_title("Preise für Diesel, E10 und E5 im letzten Monat")
ax.legend()

plt.show()
