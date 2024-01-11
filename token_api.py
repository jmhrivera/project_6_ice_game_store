'''You will find here the tokens to access to the IGDB database
and the function to get game names and platform names
'''
# File: token_api.py
# Author: Manuel Hernandez
# Date: January 9, 2024
# Description: This module contains functions for API igdb.

import requests
import functions
import pandas as pd

# Token Access
keys = {
    "client_id": "mnshverfmemhyvk4evrlm8m1mu04ay",
    "client_secret": "zwz9c3ols1hi4eevaz4xsv181jt4pa",
    "grant_type": "client_credentials"
}

TOKEN_URL = "https://id.twitch.tv/oauth2/token"
token_response = requests.post(TOKEN_URL, data=keys, timeout=10)
token_data = token_response.json()
access_token = token_data["access_token"]


def game_request(game_name, platform, client_id=keys["client_id"], token=access_token):
    '''
    This function will take two filters to look into igdb database,
    returning the game, platform and release date
    '''
    games_url = "https://api.igdb.com/v4/games/"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {token}",
    }
    # body = f'fields name, platforms.name, release_dates.human; where name = "{
    #     game_name}" & platforms.name = "{platform}" ;'

    body = f'fields name, platforms.name, release_dates.human ; search "{
        game_name}"; where platforms.name = "{platform}";'

    game_response = requests.post(
        games_url, headers=headers, data=body, timeout=10)

    if game_response.json() == []:
        print(f'El juego "{game_name}" no fue encontrado')
        route = "./datasets/games_not_found.csv"
        df = pd.DataFrame([[game_name, platform]],
                          columns=["game name", "platform"])
        functions.export_to_csv(route, df, "a")
        return "no game data"
    return game_response.json()


def platform_request(client_id=keys["client_id"], token=access_token):
    '''
    This function will take two filters to look into igdb database, 
    returning the platforms and platform names
    '''
    games_url = "https://api.igdb.com/v4/platforms"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {token}",
    }
    body = 'fields name;limit 500;'
    p_response = requests.post(
        games_url, headers=headers, data=body, timeout=10)
    return p_response.json()


# platform_request()
