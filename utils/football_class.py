import pandas as pd

class FootballPlayer:
    def __init__(self, player_id, name, age, height, weight, nationality, injured, team, position,
                 games, minutes, accuracy_passes, key_passes, total_passes, shots_on,
                 shots_total, dribbles_attempts, dribbles_past, dribbles_success,
                 fouls_drawn, fouls_committed, tackled_block, tackled_intercept,
                 tackled_total, duels_won, duels_total, goals_assist, goals_total,
                 goals_conceded, goals_saves,Photo,Logo_Team,rating, yellow_cards,
                 red_cards, yellow_red_cards, captain):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.nationality = nationality
        self.injured = injured
        self.team = team
        self.position = position
        self.games = games
        self.minutes = minutes
        self.accuracy_passes = accuracy_passes
        self.key_passes = key_passes
        self.total_passes = total_passes
        self.shots_on = shots_on
        self.shots_total = shots_total
        self.dribbles_attempts = dribbles_attempts
        self.dribbles_past = dribbles_past
        self.dribbles_success = dribbles_success
        self.fouls_drawn = fouls_drawn
        self.fouls_committed = fouls_committed
        self.tackled_block = tackled_block
        self.tackled_intercept = tackled_intercept
        self.tackled_total = tackled_total
        self.duels_won = duels_won
        self.duels_total = duels_total
        self.goals_assist = goals_assist
        self.goals_total = goals_total
        self.goals_conceded = goals_conceded
        self.goals_saves = goals_saves
        self.Photo = Photo
        self.Logo_Team = Logo_Team
        self.rating = rating
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.yellow_red_cards = yellow_red_cards
        self.captain = captain

    def __repr__(self):
        return f"Player(id={self.player_id}, name={self.name}, age={self.age}, team={self.team})"

# Player data for n players
# for next time I want to feed in the pandas df from main.py and convert it into a list of dictionaries using:

# player_data = df.to_dict('records')

# To convert the DataFrame into a list of dictionaries, we use the to_dict() 
# method with the parameter 'records', which returns a list of dictionaries where 
# each dictionary represents a player with their attribute-value pairs.


players_data = [
    (1, "Alice", 25, "5'8", 150, "England", False, "Team A", "Forward",
     10, 900, 80, 15, 100, 8, 12, 20, 10, 8,
     6, 5, 3, 2, 40, 25, 30, 7, 10,
     0, 0, 0, 0, 7.5, 2,
     0, 0, False),
    (2, "Bob", 28, "6'0", 170, "Spain", False, "Team B", "Midfielder",
     12, 800, 85, 20, 150, 12, 15, 25, 18, 15,
     10, 8, 5, 3, 60, 35, 45, 10, 5,
     0, 0, 0, 0, 8.0, 3,
     1, 0, False),
    (3, "Charlie", 23, "5'10", 160, "France", True, "Team A", "Defender",
     8, 600, 75, 10, 80, 5, 8, 15, 5, 10,
     4, 6, 8, 4, 35, 20, 30, 0, 0,
     0, 0, 1, 0, 7.2, 1,
     0, 0, False)
]




# Creating player instances dynamically
players = [FootballPlayer(*data) for data in players_data]

# Creating a DataFrame to store player data
data = {
    "ID": [player.player_id for player in players],
    "Name": [player.name for player in players],
    "Age": [player.age for player in players],
    "Height": [player.height for player in players],
    "Weight": [player.weight for player in players],
    "Nationality": [player.nationality for player in players],
    "Injured": [player.injured for player in players],
    "Team": [player.team for player in players],
    "Position": [player.position for player in players],
    "Games": [player.games for player in players],
    "Minutes": [player.minutes for player in players],
    "Accuracy_Passes": [player.accuracy_passes for player in players],
    "Key_Passes": [player.key_passes for player in players],
    "Total_Passes": [player.total_passes for player in players],
    "Shots_On": [player.shots_on for player in players],
    "Shots_Total": [player.shots_total for player in players],
    "Dribbles_Attempts": [player.dribbles_attempts for player in players],
    "Dribbles_Past": [player.dribbles_past for player in players],
    "Dribbles_Success": [player.dribbles_success for player in players],
    "Fouls_Drawn": [player.fouls_drawn for player in players],
    "Fouls_Committed": [player.fouls_committed for player in players],
    "Tackled_Block": [player.tackled_block for player in players],
    "Tackled_Intercept": [player.tackled_intercept for player in players],
    "Tackled_Total": [player.tackled_total for player in players],
    "Duels_Won": [player.duels_won for player in players],
    "Duels_Total": [player.duels_total for player in players],
    "Goals_Assist": [player.goals_assist for player in players],
    "Goals_Total": [player.goals_total for player in players],
    "Goals_Conceded": [player.goals_conceded for player in players],
    "Goals_Saves": [player.goals_saves for player in players],
    # I have not included phot and logo_team as they do not provide any value
    "Rating": [player.rating for player in players],
    "Yellow_Cards": [player.yellow_cards for player in players],
    "Red_Cards": [player.red_cards for player in players],
    "Yellow_Red_Cards": [player.yellow_red_cards for player in players],
    "Captain": [player.captain for player in players]
}
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
