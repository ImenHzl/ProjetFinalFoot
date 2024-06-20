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
                with open("data/dataTeams.json", "w") as jsonFile:
                    json.dump(infoplay, jsonFile, indent=4) 

# cette fonction permet de récuperer les infos des joeurs d'un team
def infoPlayersTeams(met,teamId,apiKey):
    url=f"https://apiv2.allsportsapi.com/football/?met={met}&APIkey={apiKey}&teamId={teamId}"
    response=requests.get(url)
    try:
        if response.status_code==200:
            print("La requête est réussi (OK 200)") 
            data=response.json()
            teamName=[]
            team={
                "teamId":teamId
            }
            teamName.append(team)
            jsonString = json.dumps(teamName)
            enregistrerJson(teamName)
            team=data['result'][0]
            players=team['players']
            all_players_info = []
            for elt in players:
                player_id=elt.get('player_key', 'N/A')
                player_name = elt.get('player_name', 'N/A')
                player_numero = elt.get('player_number', 'N/A')
                player_type = elt.get('player_type', 'N/A')
                infoplay={
                    "id joueur":player_id,
                    "nom du joueur": player_name,
                    "numero du joeur":player_numero,
                    "type du joueur":player_type
                }
                all_players_info.append(infoplay)
                jsonString = json.dumps(all_players_info)
                # Affichez la chaîne JSON
                print(jsonString)
                enregistrerJson(all_players_info)
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)

    return all_players_info

"""metV1="Teams"
teamId="100"
reponse= infoPlayersTeams(metV1, teamId)
print(reponse)"""