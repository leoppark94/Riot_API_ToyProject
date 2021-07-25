import pandas as pd

pd_champion_data = pd.read_json('champion.json')

def champion_name(key_value):
    key = []
    name = []
    for i in pd_champion_data['data']:
        key.append(i['key'])
        name.append(i['id'])

    dic = {'key': key, 'name': name}

    test = pd.DataFrame(dic)

    df_champion_list = test.set_index('key')

    champion_name = df_champion_list[str(key_value):str(key_value)]


    return champion_name
