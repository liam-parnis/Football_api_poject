import pandas as pd
from fuzzywuzzy import process
from utils.football_classes import FootballPlayer 

# Output the top matches and their scores
# for match, score in [(x[0], x[1]) for x in top_matches]:
#     print(f"Match: {match}, Score: {score}")

def choose_player(df: pd.DataFrame,user_input: str) -> pd.DataFrame:
    """This function will be used to find the player that the user inputs in the database.
    It uses fuzzy matching so that different inputs can be accepted. 
    The output of this should be the row of the dataframe that is applicable so that it can
    be stored as a player object and used in later analysis. 

    Args:
        df (pd.DataFrame): The player dataframe from the api to compare to the given player name
        user_input (str): The player that the user wants to add into his team.
    Returns:
        df: The output which is applicable to the player chosen by the user
    """
    top_matches = process.extract(user_input, df['Name'], limit=3)
    
    
    best_match_row = df[df["Name"] == top_matches[0][0]]
    second_best_match = df[df["Name"] == top_matches[1][0]]
    third_best_match = df[df["Name"] == top_matches[2][0]]
    selected_player = None
    
    while True:
        correct_player = input(f'Do you mean: {top_matches[0][0]}?. He plays for {best_match_row["Team"].iloc[0]} right? Please use Y/N or E to exit').upper()
        if correct_player in ['Y', 'N']:
            selected_player = best_match_row
            break
        elif correct_player == 'E':
            print("Exiting the process.")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    if correct_player == 'N':
        while True:
            second_try = input(f'My apologies,do you mean: {top_matches[1][0]}?. He plays for {second_best_match["Team"].iloc[0]} right? Please use Y/N or E to exit').upper()
            if second_try in ['Y', 'N']:
                selected_player = second_best_match
                break
            elif correct_player == 'E':
                print("Exiting the process.")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        if second_try == 'N':
            while True:
                last_try = input(f'My apologies,lets try one more time. Do you mean: {top_matches[2][0]}?. He plays for {third_best_match["Team"].iloc[0]} right? Please use Y/N or E to exit').upper()
                if second_try in ['Y', 'N']:
                    selected_player = third_best_match
                    break
                elif correct_player == 'E':
                    print("Exiting the process.")
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
            if last_try == 'N':
                print(f'Please try again, here is a list of all names for reference: {df[df["Position"] == "Goalkeeper"].Name}')
            else:
                print(f'Excellent! You have successfully added {top_matches[2][0]} to your side!')
        else:
            print(f'You have successfully added {top_matches[1][0]} to your side!')    
    else:
        print(f'You have successfully added {top_matches[0][0]} to your side!')
        
    # Have to convert the pandas df with 1 row into a Series
    selected_player = selected_player.iloc[0]   
    return selected_player 




def creating_player_instances(select_player: pd.Series) -> dict:
    """This function creates a player instance and stores it in a dictionary to be used later in the code,

    Args:
        select_player (pd.Series): This is the series which contains the data of the player that has been chosen by the user.

    Returns:
        dict: all players that the user has inputted are stored with the key being the players name.
    """
    
    players = {}
    player = FootballPlayer(select_player["Id"], select_player["Name"], select_player["Age"],select_player["Team"], select_player["Position"])
    players[player.Name] = player
