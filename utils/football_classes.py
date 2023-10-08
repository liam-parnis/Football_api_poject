import pandas as pd

class FootballPlayer:
    
    def __init__(self,Id,Name,Age,Team,Position):
        self.Player_ID = Id
        self.Name = Name
        self.Age = Age
        self.Team = Team
        self.Position = Position
        
    def __str__(self):
        return f"Name: {self.Name}, Age: {self.Age}, Team: {self.Team}, Position: {self.Position}"

    # def __repr__(self):
    #     return f"Player(id={self.Player_ID}, name={self.Name.encode('utf-8')}, age={self.Age}, team={self.Team.encode('utf-8')})"
            
    def create_player_from_row(cls,row):
        # To get the plain value from this sub-Series, you should use the 
        # .values attribute and then take the first value from the resulting numpy array.
        return FootballPlayer(
            row["Id"].values[0], 
            row["Name"].values[0], 
            row["Age"].values[0], 
            row["Team"].values[0], 
            row["Position"].values[0]
        )

# def __init__(self, Id, Name, Age, Height, Weight, Nationality, Injured, Team, Position,
    #              Games, Minutes, Accuracy_Passes, Key_Passes, Total_Passes, Shots_On,
    #              Shots_Total, Dribbles_Attempts, Dribbles_Past, Dribbles_Success,
    #              Fouls_Drawn, Fouls_Committed, Tackled_Block, Tackled_Intercept,
    #              Tackled_Total, Duels_Won, Duels_Total, Goals_Assist, Goals_Total,
    #              Goals_Conceded, Goals_Saves,Photo,Logo_Team,Rating, Yellow_Cards,
    #              Red_Cards, Yellow_Red_Cards, Captain):
    #     self.Player_ID = Id
    #     self.Name = Name
    #     self.Age = Age
    #     self.Height = Height
    #     self.Weight = Weight
    #     self.Nationality = Nationality
    #     self.Injured = Injured
    #     self.Team = Team
    #     self.Position = Position
    #     self.Games = Games
    #     self.Minutes = Minutes
    #     self.Accuracy_Passes = Accuracy_Passes
    #     self.Key_Passes = Key_Passes
    #     self.Total_Passes = Total_Passes
    #     self.Shots_On = Shots_On
    #     self.Shots_Total = Shots_Total
    #     self.Dribbles_Attempts = Dribbles_Attempts
    #     self.Dribbles_Past = Dribbles_Past
    #     self.Dribbles_Success = Dribbles_Success
    #     self.Fouls_Drawn = Fouls_Drawn
    #     self.Fouls_Committed = Fouls_Committed
    #     self.Tackled_Block = Tackled_Block
    #     self.Tackled_Intercept = Tackled_Intercept
    #     self.Tackled_Total = Tackled_Total
    #     self.Duels_Won = Duels_Won
    #     self.Duels_Total = Duels_Total
    #     self.Goals_Assist = Goals_Assist
    #     self.Goals_Total = Goals_Total
    #     self.Goals_Conceded = Goals_Conceded
    #     self.Goals_Saves = Goals_Saves
    #     self.Photo = Photo
    #     self.Logo_Team = Logo_Team
    #     self.Rating = Rating
    #     self.Yellow_Cards = Yellow_Cards
    #     self.Red_Cards = Red_Cards
    #     self.Yellow_Red_Cards = Yellow_Red_Cards
    #     self.Captain = Captain
    

    
    # In the updated code, the __repr__ method now explicitly encodes the Name and Team attributes using 
    # UTF-8 encoding. This ensures that any non-ASCII characters are handled properly during printing.
    
    


# Printing the DataFrame
# for player in players:
#     print(player)

# def picking_starting_11(df: pd.DataFrame):
#     GK_name = input("Hello, Who would you like to select as your starting GK? PLease give first and last names")
#     Search_dataframe = df[df["Name"] = GK_name]

#     input()


# df = pd.read_csv(r'C:\Users\liamp\OneDrive\Desktop\Liams_path_to_Data_science\Football_api_project\Output_files\df_championship_39_2021_full.csv')
        


class Team:
    def __init__(self):
        self.players = {}

    def add_player(self, player):
        self.players.append(player)

    def get_players_by_position(self, position):
        return [player for player in self.players if player.Position == position]

#! I am currently looking for ways how to store the data being given for later analysis,
#! I have been recommended pickle files, CSV or even an SQL database: https://chat.openai.com/c/8102548e-2f16-4460-97b5-928767b21b6c