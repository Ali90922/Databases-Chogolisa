import pandas as pd
import os





# have to review this before the seocnd midterm !

# Path to the CSV file
file_path = 'game_plays.csv'

# Load the CSV file in chunks to handle large files efficiently
chunk_size = 10000  # Adjust this based on your system's memory capacity

# Define the output file to save the cleaned data
output_file = 'cleaned_game_plays.csv'

# Remove the existing output file if it exists, so we can append clean chunks
if os.path.exists(output_file):
    os.remove(output_file)

# Columns to be dropped
columns_to_drop = ['description', 'x', 'y', 'st_x', 'st_y']

# Process the file in chunks
for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size, na_values=['NA'])):
    # Print the number of rows before the dropna operation
    print(f"Chunk {i + 1}: Number of rows before dropna: {len(chunk)}")

    # Drop rows where 'team_id_for' or 'team_id_against' have missing values
    chunk.dropna(subset=['team_id_for', 'team_id_against'], inplace=True)

    # Drop the specified columns
    chunk.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    # Print the number of rows after the dropna operation
    print(f"Chunk {i + 1}: Number of rows after cleaning: {len(chunk)}")

    # Append the cleaned chunk to the output CSV file
    chunk.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))

print("Cleaning complete. Check the log for row counts before and after the operation.")
