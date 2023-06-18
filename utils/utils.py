
import time
import os
import datetime
import pandas as pd
import requests
import json as json
from dotenv import load_dotenv 

# Data Path
DATA_PATH = r'C:/Users/liamp/OneDrive/Desktop/Liams_path_to_Data_science/Football_api_project/Output_files'

# Endpoints
API_FOOTBALL_PLAYERS_ENDPOINT = "https://api-football-v1.p.rapidapi.com/v3/players"

# Championship Codes
SPANISH_LEAGUE = "140"
SPANISH_LEAGUE_2 = "141"
PREMIER_LEAGUE = "39"
BUNDESLIGA = "78"
EREDIVISE_LEAGUE = "88"
# DENMARK_LEAGUE = "120"
TURKEY_LEAGUE = "203"
MAJOR_LEAGUE = "253"
INDIA_LEAGUE = "323"

# Set the championship
CHAMPIONSHIP = PREMIER_LEAGUE

# Season year
SEASON = "2021"


# Http Codes
TOO_MANY_REQUESTS = 429

# Initial Page
FIRST = 1

# the below was in the copied code base, I am yet to see how I need so many api_keys
# def get_api_keys_file(path):
#     with open(path) as f:
#         return json.load(f)


def get_api_key():
    """
    Function to retrieve the API key from environment variables.

    Returns:
        str: The API key as a string.
    """
    
    # keys = get_api_keys_file('/home/jordilucas/.secret/api_football.json')
    dotenv_path = os.path.join("config", "dev.env")
    load_dotenv(dotenv_path)
    api_key = os.getenv("API_KEY")
    # return keys['api_football_key']
    return api_key


def save_df_to_csv(df, data_path, championship):
    """
    Function to save a DataFrame to a CSV file in the specified data path.

    Args:
        df (DataFrame): The DataFrame to save.
        data_path (str): The path where the CSV file will be saved.
        championship (str): The name of the championship.
    """
    try:
        datetime_now = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
        file_path = os.path.join(data_path, f'df_championship_{championship}_{datetime_now}.csv')
        df.to_csv(file_path, index=False, header=True)
        return True, file_path
    except Exception as e:
        return False, str(e)

def get_total_pages():
    """
    Function to get the total number of pages to fetch data from API.

    Returns:
        int: Total number of pages to fetch.
    """
    querystring_ = {"league": CHAMPIONSHIP, "season": SEASON, "page": 30}
    json_response_stats_league = get_api_football(API_FOOTBALL_PLAYERS_ENDPOINT, querystring_, get_api_key())
    parsed_stats_league = draw_pretty_json(json_response_stats_league)

    return parsed_stats_league['paging']['total']


def get_api_response(url, querystring, key, method="GET"):
    """
    Function to make a GET request to the specified URL with given parameters and headers.

    Args:
        url (str): The API endpoint to make a request.
        querystring (dict): The dictionary of parameters to send in the request.
        key (str): The API key for authentication.
        method (str): The HTTP method for the request. Defaults to 'GET'.

    Returns:
        Response: The Response object from the request.
    """
    url = url
    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }
    response = requests.request(method, url, headers=headers, params=querystring)

    return response


def get_api_football(url, querystring, key):
    """
    Function to get the data from the football API and handle rate limits.

    Args:
        url (str): The API endpoint to make a request.
        querystring (dict): The dictionary of parameters to send in the request.
        key (str): The API key for authentication.

    Returns:
        str: The JSON response from the API as a string.
    """

    response = get_api_response(url, querystring, key, method="GET")

    json_response = response.text
    print(response.status_code, '::', response.url)
    print(response.headers)

    if response.status_code == TOO_MANY_REQUESTS:
        print(response.text)
        # time.sleep(61)

    return json_response


def draw_pretty_json(json_resp):
    """
    Function to parse and pretty-print a JSON string.

    Args:
        json_resp (str): The JSON string to parse and print.

    Returns:
        dict: The parsed JSON as a dictionary.
    """
    parsed = json.loads(json_resp)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    return parsed


