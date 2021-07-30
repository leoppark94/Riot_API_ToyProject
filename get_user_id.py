import requests

def get_user_id(summoner_name, key):
    url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + key
    
    result = requests.get(url)
    
    print("결과")
    print(result.json())
    
    encrypted_id = result.json()['id']
    
    puuid = result.json()['puuid']

    return encrypted_id, puuid


