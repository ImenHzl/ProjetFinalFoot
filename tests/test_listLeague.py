import pytest
import requests
import requests_mock
import json
from app.api.v1.listLeague import listLeague
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")

def test_listLeague_success(requests_mock):
    met = "Leagues"
    api_response = {
        "result": [
            {"league_key": "1", "league_name": "League 1", "league_logo": "logo1.png"},
            {"league_key": "2", "league_name": "League 2", "league_logo": "logo2.png"},
            {"league_key": "3", "league_name": "League 3", "league_logo": "logo3.png"}
        ]
    }

    requests_mock.get(f"https://apiv2.allsportsapi.com/football/?&met={met}&APIkey={apiKey}", json=api_response, status_code=200)

    result = listLeague(met)
    
    expected_result = [
        {"league_key": "1", "league_name": "League 1", "logo_league": "logo1.png"},
        {"league_key": "2", "league_name": "League 2", "logo_league": "logo2.png"},
        {"league_key": "3", "league_name": "League 3", "logo_league": "logo3.png"}
    ]
    
    assert result == expected_result

def test_listLeague_no_results(requests_mock):
    met = "Leagues"
    api_response = {"result": []}

    requests_mock.get(f"https://apiv2.allsportsapi.com/football/?&met={met}&APIkey={apiKey}", json=api_response, status_code=200)

    result = listLeague(met)
    
    expected_result = []
    
    assert result == expected_result