def get_championship_data(url, key, initial=FIRST):
    """
    Function to fetch championship data from the football API and control time between requests.

    Args:
        url (str): The API endpoint to make a request.
        key (str): The API key for authentication.
        initial (int): The initial page number to start fetching data from. Defaults to 'FIRST'.

    Returns:
        DataFrame: The fetched data as a pandas DataFrame.
    """
    df = pd.DataFrame()
    
    #//!  The below is for getting multiple 'pages' of data through different api_calls,
    #//! This currently stands at 39 api_calls and is not currently viable as I only have 100 per day.
    # request_x_minute = 30
    # dfs = []
    # for page_ in range(initial, get_total_pages()):
    #     qs = {"league": CHAMPIONSHIP, "season": SEASON, "page": page_}
    #     json_response = get_api_football(url, qs, key)
    #     parsed = json.loads(json_response)
    #     api_data = get_data(parsed)
    #     dfs.append(api_data)

    #     # You have to control time between requests in the BASIC Plan.
    #     if page_ == request_x_minute - 2:
    #         # Sleep the process to avoid TOO_MANY_REQUESTS
    #         time.sleep(121)        
    # df = pd.concat(dfs, ignore_index=True)
    
    qs = {"league": CHAMPIONSHIP, "season": SEASON, "page": initial}
    json_response = get_api_football(url, qs, key)
    parsed = json.loads(json_response)
    api_data = get_data(parsed)

    df = pd.concat([api_data], ignore_index=True)
    print(df)
    return df


def clean_weight_height(df):
    """
    Function to clean the weight and height data in a DataFrame.

    Args:
        df (DataFrame): The DataFrame to clean.

    Returns:
        DataFrame: The cleaned DataFrame.
    """
    # df['Weight_kg'] = (df['Weight'].str.extract('^([0-9]{2,3})')).astype(float) #//! this currenty does not seem to work
    df['Height_cm'] = (df['Height'].str.extract('^([0-9]{3})')).astype(float)

    df.drop(['Weight', 'Height'], axis=1, inplace=True)

    return df


