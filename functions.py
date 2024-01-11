'''Area destinated to store the functions to be applied'''

import pandas as pd
import token_api


def process_row(row):
    '''I will get a list for each row in order to use it as parameters
    (game name and game platform)'''
    game = row["name"]
    platform = row["platform_igdb"]
    games_data = token_api.game_request(game, platform)
    output_file = "./datasets/processed_game_list.csv"
    if games_data == "no game data":
        return
    # print(games_data)
    df = normalize(games_data, game)
    export_to_csv(output_file, df, "a")
    dataframe = pd.read_csv(output_file)
    year_format(dataframe)
    export_to_csv(output_file, dataframe, "w")
    return 'Process Complete'


def normalize(games_data, db_name):
    '''Function to transform the json into a DataFrame'''
    game_name = games_data[0]["name"]
    platforms = games_data[0]["platforms"]
    dates = games_data[0]["release_dates"]

    df_platforms = pd.json_normalize(platforms, sep="_")
    df_dates = pd.json_normalize(dates, sep="_")
    result = pd.merge(
        df_platforms["name"], df_dates["human"], left_index=True, right_index=True, )
    result = result.rename(
        columns={"human": "release_date", "name": "platform"})
    result["game_name"] = game_name
    result["db_name"] = db_name
    return result


def export_to_csv(route, dataframe, wmode):
    '''Save DataFrame in a csv file using with'''
    with open(route, wmode, encoding="utf-8", newline="") as f:
        # f.tell() specifies if the file has been executed before
        empty = f.tell() == 0
        # If new, use the headers
        if empty:
            dataframe.to_csv(f, index=False, header=True)
        else:
            # If not, ignore the headers
            dataframe.to_csv(f, index=False, header=False)

# Function to stablish the release date into year format


def year_format(df):
    '''Function to transform the release_date to year'''
    df['year'] = df['release_date'].str.extract(r'\b(\d{4})\b')
    return df


def relation(df, relation_df):
    '''This module will substitute the igdb platform name for the db name'''
    fusion_df = pd.merge(left=df, right=relation_df, how="left",
                         left_on="platform", right_on="platform_igdb")

    fusion_df["platform_x"] = fusion_df["platform_y"]
    fusion_df.drop(columns=["platform_y", "platform_igdb"], inplace=True)
    fusion_df.rename(columns={"platform_x": "platform"}, inplace=True)
    fusion_df.dropna(subset=["platform"], inplace=True)
    return fusion_df
