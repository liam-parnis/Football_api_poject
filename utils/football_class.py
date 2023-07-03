import pandas as pd

class FootballPlayer:
    def __init__(self, Id, Name, Age, Height, Weight, Nationality, Injured, Team, Position,
                 Games, Minutes, Accuracy_Passes, Key_Passes, Total_Passes, Shots_On,
                 Shots_Total, Dribbles_Attempts, Dribbles_Past, Dribbles_Success,
                 Fouls_Drawn, Fouls_Committed, Tackled_Block, Tackled_Intercept,
                 Tackled_Total, Duels_Won, Duels_Total, Goals_Assist, Goals_Total,
                 Goals_Conceded, Goals_Saves,Photo,Logo_Team,Rating, Yellow_Cards,
                 Red_Cards, Yellow_Red_Cards, Captain):
        self.Player_ID = Id
        self.Name = Name
        self.Age = Age
        self.Height = Height
        self.Weight = Weight
        self.Nationality = Nationality
        self.Injured = Injured
        self.Team = Team
        self.Position = Position
        self.Games = Games
        self.Minutes = Minutes
        self.Accuracy_Passes = Accuracy_Passes
        self.Key_Passes = Key_Passes
        self.Total_Passes = Total_Passes
        self.Shots_On = Shots_On
        self.Shots_Total = Shots_Total
        self.Dribbles_Attempts = Dribbles_Attempts
        self.Dribbles_Past = Dribbles_Past
        self.Dribbles_Success = Dribbles_Success
        self.Fouls_Drawn = Fouls_Drawn
        self.Fouls_Committed = Fouls_Committed
        self.Tackled_Block = Tackled_Block
        self.Tackled_Intercept = Tackled_Intercept
        self.Tackled_Total = Tackled_Total
        self.Duels_Won = Duels_Won
        self.Duels_Total = Duels_Total
        self.Goals_Assist = Goals_Assist
        self.Goals_Total = Goals_Total
        self.Goals_Conceded = Goals_Conceded
        self.Goals_Saves = Goals_Saves
        self.Photo = Photo
        self.Logo_Team = Logo_Team
        self.Rating = Rating
        self.Yellow_Cards = Yellow_Cards
        self.Red_Cards = Red_Cards
        self.Yellow_Red_Cards = Yellow_Red_Cards
        self.Captain = Captain

    def __repr__(self):
        return f"Player(id={self.Player_ID}, name={self.Name.encode('utf-8')}, age={self.Age}, team={self.Team.encode('utf-8')})"
    
    # In the updated code, the __repr__ method now explicitly encodes the Name and Team attributes using 
    # UTF-8 encoding. This ensures that any non-ASCII characters are handled properly during printing.

# Player data for n players
# for next time I want to feed in the pandas df from main.py and 
# convert it into a list of dictionaries using:

# player_data = df.to_dict('records')

# To convert the DataFrame into a list of dictionaries, we use the to_dict() 
# method with the parameter 'records', which returns a list of dictionaries where 
# each dictionary represents a player with their attribute-value pairs.


df = pd.read_csv(r'C:\Users\liamp\OneDrive\Desktop\Liams_path_to_Data_science\Football_api_project\Output_files\df_championship_39_2021_full.csv')
players_data = df.to_dict('records')

# Creating player instances dynamically
players = [FootballPlayer(**data) for data in players_data]

# Printing the DataFrame
for player in players:
    print(player)