# Loop all passes accuracy api page team
def get_data(parsed):
    """
    Function to parse the fetched data and return it as a DataFrame.

    Args:
        parsed (dict): The parsed JSON data as a dictionary.

    Returns:
        DataFrame: The parsed data as a pandas DataFrame.
    """
    # General
    id_list = []
    team_list = []
    name_list = []
    position_list = []
    age_list = []
    height_list = []
    weight_list = []
    nationality_list = []
    injured_list = []
    photo_list = []
    logo_team_list = []
    rating_list = []
    captain_list = []

    # Passes
    passes_acc_list = []
    passes_total_list = []
    passes_key_list = []

    # Shots
    shots_on_list = []
    shots_total_list = []

    # Fouls
    fouls_drawn_list = []
    fouls_comm_list = []

    # Dribbles
    dribbles_attempts = []
    dribbles_past = []
    dribbles_success = []

    # Games
    games_app_list = []
    games_minutes_list = []
    games_rating_list = []

    # Goals
    goals_total_list = []
    goals_assist_list = []
    goals_conc_list = []
    goals_saved_list = []

    # Tackles
    tackles_blocks_list = []
    tackles_inter_list = []
    tackles_total_list = []

    # Duels
    duels_won_list = []
    duels_total_list = []

    # Cards
    yellow_card_list = []
    red_card_list = []
    yellowred_card_list = []

    # print("Longitud parsed[response]: {}".format(len(parsed['response'])))
    # print("parsed_stats_league[results]: {}".format(parsed['results']))
    for i in range(0, parsed['results']):
        # Mains
        response = parsed['response'][i]
        stats = response['statistics'][0]

        # General
        id_player = response['player']['id']
        team = stats['team']['name']
        logo_team = stats['team']['logo']
        name = response['player']['name']
        age = response['player']['age']
        height = response['player']['height']
        weight = response['player']['weight']
        nationality = response['player']['nationality']
        injured = response['player']['injured']
        photo = response['player']['photo']

        # Appends
        position_list.append(stats['games']['position'])
        rating_list.append(stats['games']['rating'])
        captain_list.append(stats['games']['captain'])
        age_list.append(age)
        height_list.append(height)
        weight_list.append(weight)
        nationality_list.append(nationality)
        injured_list.append(injured)
        photo_list.append(photo)
        id_list.append(id_player)
        team_list.append(team)
        name_list.append(name)
        logo_team_list.append(logo_team)

        # Cards
        yellow_card_list.append(stats['cards']['yellow'])
        red_card_list.append(stats['cards']['red'])
        yellowred_card_list.append(stats['cards']['yellowred'])

        # Passes
        passes_acc_list.append(stats['passes']['accuracy'])
        passes_total_list.append(stats['passes']['total'])
        passes_key_list.append(stats['passes']['key'])

        # Shots
        shots_on_list.append(stats['shots']['on'])
        shots_total_list.append(stats['shots']['total'])

        # Fouls
        fouls_drawn_list.append(stats['fouls']['drawn'])
        fouls_comm_list.append(stats['fouls']['committed'])

        # Dribbles
        dribbles_attempts.append(stats['dribbles']['attempts'])
        dribbles_past.append(stats['dribbles']['past'])
        dribbles_success.append(stats['dribbles']['success'])

        # Games
        games_app_list.append(stats['games']['appearences'])
        games_minutes_list.append(stats['games']['minutes'])
        games_rating_list.append(stats['games']['rating'])

        # Goals
        goals_total_list.append(stats['goals']['total'])
        goals_assist_list.append(stats['goals']['assists'])
        goals_conc_list.append(stats['goals']['conceded'])
        goals_saved_list.append(stats['goals']['saves'])

        # Tackles
        tackles_blocks_list.append(stats['tackles']['blocks'])
        tackles_inter_list.append(stats['tackles']['interceptions'])
        tackles_total_list.append(stats['tackles']['total'])

        # Duels
        duels_total_list.append(stats['duels']['total'])
        duels_won_list.append(stats['duels']['won'])

    api_data = pd.DataFrame({"Id": id_list, "Name": name_list,
        "Age": age_list,
        "Height": height_list,
        "Weight": weight_list,
        "Nationality": nationality_list,
        "Injured": injured_list,
        "Team": team_list,
        "Position": position_list,
        "Games": games_app_list,
        "Minutes": games_minutes_list,
        "Accuracy_Passes": passes_acc_list,
        "Key_Passes": passes_key_list,
        "Total_Passes": passes_total_list,
        "Shots_On": shots_on_list,
        "Shots_Total": shots_total_list,
        "Dribbles_Attempts": dribbles_attempts,
        "Dribbles_Past": dribbles_past,
        "Dribbles_Success": dribbles_success,
        "Fouls_Drawn": fouls_drawn_list,
        "Fouls_Committed": fouls_comm_list,
        "Tackled_Block": tackles_blocks_list,
        "Tackled_Intercept": tackles_inter_list,
        "Tackled_Total": tackles_total_list,
        "Duels_Won": duels_won_list,
        "Duels_Total": duels_total_list,
        "Goals_Assist": goals_assist_list,
        "Goals_Total": goals_total_list,
        "Goals_Conceded": goals_conc_list,
        "Goals_Saves": goals_saved_list,
        "Photo": photo_list,
        "Logo_Team": logo_team_list,
        "Rating": rating_list,
        "Yellow_Cards": yellow_card_list,
        "Red_Cards": red_card_list,
        "Yellow_Red_Cards": yellowred_card_list,
        "Captain": captain_list
        })
    return api_data