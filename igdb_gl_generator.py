"""Code to download data from IGDB and fusion with a csv file."""
import pandas as pd
import functions

# This are the elements and routes necessarys to process the data
game_list = pd.read_csv("datasets/filtered_games_db.csv")
relation_df = pd.read_csv("datasets/platform_relation.csv")

# First we do the research to receive data about the games
new_list = game_list.apply(functions.process_row, axis=1)

# This are the elements and routes necessarys to create a relation
PROCESSED_ROUTE = "datasets/processed_game_list.csv"
NOT_FOUND_ROUTE = "datasets/games_not_found.csv"
dataframe = pd.read_csv(PROCESSED_ROUTE)
not_found_df = pd.read_csv(NOT_FOUND_ROUTE)

# Then we look for a relation between the platforms to homologate the info for processed_df
processed_fusion = functions.relation(dataframe, relation_df)
processed_fusion = processed_fusion.drop_duplicates()
functions.export_to_csv(PROCESSED_ROUTE, processed_fusion, "w")

# Then we look for a relation between the platforms to homologate the info for not found games
not_found_fusion = functions.relation(not_found_df, relation_df)
not_found_fusion = not_found_fusion.drop_duplicates()
functions.export_to_csv(NOT_FOUND_ROUTE, not_found_fusion, "w")

print("Process Complete")
