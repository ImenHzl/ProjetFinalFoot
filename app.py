from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/league')
def league():
    try:
        response = requests.get('http://127.0.0.1:8000/league')
        response.raise_for_status()
        dataListLeague = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données depuis FastAPI: {e}")
        dataListLeague = []
    return render_template('league.html', leagues=dataListLeague)

@app.route('/league/<int:league_id>')
def team(league_id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/league/{league_id}')
        response.raise_for_status()
        dataListteam = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données depuis FastAPI: {e}")
        dataListteam = []
    return render_template('listTeam.html', teams=dataListteam)

@app.route('/Teams/<int:idTeam>')
def team_details(idTeam):
    try:
        response = requests.get(f'http://127.0.0.1:8000/Teams/{idTeam}')
        response.raise_for_status()
        datateam = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données depuis FastAPI: {e}")
        datateam = []
    return render_template('listJoueur.html', joueurs=datateam)

if __name__ == '__main__':
    app.run(debug=True)
