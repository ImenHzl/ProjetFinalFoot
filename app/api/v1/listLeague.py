import requests
import json
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")


# cette fonction permet d'enregistrer les données dans un fichier json
def enregistrerJson(infoplay):
    # Enregistrez la chaîne JSON dans un fichier
    with open("data/dataListLeague.json", "w") as jsonFile:
        json.dump(infoplay, jsonFile, indent=4)


"""
cette fonction permet de récupérer la liste de Teams pour une league
elle prend 2 paramètres
        params:
            met: pour spécifier la section qu'on veut récupérer
        return:
            un fichier json qui contient toutes les infos d'une league
"""


def listLeague(met):
    url = f"https://apiv2.allsportsapi.com/football/?&met={met}&APIkey={apiKey}"
    response = requests.get(url)
    dataLeague = []  # Initialiser à une liste vide par défaut
    try:
        if response.status_code == 200:
            print("La requête est réussie (OK 200)")
            data = response.json()
            if 'result' in data and isinstance(data['result'], list):
                all_team_info = []
                for index, team in enumerate(data['result']):
                    if index >= 10:  # Limiter à 10 résultats
                        break
                    league_key = team.get('league_key', 'N/A')
                    league_name = team.get('league_name', 'N/A')
                    league_pays = team.get('country_name', 'N/A')
                    infoplay = {
                        "league_key": league_key,
                        "league_name": league_name,
                        "pays_league": league_pays
                    }
                    all_team_info.append(infoplay)
                enregistrerJson(all_team_info)  # Enregistrer les données dans un fichier JSON
                dataLeague = all_team_info  # Assigner les données à retourner
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
    return dataLeague  # Retourner les données


"""met = "Leagues"
result = listLeague(met)
print(result)"""
