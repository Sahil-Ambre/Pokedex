import requests
import sqlite3
import pandas as pd

engine = sqlite3.connect("pokedex.db")
cursor = engine.cursor()

names = []
types = []

for i in range(1,100):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}/").json()
    names.append(data["name"])
    types.append(data["types"][0]["type"]["name"])


df = pd.DataFrame({"name": names, "type": types})

df.to_sql("pokeinfo", engine, if_exists="replace", index=False)


