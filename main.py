from utils.utils import get_championship_data, get_api_key, API_FOOTBALL_PLAYERS_ENDPOINT, \
    save_df_to_csv, clean_weight_height, DATA_PATH,CHAMPIONSHIP


def get_api_data():

    # Get API Key
    key = get_api_key()
    # Get championship dataset
    df_championship = get_championship_data(API_FOOTBALL_PLAYERS_ENDPOINT, key)
    # Save championship dataset in csv format
    # save_df_to_csv(clean_weight_height(df_championship))
    
    result, file_path = save_df_to_csv(df_championship,DATA_PATH,CHAMPIONSHIP)

    if result:
        print("CSV file has been successfully saved at:", file_path)
    else:
        print("Error occurred while saving the CSV file:", file_path)
    
    print((df_championship))

# The main one.
if __name__ == '__main__':
    get_api_data()
