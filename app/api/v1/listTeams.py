import requests
import json
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")


def enregistrerJson(data):
    with open('data/dataListTeams.json', 'w') as f:
        json.dump(data, f, indent=4)


def listTeamsLeague(met, leagueId, apiKey):
    url = f"https://apiv2.allsportsapi.com/football/?&met={met}&leagueId={leagueId}&APIkey={apiKey}"
    response = requests.get(url)
    dataLeague = []
    try:
        if response.status_code == 200:
            print("La requête est réussie (OK 200)")
            data = response.json()
            team = data.get('result', [])
            all_team_info = []
            for elt in team:
                team_key = elt.get('team_key', 'N/A')
                team_logo = elt.get('team_logo', 'N/A')
                team_name = elt.get('team_name', 'N/A')
                infoplay = {
                    "team_key": team_key,
                    "team_logo": team_logo,
                    "team_name": team_name
                }
                all_team_info.append(infoplay)
            enregistrerJson(all_team_info)
            dataLeague = all_team_info
        else:
            print(f"Erreur {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
    return dataLeague


met = "Teams"
leagueId = "3"
resultat = listTeamsLeague(met, leagueId, apiKey)
print(resultat)
