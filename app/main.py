from fastapi import FastAPI,HTTPException
import json
from api.v1.listTeams import listTeamsLeague
from api.v1.listJoeur import infoPlayersTeams
from api.v1.infoJoeur import infoPlayers
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")

app= FastAPI()

# Charger les données JSON depuis le fichier
with open("data/dataListLeague.json", "r") as file:
    dataListLeague = json.load(file)

@app.get("/league")
def read_listLeague():
    return dataListLeague

@app.get("/league/{idLeague}")
def read_listTeams(idLeague: int):
    try:
        resultat = listTeamsLeague("Teams", idLeague,apiKey)
        return resultat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/Teams/{idTeam}")
def read_listJoeurs(idTeam: int):
    try:
        resultat = infoPlayersTeams("Teams", idTeam,apiKey)
        return resultat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/Joueur/{idJoueur}")
def read_infoJoueur(idJoueur:int):
    try:
        resultat = infoPlayers("Players", idJoueur,apiKey)
        return resultat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    



