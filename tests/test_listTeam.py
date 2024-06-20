import pytest
import requests_mock
import json
from dotenv import load_dotenv
import os
from app.api.v1.listTeams import listTeamsLeague

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")

def test_listTeams_success(requests_mock):
    met = "Teams"
    leagueId = "3"
    api_response = {
        "result": [
            {"team_key": 1, "team_logo": "logo.jpg", "standing_team": "N/A"},
            {"team_key": 2, "team_logo": "logo.jpg", "standing_team": "N/A"},
            {"team_key": 3, "team_logo": "logo.jpg", "standing_team": "N/A"}
        ]
    }

    requests_mock.get(f"https://apiv2.allsportsapi.com/football/?&met={met}&leagueId={leagueId}&APIkey={apiKey}", json=api_response, status_code=200)

    result = listTeamsLeague(met, leagueId, apiKey)
    
    expected_result = [
        {"team_key": 1, "team_logo": "logo.jpg", "standing_team": "N/A"},
        {"team_key": 2, "team_logo": "logo.jpg", "standing_team": "N/A"},
        {"team_key": 3, "team_logo": "logo.jpg", "standing_team": "N/A"}
    ]

    print("Résultat réel:", result)
    print("Résultat attendu:", expected_result)
    
    assert result == expected_result

def test_listTeams_no_results(requests_mock):
    met = "Teams"
    leagueId = "100"
    api_response = {"result": []}

    requests_mock.get(f"https://apiv2.allsportsapi.com/football/?&met={met}&leagueId={leagueId}&APIkey={apiKey}", json=api_response, status_code=200)

    result = listTeamsLeague(met, leagueId, apiKey)
    
    expected_result = []
    
    assert result == expected_result
