import requests

def match_history(puuid, key):
    url = "https://asia.api.riotgames.com//lol/match/v5/matches/by-puuid/" + puuid + "/ids?queue=420&start=0&count=100&api_key=" + key

    result = requests.get(url)

    return result.json()