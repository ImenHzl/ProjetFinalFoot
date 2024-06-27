import requests
import json
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")


# cette fonction permet d'enregistrer les donnees dans un fichier json
def enregistrerJson(infoplay):
    # Enregistrez la chaîne JSON dans un fichier
    with open("data/dataJoueur.json", "w") as jsonFile:
        json.dump(infoplay, jsonFile, indent=4)


"""cette fonction permet de récuperer les infos des joeurs d'un team
    elle prend comme parametres
        params:
            met: pour préciser qu'on cherche de info de joueur
            playerid: id de joueur
        return:
            un fichier json qui contient les infos de joueur
"""


def infoPlayers(met, playerid):
    url = f"https://apiv2.allsportsapi.com/football/?&met={met}&playerId={playerid}&APIkey={apiKey}"
    response = requests.get(url)
    try:
        if response.status_code == 200:
            print("La requête est réussi (OK 200)")
            data = response.json()
            team = data['result'][0]
            player_info = []
            player_name = team.get('player_name', 'N/A')
            player_numero = team.get('player_number', 'N/A')
            player_type = team.get('player_type', 'N/A')
            player_count = team.get('player_country', 'N/A')
            infoplay = {
                    "nom du joueur": player_name,
                    "numero du joeur": player_numero,
                    "type du joueur": player_type,
                    "pays du joueur": player_count
                }
            player_info.append(infoplay)
            jsonString = json.dumps(infoplay)
            # Affichez la chaîne JSON
            print(jsonString)
            enregistrerJson(player_info)
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
    return player_info


"""metV1="Players"
teamId="26180013"
reponse= infoPlayers(metV1, teamId)
print(reponse)"""
